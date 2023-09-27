from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

def get_thumbnail_urls(video_url):
    youtube_video = YouTube(video_url)
    thumbnails = {
        "default": youtube_video.thumbnail_url,
        "medium": youtube_video.thumbnail_url.replace("default.jpg", "mqdefault.jpg"),
        "high": youtube_video.thumbnail_url.replace("default.jpg", "hqdefault.jpg"),
        "standard": youtube_video.thumbnail_url.replace("default.jpg", "sddefault.jpg"),
        "max_resolution": youtube_video.thumbnail_url.replace("default.jpg", "maxresdefault.jpg")
    }
    return thumbnails

@app.route('/', methods=['GET', 'POST'])
def index():
    thumbnails = {}
    if request.method == 'POST':
        video_url = request.form.get('video_url')
        thumbnails = get_thumbnail_urls(video_url)
    return render_template('index.html', thumbnails=thumbnails)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

def get_thumbnail_urls(video_url):
    youtube_video = YouTube(video_url)
    thumbnails = {
        "default": youtube_video.thumbnail_url,
        "medium": youtube_video.thumbnail_url.replace("default.jpg", "mqdefault.jpg"),
        "high": youtube_video.thumbnail_url.replace("default.jpg", "hqdefault.jpg"),
        "standard": youtube_video.thumbnail_url.replace("default.jpg", "sddefault.jpg"),
        "max_resolution": youtube_video.thumbnail_url.replace("default.jpg", "maxresdefault.jpg")
    }
    return thumbnails

@app.route('/', methods=['GET', 'POST'])
def index():
    thumbnails = {}
    if request.method == 'POST':
        video_url = request.form.get('video_url')
        thumbnails = get_thumbnail_urls(video_url)
    return render_template('index.html', thumbnails=thumbnails)

if __name__ == '__main__':
    app.run(debug=True)
