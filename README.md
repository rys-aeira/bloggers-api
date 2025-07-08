# Blogger API

A simple RESTful API for managing blog posts, built with Flask and designed to run locally or in Docker.

## Features
- List all blog posts
- Create a new post
- Update an existing post
- Delete a post
- Data is stored in a local JSON file (`posts.json`)

## Endpoints

### List all posts
- **GET** `/posts`
- Returns a list of all blog posts.

### Create a new post
- **POST** `/posts`
- Request body (JSON): `{ "title": "Post Title", "content": "Post content" }`
- Returns the created post with an assigned `id`.

### Update a post
- **PUT** `/posts/<post_id>`
- Request body (JSON): `{ "title": "New Title", "content": "Updated content" }`
- Updates the post with the given `id`.

### Delete a post
- **DELETE** `/posts/<post_id>`
- Deletes the post with the given `id`.

### Home
- **GET** `/`
- Returns a welcome message.

## Running Locally

1. Install dependencies:
   ```bash
   pip install flask
   ```
2. Start the server:
   ```bash
   python app.py
   ```
3. Visit [http://localhost:8000](http://localhost:8000)

## Running with Docker

1. Build the Docker image:
   ```bash
   docker build -t blogger-api .
   ```
2. Run the container:
   ```bash
   docker run -p 8000:8000 blogger-api
   ```
3. Visit [http://localhost:8000](http://localhost:8000)

## Data Persistence
- All posts are stored in `posts.json` in the project directory.
- The file is created automatically if it does not exist.

## Example `posts.json`
```json
[
  {
    "id": 1,
    "title": "My First Post",
    "content": "This is my first blog post!"
  }
]
```

## License
MIT
