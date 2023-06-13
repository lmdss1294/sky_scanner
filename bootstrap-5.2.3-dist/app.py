from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        departure_time = request.form.get('time')
        departure_datetime = datetime.strptime(departure_time, '%Y-%m-%dT%H:%M')
        new_time = departure_datetime + timedelta(hours=5)
        return render_template('result.html',new_time=new_time)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)