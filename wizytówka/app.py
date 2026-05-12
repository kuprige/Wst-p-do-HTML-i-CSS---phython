from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/o_mnie')
def o_mnie():
    return render_template('o_mnie.html')

@app.route('/kontakt', methods=['GET', 'POST'])
def kontakt():
    if request.method == 'POST':
        message = request.form.get('message')
        print("Otrzymano wiadomość:", message)
    return render_template('kontakt.html')

if __name__ == '__main__':
    app.run(debug=True)
