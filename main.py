from flask import Flask

# Creating app
app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)