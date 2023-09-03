import openai
import config

openai.api_key = config.DevelopmentConfig.OPENAI_KEY

def generate_chat_response(prompt):

    """
    This function generates a chat response and handles API errors.

    It uses the openai.SomeApiCall() function to make an API call and handles
    any openai.error.APIError that may occur.

    Returns:
        str: The chat response or an error message.
    """

    try:
        messages = []
        messages.append({"role": "system", "content": "You are helpful assistant."})

        question = {}
        question['role'] = 'user'
        question['content'] = prompt
        messages.append(question)

        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

        answer = response['choices'][0]['message']['content'].replace('\n','<br>')

    except openai.error.APIError as api_error:

        print(f"An APIError occurred: {api_error}")

    return answer