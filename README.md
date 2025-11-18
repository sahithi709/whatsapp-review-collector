# WhatsApp Review Collector

A full-stack application that collects reviews via WhatsApp using Twilio integration. The backend is built with FastAPI and the frontend is a React application.

## Table of Contents

- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Configuration](#configuration)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)

## Project Structure

```
whatsapp-review-collector/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py           # FastAPI application entry point
│   │   ├── models.py         # Database models
│   │   ├── crud.py           # Database operations
│   │   ├── db.py             # Database configuration
│   │   ├── state.py          # Application state
│   │   └── twilio_webhook.py # Twilio webhook handler
│   ├── docker-compose.yml    # PostgreSQL container setup
│   ├── requirements.txt      # Python dependencies
│   └── .env                  # Environment variables (create this)
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── App.js
│   │   └── index.js
│   └── package.json
└── README.md
```

## Prerequisites

- **Python 3.8+** (for backend)
- **Node.js 14+** and **npm** (for frontend)
- **Docker** and **Docker Compose** (for PostgreSQL database)
- **Twilio Account** (for WhatsApp integration)
- **Git**

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/whatsapp-review-collector.git
cd whatsapp-review-collector
```

### 2. Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python -m venv venv
source venv/bin/activate
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the `backend` directory with the following variables:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/reviewsdb
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=+1234567890
```

### 3. Frontend Setup

Navigate to the frontend directory:

```bash
cd ../frontend
```

Install Node dependencies:

```bash
npm install
```

## Running the Project

### Step 1: Start the Database

From the `backend` directory, start PostgreSQL with Docker Compose:

```bash
docker-compose up -d
```

This will start a PostgreSQL database container on `localhost:5432`.

### Step 2: Start the Backend Server

From the `backend` directory (with virtual environment activated):

```bash
uvicorn app.main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`

View the interactive API documentation at `http://localhost:8000/docs`

### Step 3: Start the Frontend Server

In a new terminal, navigate to the `frontend` directory:

```bash
cd frontend
npm start
```

The React application will automatically open at `http://localhost:3000`

## Configuration

### Environment Variables

Create a `.env` file in the `backend` directory with:

- `DATABASE_URL`: PostgreSQL connection string
- `TWILIO_ACCOUNT_SID`: Your Twilio account SID
- `TWILIO_AUTH_TOKEN`: Your Twilio authentication token
- `TWILIO_PHONE_NUMBER`: Your Twilio WhatsApp phone number

### Twilio Setup

1. Sign up for a [Twilio account](https://www.twilio.com/console)
2. Enable WhatsApp in the Twilio console
3. Get your phone number and credentials
4. Update your `.env` file with these credentials
5. Set your webhook URL in Twilio to point to your backend API

## API Documentation

Once the backend server is running, visit `http://localhost:8000/docs` to view the interactive Swagger UI documentation for all available API endpoints.

## Stopping Services

### Stop the Frontend
- Press `Ctrl+C` in the terminal running `npm start`

### Stop the Backend
- Press `Ctrl+C` in the terminal running `uvicorn`

### Stop the Database
```bash
docker-compose down
```

## Development

### Backend Dependencies

- **FastAPI**: Modern web framework for building APIs
- **Uvicorn**: ASGI web server
- **SQLAlchemy**: ORM for database operations
- **asyncpg**: Async PostgreSQL driver
- **Pydantic**: Data validation
- **Twilio**: WhatsApp integration
- **python-dotenv**: Environment variable management

### Frontend Dependencies

- **React**: UI library
- **react-scripts**: Build and development tools

## Troubleshooting

- **Database Connection Error**: Ensure Docker is running and PostgreSQL container is up (`docker-compose ps`)
- **Port Already in Use**: Change the port in the uvicorn command or kill the process using the port
- **Missing Dependencies**: Re-run `pip install -r requirements.txt` or `npm install`

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues or questions, please open an issue on GitHub.
