from flask import Flask, request, render_template

app = Flask(__name__)

#@app.route('/')
#def my_form():
#    return render_template('html-gui.html')

@app.route('/', methods=['GET'])
def dropdown():
    social_media = ['facebook', 'instagram', 'twitter']
    return render_template('html-gui.html', social_media=social_media)


app.run()
