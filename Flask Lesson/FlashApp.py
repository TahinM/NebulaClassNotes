from flask import Flask
app = Flask(__name__)

@app.route('/status')
def home():
    return {"status": "OK"}

@app.route('/square/<int:number>')
def square(number):
    return {"square": number ** 2}

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    if not data or 'message' not in data:
        return {"error": "No message provided"}, 400
    return {"echo": data['message']}

if __name__ == '__main__':
    app.run(debug=True)