import requests  
import json  
import os  
  
# 接口的URL  
url = 'https://12.qqwxx.cn/kx/a.json'  # 请将此URL替换为您的实际接口URL  
  
# 发送HTTP GET请求到接口  
response = requests.get(url)  
  
# 检查请求是否成功  
if response.status_code == 200:  
    # 获取接口的JSON响应  
    data = response.json()  
      
    # 将解析后的数据保存到本地文件  
    json_output_file = os.path.join(os.getcwd(), 'output_data.json')  
    with open(json_output_file, 'w', encoding='utf-8') as f:  
        json.dump(data, f, ensure_ascii=False, indent=4)  
      
    # 假设接口响应中包含文件的URL，我们需要下载这些文件  
    # 这里我们假设响应中有一个名为'files'的键，其值是一个包含文件URL的列表  
    # 注意：这只是一个示例，您需要根据实际的接口响应结构来调整代码  
    if 'files' in data:  
        for file_url in data['files']:  
            file_name = os.path.basename(file_url)  # 从URL中提取文件名  
            file_path = os.path.join(os.getcwd(), file_name)  
            file_response = requests.get(file_url)  
              
            if file_response.status_code == 200:  
                with open(file_path, 'wb') as fb:  
                    fb.write(file_response.content)  
                print(f"文件 {file_name} 已成功下载")  
            else:  
                print(f"无法下载文件 {file_name}，状态码：{file_response.status_code}")  
      
    # 打印成功消息  
    print("数据已成功保存到output_data.json文件中，并尝试下载所有相关文件")  
else:  
    # 打印错误信息  
    print(f"请求失败，状态码：{response.status_code}")