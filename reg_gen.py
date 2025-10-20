from openai import OpenAI
import re

client = OpenAI()
# Function to interact with GPT-4 API
def generate_parser_code(log_sample):
    prompt = f"""
I have Apache log data, and I need a Python script to parse it. Here is a sample log line:

{log_sample}

The script should:
1. Use regex to parse the log line into fields depending on the sample
3. Include a function named "process_log_file" to process a log file and output the parsed data as a JSON file.

Generate only the Python script.
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an expert Python developer."},
                  {"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content

# Sample Apache log line
log_sample = '[Sun Dec 04 04:47:44 2005] [notice] workerEnv.init() ok /etc/httpd/conf/workers2.properties'

            


def get_first_three_lines(file_path):
    """
    Reads the first three lines of a file and appends them to a list.

    Args:
        file_path (str): Path to the file.

    Returns:
        list: A list containing the first three lines of the file.
    """
    lines = []
    try:
        with open(file_path, 'r') as file:
            for i, line in enumerate(file):
                if i >= 3:  # Stop after reading 3 lines
                    break
                lines.append(line.strip())  # Strip removes leading/trailing whitespace
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return lines

# Example usage:
# file_path = "path/to/apache_log_file.log"
first_three_lines = get_first_three_lines("C:/Users/admin/Documents/GitHub/RegLOG/data/logs/Apache/Apache_2k.log")
# print(first_three_lines)



def extract_code_inside_backticks(generated_code):
    """
    Extracts content inside the triple backticks from the generated code.

    Args:
        generated_code (str): The full response with markdown formatting.

    Returns:
        str: Extracted code inside the backticks.
    """
    match = re.search(r"```(?:python)?\n(.*?)```", generated_code, re.S)
    return match.group(1) if match else ""

log_sample2 = "/n".join(first_three_lines)
# Generate parser code
generated_code = generate_parser_code(log_sample2)

cleaned_code = extract_code_inside_backticks(generated_code)


# Save the generated code to a file
output_file = "generated_parser2.py"
with open(output_file, "w") as f:
    f.write(cleaned_code)

print(f"Python parser script generated and saved to {output_file}")
