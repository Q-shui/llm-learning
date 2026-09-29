import json

input_path = "jsonl_test_data.jsonl"

total_lines = 0#总行数
valid_records = 0#有效行数
invalid_records = 0#无效行数
text_lengths = []#文本长度

with open(input_path, 'r', encoding='utf-8') as file:
    for line_number, line in enumerate(file, start=1):
        total_lines += 1
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            invalid_records += 1
            print(f"Line {line_number} is not a valid JSON record.")
            continue

        text = record.get("text", "")

        if not isinstance(text, str):
            invalid_records += 1
            print(f"Line {line_number} has an invalid 'text' field.")
            continue

        if not text.strip():
            invalid_records += 1
            print(f"Line {line_number} has an empty 'text' field.")
            continue

        valid_records += 1
        text_lengths.append(len(text))


print(f"Total lines: {total_lines}")
print(f"Valid records: {valid_records}")
print(f"Invalid records: {invalid_records}")
print(f"Total text length: {sum(text_lengths)}")