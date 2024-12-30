from flask import Flask

app = Flask(__name__)

@app.route('/')
def func():
  return "Welcome to the cloud!!!"

if __name__ == '__main__':
  app.run(port=9000)

