from flask import Flask, render_template, request, redirect, url_for, jsonify
import time

app = Flask(__name__)

# Dummy condition function


def dummy_condition():
    time.sleep(5)  # Simulate a delay for the dummy condition
    # Dummy video link
    return "https://cdn.creatomate.com/renders/f59d1c00-2392-4dab-a634-4af229e4b6d5.mp4"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        news_link = request.form['news_link']
        return redirect(url_for('loading', news_link=news_link))
    return render_template('index.html')


@app.route('/loading')
def loading():
    news_link = request.args.get('news_link')
    return render_template('loading.html', news_link=news_link)


@app.route('/result')
def result():
    video_link = dummy_condition()
    return render_template('result.html', video_link=video_link)


if __name__ == '__main__':
    app.run(debug=True)
