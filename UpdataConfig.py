import json
import os
username = os.getlogin() 

# 使用格式化字符串将变量插入到路径中
UserSetupConfig = f'C:\\Users\\{username}\\.pangu\\UserSetupConfig.json'
UpdataConfig = f'C:\\Users\\{username}\\.pangu\\UpdataConfig.json'

# 从原始 JSON 文件中读取数据, 是否存在提取KaitianRootPath变量值
with open(UserSetupConfig, 'r', encoding='utf-8') as file:
    data = json.load(file)
kaitian_root_path_value = data.get('KaitianRootPath')

#检查 KaitianRootPath 如果存在侧执行
if kaitian_root_path_value:
    # 从目标 JSON 文件读取已存在的数据
    with open(UpdataConfig, 'r', encoding='utf-8') as out_file:
        existing_data = json.load(out_file)

    # 更新数据
    existing_data["KaitianRootPath"] = kaitian_root_path_value

    # 将更新后的数据写回目标 JSON 文件
    with open(UpdataConfig, 'w', encoding='utf-8') as out_file:
        json.dump(existing_data, out_file, ensure_ascii=False, indent=4)
else:
    print('KaitianRootPath not found in JSON file.')
