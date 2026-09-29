import argparse
from pathlib import Path
#parser = argparse.ArgumentParser(description="Test argparse")

#parser.add_argument("--name",type = str, help = "用户名称")
#parser.add_argument("--age",type = int, help = "用户年龄")

'''
(llm-learning) PS C:\工作\学习\llm-learning> python .\tests\test_argparse.py --age 20 --name Alice 1 2
姓名：Alice
年龄：20
源文件：1
目标文件：2
(llm-learning) PS C:\工作\学习\llm-learning> python .\tests\test_argparse.py --age 20 --name Alice 2 1
姓名：Alice
年龄：20
源文件：2
目标文件：1

常用参数选项
parser.add_argument(
    "--port",
    type=int,           # 转换数据类型
    default=8080,       # 未输入时的默认值
    required=True,      # 是否必须提供
    help="服务端口",    # 帮助文字
    choices=[80, 443, 8080],  # 限制可选值
)



'''

#parser.add_argument("--host",type = str,default = "127.0.0.1")#有默认参数
#parser.add_argument("--token",required = True)#必须提供参数

#bool开关
#parser.add_argument("--verbose",action = "store_true",help = "启用详细输出")

#接受多个值
#parser.add_argument("--files",nargs = "+",help = "输入文件列表")

#接受重复参数
#parser.add_argument("--tag",action = "append",help = "标签")

#位置参数不带--需要指定顺序
#parser.add_argument("source")
#parser.add_argument("destination")

#读取命令行参数
#args = parser.parse_args()


#print(f"姓名：{args.name}")
#print(f"年龄：{args.age}")
#print(f"源文件：{args.source}")
#print(f"目标文件：{args.destination}")

#print(f"主机：{args.host}")
#print(f"令牌：{args.token}")
#if args.verbose:
#    print("详细输出已启用")

#print(f"输入文件列表：{args.files}")
#print(f"标签：{args.tag}")

def main():
    parser = argparse.ArgumentParser(
        prog = "filetool",
        description="读取文本文件并输出结果",
    )

    #文本路径
    parser.add_argument(
        "--input_path",
        type = Path,
        help = "输入文件路径",
    )

    #输出文件路径，未提供输出到终端
    parser.add_argument(
        "--output_path",
        type = Path,
        help = "输出文件路径,如果未提供则输出到终端",
    )

    #将内容转换为大写
    parser.add_argument(
        "--uppercase",
        action = "store_true",
        help = "将内容转换为大写",
    )

    #文件编码，默认为utf-8
    parser.add_argument(
        "--encoding",
        type = str,
        default = "utf-8",
        help = "文件编码，默认为utf-8",
    )

    args = parser.parse_args()

    if not args.input_path.is_file():
        parser.error(f"Error:输入文件路径 {args.input_path} 不存在")

    content = args.input_path.read_text(encoding=args.encoding)

    if args.uppercase:
        content = content.upper()

    if args.output_path:
        args.output_path.write_text(content,encoding=args.encoding)
        print(f"内容已写入 {args.output_path}")
    else:
        print(content)

if __name__ == "__main__":
    main()

