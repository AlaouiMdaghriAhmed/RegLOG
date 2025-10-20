import re
import json

def parse_log_line(line):
    pattern = r'\[(.*?)\] \[(.*?)\] (.*)'
    match = re.search(pattern, line)
    if match:
        return {
            'timestamp': match.group(1),
            'log_level': match.group(2),
            'message': match.group(3)
        }
    else:
        return None

def process_log_file(log_file_path, output_file_path):
    parsed_data = []
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            parsed_line = parse_log_line(line)
            if parsed_line:
                parsed_data.append(parsed_line)

    with open(output_file_path, 'w') as output_file:
        json.dump(parsed_data, output_file)

# Example usage:
# process_log_file('apache.log', 'parsed_data.json')
