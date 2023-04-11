from flask import Flask, render_template, request
from includes import VideoProcessing, AudioProcessing, TextProcessing

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods = ['POST'])
def translate():
    url = request.form.get('url')
    
    VideoProcessing.get_video(url=url)
    AudioProcessing.get_audio()
    
    textProcessing = TextProcessing()
    text = textProcessing.to_text()

    
    return render_template('result.html', text=text)


if __name__ == "__main__":
    app.run(port=3000, debug=True)