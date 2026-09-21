import React, { useState } from "react";

function Login({ onRegister, onHome }) {

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async (event) => {

    event.preventDefault();

    try {

      const response = await fetch(
        "http://127.0.0.1:8000/api/users/login",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            email: email,
            password: password
          })
        }
      );

      const data = await response.json();

      if (response.ok) {

        alert("Login successful!");

        console.log(data);

        onHome();

      } else {

        alert("Login failed!");

        console.log(data);

      }

    } catch (error) {

      console.log("Error:", error);

      alert("Cannot connect to backend!");

    }
  };

  return (
    <div>

      <h2>Login</h2>

      <form onSubmit={handleLogin}>

        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(event) => setEmail(event.target.value)}
        />

        <br />
        <br />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(event) => setPassword(event.target.value)}
        />

        <br />
        <br />

        <button type="submit">
          Login
        </button>

      </form>

      <br />

      <button onClick={onRegister}>
        Register
      </button>

      <br />
      <br />

      <button onClick={onHome}>
        Home
      </button>

    </div>
  );
}

export default Login;