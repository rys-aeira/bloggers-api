# main application code 
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# load posts from a JSON file
def load_posts():
    try:
        with open("posts.json", "r") as file:
            return json.load(file)
    except:
        return []

# Save posts to a JSON file
def save_posts(posts):
    with open("posts.json", "w") as file:
        json.dump(posts, file)

# Get/posts - list all posts
@app.route('/posts', methods=['GET'])
def get_posts():
    posts = load_posts()
    return jsonify(posts)

# create a new post
@app.route('/posts', methods=['POST'])
def create_post():
    new_post = request.get_json()
    posts = load_posts()
    new_post['id'] = len(posts) + 1
    posts.append(new_post)
    save_posts(posts)
    return jsonify(new_post), 201

# Update a Post
@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    updated_data = request.get_json()
    posts = load_posts()
    for post in posts:
        if post['id'] == post_id:
            post.update(updated_data)
            save_posts(posts)
            return jsonify(post)
    return jsonify({'error': 'Post not found'}), 404

# Delete a Post
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    posts = load_posts()
    posts = [post for post in posts if post['id'] != post_id]
    save_posts(posts)
    return jsonify({'message': 'Post deleted'})

# Add homepage route 
@app.route('/')
def home():
    return "Welcome to the Blog API. Try /posts"

# Run the application
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
