from openai import OpenAI
import random

client = OpenAI()

def extract_templates_from_logs(log_lines):
    """
    Extract generalized log templates from raw log lines using GPT-4.
    """
    prompt = f"""
I have the following Apache log lines, and I need to extract generalized log templates. 
For each log line:
1. Identify constant parts of the log as text.
2. Replace variable parts such as timestamps, numerical values, file paths, and other unique identifiers with the placeholder `<*>`.
3. Ensure that each unique log structure gets a unique EventId, like E1, E2, etc.

Log lines:
{log_lines}

Output the results in the following format:
EventId\tEventTemplate
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert in log analysis and template extraction."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    return response.choices[0].message.content

def sample_logs(log_lines, sample_size):
    """
    Randomly sample a subset of log lines.
    """
    log_lines = log_lines.strip().split("\n")
    return random.sample(log_lines, min(sample_size, len(log_lines)))

# File paths
messages_file_path = r"C:/Users/admin/Documents/GitHub/RegLOG/data/gen/messages.txt"
output_file_path = r"C:/Users/admin/Documents/GitHub/RegLOG/data/gen/apache_log_templates.txt"

# Load log lines from the messages file
with open(messages_file_path, "r") as file:
    log_lines = file.read()

# Extract a sample of log lines
sampled_logs = sample_logs(log_lines, 50)

# Extract templates
templates = extract_templates_from_logs("\n".join(sampled_logs))

# Save templates to a file
with open(output_file_path, "w") as f:
    f.write(templates)

print(f"Templates extracted and saved to {output_file_path}")
