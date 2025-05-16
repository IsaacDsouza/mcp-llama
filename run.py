from models.llama_runner import run_prompt
from email_utils import send_email

def parse_email_request(input_str: str):
    if "send an email to" in input_str:
        try:
            parts = input_str.split("send an email to")[1].strip()
            to_part, rest = parts.split(" with subject ")
            subject_part, body_part = rest.split(" and body ")
            return to_part.strip(), subject_part.strip(), body_part.strip()
        except ValueError:
            return None
    return None

def main():
    print("Welcome to the LLaMA Email Agent!")
    print("Type your email request (e.g., 'Send an email to...') or type 'exit' to quit.")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            break
        
        email_parts = parse_email_request(user_input)
        if email_parts:
            to, subject, body = email_parts
            result = send_email(to, subject, body)
            print(result)
        else:
            response = run_prompt(user_input)
            print("llama(email)", response)

if __name__ == "__main__":
    main()
