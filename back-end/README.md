# README

## Overview
This is the backend for our application, built with Django and Django Rest Framework. It provides a set of API endpoints for user authentication and for creating, retrieving, updating, and deleting posts and comments.

## API Endpoints

### User Authentication
- **`login/`** 
  - **Method:** POST
  - **Description:** Log in a user.
  - **Requirements:** `username` and `password` in the request body.
  - **Response:** Returns a token and user data if successful.

- **`signup/`** 
  - **Method:** POST
  - **Description:** Sign up a new user.
  - **Requirements:** `username`, `email`, and `password` in the request body.
  - **Response:** Returns a token and user data if successful.

- **`test_token/`**
  - **Method:** GET
  - **Description:** Test if a token is valid.
  - **Requirements:** Token in the Authorization header.

### Posts
- **`posts/`**
  - **Method:** GET
  - **Description:** Retrieve all posts.
  - **Requirements:** Token in the Authorization header.

- **`posts/`**
  - **Method:** POST
  - **Description:** Create a new post.
  - **Requirements:** Token in the Authorization header and post data in the request body.

- **`posts/<id>/`**
  - **Method:** GET
  - **Description:** Retrieve a specific post by its ID.
  - **Requirements:** Token in the Authorization header.

- **`posts/<id>/`**
  - **Method:** PUT
  - **Description:** Update a specific post by its ID.
  - **Requirements:** Token in the Authorization header and updated post data in the request body.

- **`posts/my_posts/`**
  - **Method:** GET
  - **Description:** Get all your posts.
  - **Requirements:** Token in the Authorization header and updated post data in the request body.

- **`posts/<id>/`**
  - **Method:** DELETE
  - **Description:** Delete a specific post by its ID.
  - **Requirements:** Token in the Authorization header.

### Comments
- **`comments/`**
  - **Method:** GET
  - **Description:** Retrieve all comments.
  - **Requirements:** Token in the Authorization header.

- **`comments/`**
  - **Method:** POST
  - **Description:** Create a new comment.
  - **Requirements:** Token in the Authorization header and comment data in the request body.

- **`comments/<id>/`**
  - **Method:** GET
  - **Description:** Retrieve a specific comment by its ID.
  - **Requirements:** Token in the Authorization header.

- **`comments/<id>/`**
  - **Method:** PUT
  - **Description:** Update a specific comment by its ID.
  - **Requirements:** Token in the Authorization header and updated comment data in the request body.

- **`/likes/`**
  - **Method:** GET, POST
  - **Description:** Post request to like and get request to get likes for a spicific post.
  - **Requirements:** Token in the Authorization header.
