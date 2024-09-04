import json

# 读取 JSON 文件
def read_json_file(file_path):
    """Read JSON data from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {file_path}.")
        return None

# 写入 JSON 文件
def write_json_file(file_path, data):
    """Write JSON data to a file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Data successfully written to {file_path}.")
    except Exception as e:
        print(f"Error writing to {file_path}: {e}")

# 转换播放量格式
def convert_play_count(play_count_str):
    """Convert play count from various formats to an integer string."""
    try:
        if '万' in play_count_str:
            return str(int(float(play_count_str.replace('万', '')) * 10000))
        elif '千' in play_count_str:
            return str(int(float(play_count_str.replace('千', '')) * 1000))
        else:
            return str(int(play_count_str))
    except ValueError:
        print(f"Invalid play count format: {play_count_str}")
        return play_count_str

# 处理 JSON 数据
def process_json_data(data):
    """Process JSON data to update play counts, filter specific fields, and remove duplicates."""
    processed_data = []
    seen = set()  # 用于跟踪已经处理过的条目
    
    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict) and "title" in item and "bofangliang" in item:
                # 构建唯一标识符，结合 title 和 bofangliang 来识别是否重复
                unique_identifier = (item["title"], item["bofangliang"])
                
                if unique_identifier not in seen:
                    # 只保留 "title" 和 "bofangliang" 字段，并转换播放量
                    filtered_item = {
                        "title": item["title"],
                        "bofangliang": convert_play_count(item["bofangliang"])
                    }
                    # 增加播放量
                    filtered_item["bofangliang"] = str(int(filtered_item["bofangliang"]) + 1)
                    
                    # 添加到结果列表，并将该条目标记为已处理
                    processed_data.append(filtered_item)
                    seen.add(unique_identifier)  # 将此条目添加到 seen 集合中

    return processed_data

# 主程序
if __name__ == "__main__":
    # 定义文件路径
    input_file = 'content.json'
    output_file = 'output.json'

    # 读取 JSON 数据
    json_data = read_json_file(input_file)

    if json_data is not None:
        # 处理数据
        processed_data = process_json_data(json_data)

        # 保存处理后的数据到新的 JSON 文件
        write_json_file(output_file, processed_data)
