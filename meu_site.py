from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def homePage():
    return render_template('homepage.html', titulo='Home')

@app.route('/cidadania')
def cidadania():
    return render_template('cidadania.html', titulo="Cidadania")

@app.route('/novorg')
def novorg():
    return render_template("novorg.html", titulo="Novo Rg")

@app.route('/mapa')
def mapa():
    return render_template("mapa.html", titulo="Mapa")


if __name__ == "__main__":
    app.run(debug=True)