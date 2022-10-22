from flask import Flask,render_template
from naver_webtoon_best import get_best_challenge50

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webtoons')
def webtoons():
    view_count_url="https://comic.naver.com/genre/bestChallenge?m=main&order=ViewCount"
    views=get_best_challenge50(view_count_url)
    return render_template('webtoons.html',views=views)

if __name__=="__main__":
    app.run(debug=True)
