from flask import Flask, render_template
app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    """
    This application displays the song "Wrecking Ball by Miley Cyrus"
    """
    return render_template('index.html')

