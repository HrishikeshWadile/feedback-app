from flask import Flask, render_template, request, redirect

app = Flask(__name__)

data = []

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    rating = request.form['rating']
    comment = request.form['comment']

    data.append({
        "name": name,
        "rating": rating,
        "comment": comment
    })

    return redirect('/responses')

@app.route('/responses')
def responses():
    return render_template('responses.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)