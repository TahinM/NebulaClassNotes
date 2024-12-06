from flask import Flask, request, abort
app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "Welcome to Flask Backend!"}

@app.route('/hello')
def hello():
    return {"message": "Hello, World!"}

@app.route('/user/<username>')
def greet_user(username):
    return {"message": f"Hello, {username}!"}

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    return {"received": data}

@app.errorhandler(404)
def not_found(error):
    return {"error": "Resource not found"}, 404

@app.errorhandler(500)
def server_error(error):
    return {"error": "Server error"}, 500

if __name__ == '__main__':
       app.run(debug=True)