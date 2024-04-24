from flask import Flask

app = Flask(__name__)

# http://localhost:5000/ -> '/' al final
@app.route('/')
def inicio():
   return 'Hola Mundo desde Flask'


if __name__ == '__main__':
   app.run(debug=True)