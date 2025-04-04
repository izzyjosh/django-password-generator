import { useState } from "react";
import Passwordlevel from "./components/Passwordlevel";
import Form from "./components/Form";
import PasswordDisplay from "./components/PasswordDisplay";
import "./App.css";

function App() {
  const [rangeValue, setRangeValue] = useState(6);
  const [options, setOptions] = useState({
    uppercase: false,
    lowercase: false,
    numbers: false,
    symbols: false
  });

  const handleToggle = key => {
    setOptions(prev => ({ ...prev, [key]: !prev[key] }));
  };
  const handleRangeChange = event => {
    const value = event.target.value;
    setRangeValue(value);
  };
  return (
    <div className="bg-gray-50 w-full max-w-[800px] mx-auto sm:mt-32 md:mt-40 lg:mt-[300px] rounded-md p-4">
      <Passwordlevel length={rangeValue} options={options} />
      <Form
        rangeValue={rangeValue}
        handleRangeChange={handleRangeChange}
        options={options}
        handleToggle={handleToggle}
      />
      <PasswordDisplay />
    </div>
  );
}

export default App;
