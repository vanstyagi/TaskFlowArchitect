from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "🔥 TaskFlow Architect is LIVE! 🔥"

if __name__ == '__main__':
    app.run(debug=True)
