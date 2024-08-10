from flask import Flask
from flask import render_template
from flask import request

from downloader import download_one_video, download_playlist

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def download():
    data = request.json
    url = data.get('url', None)
    extension = data.get('extension', None)
    playlist = data.get('playlist', None)

    if not playlist:
        response = download_one_video(url=url, extension=extension)
    else:
        response = download_playlist(url=url, extension=extension)
    return response


if __name__ == '__main__':
    app.run(debug=True)
