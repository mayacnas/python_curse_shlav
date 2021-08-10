
from flask import Flask, request, render_template

app = Flask(__name__)

# Main page index.html
@app.route('/')
def my_form():
    return render_template('index.html')

# Gets the input from user in the form
@app.route('/', methods=['GET','POST'])
def my_form_post():
    text = request.form['text']
    return text
    

def main():

    # Runs the app in the local IP address in port 80 (http)
    app.run(host='0.0.0.0', port='80')

if __name__ == '__main__':
    main()
