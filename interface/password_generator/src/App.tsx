import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import Passwordlevel from "./components/Passwordlevel";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
        <div className="bg-gray-50 h-[1240px] w-[800px] mx-auto mt-[300px] rounded-md">
         <Passwordlevel />
         </div>
     
    </>
  );
}

export default App;
