from flask import Flask, render_template

app = Flask(__name__)


# 5
@app.route('/numbers')
def numbers_page():
    liist = list(range(1, 6))
    return render_template('numbers.html', royxat=liist)


if __name__ == '__main__':
    app.run(debug=True)
