from flask import Flask

app = Flask(__name__)

@app.route('/')
def tabla():
    resultado = "<h2>Tabla del 12</h2>"

    for i in range(13):
        resultado += f"12 x {i} = {12*i}<br>"

    return resultado


if __name__ == '__main__':
    app.run(debug=True, port=5000)

