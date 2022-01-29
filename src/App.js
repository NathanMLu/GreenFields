import "./App.css";
import React, { useState, useEffect } from "react";
import Navbar from "./components/Navbar/Navbar";
import DashBoard from "./components/Scores/DashBoard";

function App() {
  const [data, setData] = useState({ name: null });
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("/api");
        if (response.ok) {
          const info = await response.json();
          setData(info);
          console.log(info);
          return info;
        }
      } catch (error) {
        return error;
      }
    };
    fetchData();
  }, [setData]);

  return (
    <React.Fragment>
      <header>
        <Navbar />
      </header>

      <DashBoard />
    </React.Fragment>
  );
}

export default App;
