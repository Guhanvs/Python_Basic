import openai

# Set your OpenAI API key directly
openai.api_key = "sk-Z_NhzNEknF9kecQle8F4vvDDwKgT33BhfLbLuCEEyjT3BlbkFJnQeZilyk_BgnKfEJMX25iYEusloR4q86CcJlXCUUEA"  # Replace with your actual API key


def generate_response(prompt):
    try:
        # Send a request to the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can change to "gpt-4" if you have access
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        # Extract and return the response
        return response['choices'][0]['message']['content']

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    # Define a list of prompts
    prompts = [
        "What are the benefits of using renewable energy?",
        "Can you explain the theory of relativity?",
        "Tell me a joke about programmers."
    ]

    # Iterate through prompts and generate responses
    for prompt in prompts:
        print(f"Prompt: {prompt}")
        response = generate_response(prompt)
        print(f"Response: {response}\n")
