
import React from "react";

function EventCard({ onRegister }) {
  return (
    <div>
      <h2>BGMI Championship</h2>
      <p>Date: 20 August 2026</p>
      <p>Location: Chennai</p>
      <p>Ticket Price: ₹299</p>

      <button onClick={onRegister}>Register</button>
    </div>
  );
}

export default EventCard;