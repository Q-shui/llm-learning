import sys
import json

'''
#从命令行接受文件路径
if len(sys.argv) != 2:
    print("Usage: python jsonl_stats.py <input_file>")
    sys.exit(1)

input_path = sys.argv[1]
total_lines = 0
valid_records = 0
invalid_records = 0
empty_lines = 0
invalid_json_lines = 0
missing_text_lines = 0
invalid_text_lines = 0
text_lengths = []
'''

def main():

    if len(sys.argv) != 2:
        print("Usage: python jsonl_stats.py <input_file>")
        sys.exit(1)

    input_path = sys.argv[1]
    total_lines = 0
    valid_records = 0
    invalid_records = 0
    empty_lines = 0
    invalid_json_lines = 0
    missing_text_lines = 0
    invalid_text_lines = 0
    text_lengths = []

    try:
    #file = open(input_path, 'r', encoding='utf-8')
        with open(input_path, 'r', encoding='utf-8') as file:

            '''
            for _line_number, _line in enumerate(file, start=1):
                print(f"第 {_line_number} 行: {_line}")
            '''


        
            for line_number, line in enumerate(file, start=1):
                
                print(f"第 {line_number} 行: {line}")

                total_lines += 1

                #检查是否为空行
                if not line.strip():
                    empty_lines += 1
                    invalid_records += 1
                    print(f"Warning:line {line_number} is empty.")
                    continue


            #将每一行转换为字典
                try:
                    record = json.loads(line)

                    #判断这一行转换后是不是字典对象
                    if not isinstance(record,dict):
                        invalid_records += 1
                        print(f"Warning:line {line_number} is not a valid JSON object.")
                        continue

                    #检查字典中是否有text字段
                    if 'text' not in record:
                        missing_text_lines += 1
                        invalid_records += 1
                        print(f"Warning:line {line_number} is missing 'text' field.")
                        continue

                    text = record['text']

                    #检查text是否为字符串类型
                    if not isinstance(text,str):
                        invalid_text_lines += 1
                        invalid_records += 1
                        print(f"Warning:line {line_number} 'text' field is not a string.")
                        continue

                    text = text.strip()

                    #检查text是否为空字符串
                    if not text:
                        missing_text_lines += 1
                        invalid_records += 1
                        print(f"Warning:line {line_number} 'text' field is empty.")
                        continue

                    #记录有效记录数和文本长度
                    valid_records += 1
                    text_lengths.append(len(text))

                except json.JSONDecodeError as error:
                    invalid_json_lines += 1
                    invalid_records += 1
                    print(f"Warning:line {line_number} is not valid JSON. Error: {error.msg}")
                    continue

        print(f"总行数:{total_lines}")
        print(f"有效记录数:{valid_records}")
        print(f"无效记录数:{invalid_records}")
        print(f"空行数:{empty_lines}")
        print(f"无效JSON行数:{invalid_json_lines}")
        print(f"缺失文本行数:{missing_text_lines}")
        print(f"无效文本行数:{invalid_text_lines}")

    except FileNotFoundError:
        print(f"Error:file not found:{input_path}")
        sys.exit(1)
'''
try:
    #file = open(input_path, 'r', encoding='utf-8')
    with open(input_path, 'r', encoding='utf-8') as file:


        
        for _line_number, _line in enumerate(file, start=1):
            print(f"第 {_line_number} 行: {_line}")
        

        for line_number, line in enumerate(file, start=1):
            print(f"第 {line_number} 行: {line}")

            #检查是否为空行
            if not line.strip():
                empty_lines += 1
                invalid_records += 1
                print(f"Warning:line {line_number} is empty.")
                continue
            total_lines += 1

            #将每一行转换为字典
            try:
                record = json.loads(line)

                #判断这一行转换后是不是字典对象
                if not isinstance(record,dict):
                    invalid_records += 1
                    print(f"Warning:line {line_number} is not a valid JSON object.")
                    continue

                #检查字典中是否有text字段
                if 'text' not in record:
                    missing_text_lines += 1
                    invalid_records += 1
                    print(f"Warning:line {line_number} is missing 'text' field.")
                    continue

                text = record['text']

                #检查text是否为字符串类型
                if not isinstance(text,str):
                    invalid_text_lines += 1
                    invalid_records += 1
                    print(f"Warning:line {line_number} 'text' field is not a string.")
                    continue

                text = text.strip()

                #检查text是否为空字符串
                if not text:
                    missing_text_lines += 1
                    invalid_records += 1
                    print(f"Warning:line {line_number} 'text' field is empty.")
                    continue

                #记录有效记录数和文本长度
                valid_records += 1
                text_lengths.append(len(text))

            except json.JSONDecodeError as error:
                invalid_json_lines += 1
                invalid_records += 1
                print(f"Warning:line {line_number} is not valid JSON. Error: {error.msg}")
                continue

    print(f"总行数:{total_lines}")
    print(f"有效记录数:{valid_records}")
    print(f"无效记录数:{invalid_records}")
    print(f"空行数:{empty_lines}")
    print(f"无效JSON行数:{invalid_json_lines}")
    print(f"缺失文本行数:{missing_text_lines}")
    print(f"无效文本行数:{invalid_text_lines}")

except FileNotFoundError:
    print(f"Error:file not found:{input_path}")
    sys.exit(1)
'''

if __name__ == "__main__":
    main()