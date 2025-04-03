import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import Passwordlevel from "./components/Passwordlevel";
import Form from "./components/Form";
import PasswordDisplay from "./components/PasswordDisplay";
import "./App.css";

function App() {
  return (
    <div className="bg-gray-50 h-[1240px] w-[800px] mx-auto mt-[300px] rounded-md">
      <Passwordlevel />
      <Form />
      <PasswordDisplay/>
    </div>
  );
}

export default App;
