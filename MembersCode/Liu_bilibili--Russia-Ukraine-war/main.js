const playwright = require('playwright');
const axios = require('axios');
const fs = require('fs');


(async () => {
  const browser = await playwright.chromium.launch({ headless: false }); // 设为 false 以便调试
  const context = await browser.newContext();
  const page = await context.newPage();

  // 导航到目标页面
  await page.goto('https://search.bilibili.com/all?vt=27035598&keyword=%E4%BF%84%E4%B9%8C%E6%88%98%E4%BA%89&from_source=webtop_search&spm_id_from=333.1007&search_source=5');

  // 等待并抓取 #exploreFeeds 元素内容
  try {
    await page.evaluate(() => {
        window.scrollTo(0, 1000)
    } );
   let arr = []
   //await page.waitForSelector('section', { timeout: 10000 });

   for (let i = 0 ; i < 2 ; i++){
       await page.waitForSelector('div.col_3.col_xs_1_5.col_md_2.col_xl_1_7.mb_x40', { timeout: 10000 });
       const content = await page.$$eval('div.col_3.col_xs_1_5.col_md_2.col_xl_1_7.mb_x40', els => {
           return els.map(item => {     
               return {
                "title":item.querySelector('div.bili-video-card__info--right h3.bili-video-card__info--tit').title,

                "bofangliang":item.querySelector('span.bili-video-card__stats--item span').innerHTML,
             
                "Time":item.querySelector('div.bili-video-card__stats span.bili-video-card__stats__duration').innerHTML,
                
                "author":item.querySelector('a.bili-video-card__info--owner span.bili-video-card__info--author').innerHTML,
                
                "img":item.querySelector('picture.v-img.bili-video-card__cover img').src,
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

 //下载图片的方法
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