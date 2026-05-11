from flask import Flask, render_template

app = Flask(__name__)

@app.route('/o_mnie')
def o_mnie():
    return render_template('o_mnie.html')

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')

if __name__ == '__main__':
    app.run(debug=True)
