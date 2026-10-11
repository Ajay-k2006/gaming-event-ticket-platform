# Gaming Event Ticket Platform

## Project Overview
A web application for users to view gaming events, register, book tickets, and create payment records.

## Technologies Used
- Frontend: React.js
- Backend: Python FastAPI
- Database: SQLite
- API Testing: Swagger UI

## Modules
1. User Registration
2. User Login
3. Event Management
4. Ticket Management
5. Ticket Registration
6. Payment Management

## Project Structure
- `frontend/` – React user interface
- `backend/app/api/` – API endpoints
- `backend/app/models/` – Database models
- `backend/app/schemas/` – Data schemas
- `backend/gaming_event.db` – SQLite database

## How to Run

### Backend
Open a terminal in the `backend` folder:

```bash
python -m uvicorn app.main:app --reload --port 8000
```

API documentation: http://127.0.0.1:8000/docs

### Frontend
Open another terminal in the `frontend` folder:

```bash
npm start
```

Frontend URL: http://localhost:3000

## Database
SQLite stores users, events, tickets, registrations, and payment records.

## Testing
- Registration and login
- Event and ticket APIs
- Ticket booking and quantity validation
- Payment record creation
- Database verification

## Limitation
The payment module currently creates payment records. A real payment gateway has not been integrated.
