const playwright = require('playwright');
const axios = require('axios');
const fs = require('fs');



(async () => {
  const browser = await playwright.chromium.launch({ headless: false }); // 设为 false 以便调试
  const context = await browser.newContext();
  const page = await context.newPage();

  // 导航到目标页面
  await page.goto('https://www.kuaishou.com/search/video?searchKey=%E4%BF%84%E4%B9%8C%E5%86%B2%E7%AA%81');

  // 等待并抓取 #exploreFeeds 元素内容
  try {
    let arr = []
    // await page.waitForSelector('section', { timeout: 10000 });

    for (let i = 0 ; i < 2 ; i++){
        await page.evaluate((idx) => {
            window.scrollTo(0, 800*idx)
        },i);
        await page.waitForSelector('div.video-card.video-item.vertical', { timeout: 10000 });
        const content = await page.$$eval('div.video-card.video-item.vertical', els => {
            return els.map(item => {     
                return {
                    "title":item.querySelector('div.video-info h5.video-info-title').innerHTML,
                    /*"author":item.querySelector('a.author span').innerHTML,*/
                    "like":item.querySelector('div.video-info-content span.info-text').innerHTML,
                    "img":item.querySelector('div img').src,
                };
            })
        });
        arr = arr.concat(content)
        console.log(content);
        console.log(i,"======================================================================");
    }
    writeToJsonFile(arr,"content.json")
    
    arr.forEach(item => {
        // item.img.split("/")[item.img.split("/").length-1]
        downloadImage(item.img,`./imgs/${item.img.split("/")[item.img.split("/").length-1]}.png`)
    })
  } catch (error) {
    console.log('error', error);
  }

  // 关闭浏览器
  await browser.close();
})();

// 写入json文件的写法
function writeToJsonFile(data, filename) {
    const jsonData = JSON.stringify(data, null, 2); // 将数据转换为格式化的 JSON 字符串
    fs.writeFile(filename, jsonData, 'utf8', (err) => {
      if (err) {
        console.error('Error writing to JSON file: ', err);
        return;
      }
      console.log(`Data written to ${filename}`);
    });
}

// 下载图片的方法
async function downloadImage(imageUrl, outputPath) {
    try {
      // 发起 HTTP 请求获取图片数据
      const response = await axios({
        url: imageUrl,
        method: 'GET',
        responseType: 'stream'
      });
  
      // 创建可写流以将图片数据写入到文件
      const writer = fs.createWriteStream(outputPath);
  
      // 将响应流管道到可写流
      response.data.pipe(writer);
  
      // 监听 'finish' 事件，当写入完成时触发
      return new Promise((resolve, reject) => {
        writer.on('finish', resolve);
        writer.on('error', reject);
      });
    } catch (error) {
      console.error('Error downloading image:', error);
      throw error;
    }
  }
  


