import "./App.css";
import { useState } from "react";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Home from "./pages/Home";

function App() {
  const [page, setPage] = useState("home");

  return (
    <div>
      {page === "home" && (
        <Home
          onLogin={() => setPage("login")}
          onRegister={() => setPage("register")}
        />
      )}

      {page === "login" && (
        <Login
          onRegister={() => setPage("register")}
          onHome={() => setPage("home")}
        />
      )}

      {page === "register" && (
        <Register
          onLogin={() => setPage("login")}
          onHome={() => setPage("home")}
        />
      )}
    </div>
  );
}

export default App;