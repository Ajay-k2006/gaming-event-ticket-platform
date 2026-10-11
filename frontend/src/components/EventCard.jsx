import React, { useState } from "react";

function EventCard() {
  const [loading, setLoading] = useState(false);
  const [paymentLoading, setPaymentLoading] = useState(false);
  const [registrationId, setRegistrationId] = useState(null);

  const handleRegister = async () => {
    setLoading(true);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/api/registrations/?user_id=5&ticket_id=1&quantity=1",
        { method: "POST" }
      );

      const data = await response.json();

      if (!response.ok) {
        alert(data.detail || "Booking failed!");
        return;
      }

      const id = data.registration?.id;

      if (!id) {
        alert("Registration ID not found!");
        console.log(data);
        return;
      }

      setRegistrationId(id);
      alert("Booking successful! Registration ID: " + id);
    } catch (error) {
      console.log(error);
      alert("Cannot connect to backend!");
    } finally {
      setLoading(false);
    }
  };

  const handlePayment = async () => {
    if (!registrationId) {
      alert("First book your ticket!");
      return;
    }

    setPaymentLoading(true);

    try {
      const url =
        "http://127.0.0.1:8000/api/payments/?registration_id=" +
        registrationId +
        "&amount=299&payment_method=UPI";

      const response = await fetch(url, { method: "POST" });
      const data = await response.json();

      if (!response.ok) {
        alert(data.detail || "Payment failed!");
        return;
      }

      alert("Payment record created! Status: " + data.payment.payment_status);
    } catch (error) {
      console.log(error);
      alert("Cannot connect to backend!");
    } finally {
      setPaymentLoading(false);
    }
  };

  return (
    <div>
      <h2>BGMI Championship</h2>
      <p>Date: 20 August 2026</p>
      <p>Location: Chennai</p>
      <p>Ticket Price: ₹299</p>

      <button onClick={handleRegister} disabled={loading}>
        {loading ? "Booking..." : "Register"}
      </button>

      <button
        onClick={handlePayment}
        disabled={!registrationId || paymentLoading}
      >
        {paymentLoading ? "Processing..." : "Create Payment Record"}
      </button>
    </div>
  );
}

export default EventCard;