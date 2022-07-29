
from flask import Flask, redirect, url_for, request, render_template
import predictor as pr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('about.html')

@app.route('/catch_phish', methods = ['POST', 'GET'])
def catch_phish():
    if request.method == 'POST':
      url = request.form.get('url')
      print(url)
      return redirect(url_for('results',url = url))
    return render_template('catch_phish.html')

@app.route('/results', methods = ['POST','GET'])
def results():
    # url = request.get_data()
    url = request.form.get('url', None)
    res = pr.classifyURL(url)
    return render_template('results.html', url=url, res=res)

app.run(debug=False)

