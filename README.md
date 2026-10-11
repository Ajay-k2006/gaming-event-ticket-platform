# Gaming Event Ticket Platform

## Project Overview
The Gaming Event Ticket Platform is a web application that allows users to register, log in, view gaming events, book tickets, and create payment records.

## Technologies Used
- Frontend: React.js
- Backend: Python FastAPI
- Database: SQLite
- API Testing: Swagger UI

## Features
1. User Registration
2. User Login
3. Event Management
4. Ticket Management
5. Ticket Booking
6. Payment Record Management

## Project Structure
- `backend/` - FastAPI backend and SQLite database
- `frontend/` - React frontend
- `docs/` - Project diagrams and documentation

## How to Run

### 1. Start the Backend
Open a terminal in the project root and run:

```bash
cd backend
python -m uvicorn app.main:app --reload --port 8000
```

Backend API: http://127.0.0.1:8000

Swagger documentation: http://127.0.0.1:8000/docs

### 2. Start the Frontend
Open another terminal and run:

```bash
cd frontend
npm start
```

Frontend: http://localhost:3000

## Testing
- User registration and login tested
- Event and ticket APIs tested
- Ticket booking verified in SQLite
- Payment record creation verified in SQLite
- Backend health endpoint tested

## Limitation
The payment module creates payment records only. A real payment gateway has not been integrated.

## Database
The application uses SQLite to store users, events, tickets, registrations, and payment records.

## Future Enhancements
- Integrate a real payment gateway
- Improve user authentication and authorization
- Add event search and filtering
- Display booking history and payment status
