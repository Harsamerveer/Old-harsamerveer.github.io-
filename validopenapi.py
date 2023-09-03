from flask import Flask, render_template
from decouple import config

app = Flask(__name__)

# Access the API key
api_key = config('API_KEY')

# Define a custom error message for missing API key
missing_api_key_message = "API key is missing. Please provide a valid API key."

# Define a route that requires the API key
@app.route('/protected_resource')
def protected_resource():
    if api_key:
        # Your code to access the protected resource using the API key goes here
        return "Protected Resource Accessed Successfully", 200
    else:
        # Return a custom error message if the API key is missing
        return missing_api_key_message, 403  # 403 indicates "Forbidden" due to missing API key

if __name__ == '__main__':
    app.run()
