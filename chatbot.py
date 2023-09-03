
from flask import Flask, render_template, jsonify, request
import config
import openaiapi


def page_not_found(e):
  return render_template('404.html'), 404

def internal_server_error(e):
    return render_template('500.html'), 500

def method_not_found(e):
    return render_template('405.html'), 405

app = Flask(__name__)
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)

app.register_error_handler(500, internal_server_error)

app.register_error_handler(500, method_not_found)




@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        prompt = request.form['prompt']

        res = {'answer': openaiapi.generate_chat_response(prompt)}
        return jsonify(res), 200
    return render_template('ChatBot.html', **locals())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)