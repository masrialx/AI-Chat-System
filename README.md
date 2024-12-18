# AI Chat System with Django REST API

This project implements a simple AI-powered chat system using Django and Django REST Framework (DRF). The system includes APIs for user registration, login, chatting with an AI, and checking token balances.

## Features

1. **User Registration**: Allows users to register with a unique username and password. Each user is assigned 4000 tokens upon successful registration.
2. **User Login**: Allows users to log in with their username and password to receive an authentication token for further interactions.
3. **Chatting with AI**: Users can send messages to an AI-powered chatbot, which responds with a dummy value. Each message deducts 100 tokens from the user's account.
4. **Token Balance**: Users can check their remaining tokens via an authenticated API request.

## Requirements

- Python 3.x
- Django 3.x+
- Django REST Framework
- SQLite (default database)

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-chat-system.git
cd ai-chat-system
```

### 2. Install dependencies

Make sure you have `pip` installed. Run the following command to install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Setup the Database

Apply the migrations to create the necessary database tables:

```bash
python manage.py migrate
```

### 4. Run the Development Server

To run the Django development server, use the following command:

```bash
python manage.py runserver
```

The server should now be running at `http://localhost:8000/`.

## API Endpoints

### 1. **User Registration**

- **URL**: `/register/`
- **Method**: `POST`
- **Request Body**:

```json
{
    "username": "john_doe",
    "password": "password123"
}
```

- **Response**:

```json
{
    "message": "User registered successfully."
}
```

### 2. **User Login**

- **URL**: `/login/`
- **Method**: `POST`
- **Request Body**:

```json
{
    "username": "john_doe",
    "password": "password123"
}
```

- **Response**:

```json
{
    "token": "randomlyGeneratedToken123"
}
```

### 3. **Chat with AI**

- **URL**: `/chat/`
- **Method**: `POST`
- **Headers**:

```bash
Authorization: randomlyGeneratedToken123
```

- **Request Body**:

```json
{
    "message": "Hello, AI!"
}
```

- **Response**:

```json
{
    "user": 1,
    "message": "Hello, AI!",
    "response": "AI response",
    "timestamp": "2024-12-18T12:34:56Z"
}
```

### 4. **Token Balance**

- **URL**: `/balance/`
- **Method**: `GET`
- **Headers**:

```bash
Authorization: randomlyGeneratedToken123
```

- **Response**:

```json
{
    "tokens": 3900
}
```

## Task Breakdown

### Task 1: User Registration API

The `/register/` endpoint allows users to register with a unique username and password. Upon successful registration, a user is created with an initial token balance of 4000.

### Task 2: User Login API

The `/login/` endpoint allows users to log in with their credentials. A successful login returns a random authentication token, which is used for subsequent API calls.

### Task 3: Chat API

The `/chat/` endpoint allows authenticated users to send messages to the AI chatbot. Each message deducts 100 tokens from the user's account. A dummy AI response is returned, and the chat is saved in the database.

### Task 4: Token Balance API

The `/balance/` endpoint allows users to check their current token balance by sending an authenticated request with their token.

## Troubleshooting

- **Invalid token**: Ensure that the token is passed correctly in the `Authorization` header.
- **Insufficient tokens**: If a user tries to send a message without enough tokens, they will receive an error response.
- **Database issues**: Make sure you've run the migrations using `python manage.py migrate`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

### Key Points:
- **Setup Instructions**: It includes all the necessary steps for setting up the project, installing dependencies, running migrations, and starting the development server.
- **API Documentation**: Each API endpoint is documented with the URL, method, request body, and response.
- **Task Breakdown**: A summary of each task is provided for clarity.

### Next Steps:
1. Replace the placeholder GitHub URL in the **Clone the repository** section.
2. Make sure the actual `requirements.txt` file is included with the necessary dependencies (e.g., `Django`, `djangorestframework`).
3. Update the `Authorization` token handling in the `ChatView` and `TokenBalanceView` if you plan to implement more sophisticated authentication (e.g., JWT).