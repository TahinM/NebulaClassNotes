from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "Welcome to the Blog API!"}

blog_posts = {}
current_id = 1

#Get endpoint
@app.route('/post', methods = ['GET'])
def get_posts():
    return {'posts': blog_posts}

#Post endpoint
@app.route('/post', methods = ['POST'])
def create_post():
    global current_id
    data = request.get_json()
    blog_posts[current_id] = data
    current_id += 1
    return {'post': blog_posts[current_id -1]}

#GET specific ID
@app.route('/posts/<int:id>', methods = ['GET'])
def get_postID(id):
    return {'post': blog_posts[id]}

#Update
@app.route('/posts/<int:id>', methods = ['PUT'])
def put_post(id):
    data = request.get_json()
    blog_posts[id] = data
    return {'post': blog_posts[id]}

#Delete
@app.route('/posts/<int:id>', methods = ['DELETE'])
def delete_post(id):
    del blog_posts[id]
    return {'Message': 'Deleted Successfully!'}


if __name__ == '__main__':
    app.run(debug=True)