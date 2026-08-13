import React from "react";
import EventCard from "../components/EventCard";

function Home({ onLogin, onRegister }) {
  return (
    <div>
      <h1>Gaming Event Ticket Platform</h1>

      <p>Welcome to Gaming Event Ticket Platform</p>

      <button onClick={onLogin}>Login</button>
      <button onClick={onRegister}>Register</button>

      <h2>Upcoming Events</h2>

      <EventCard onRegister={onRegister} />
    </div>
  );
}

export default Home;