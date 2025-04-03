import React, { useState } from "react";
import { RxLetterCaseUppercase, RxLetterCaseLowercase } from "react-icons/rx";
import { Bs123 } from "react-icons/bs";
import { RiEqualizer3Line } from "react-icons/ri";

const Form = () => {
  const [rangeValue, setRangeValue] = useState(6);

  const handleRangeChange = event => {
    const value = event.target.value;
    setRangeValue(value);
  };
  return (
    <div className="mt-10 mx-3">
      <p className="text-2xl">
        Password length: <span>{rangeValue}</span>
      </p>
      <input
        type="range"
        min="4"
        max="100"
        step="1"
        value={rangeValue}
        onChange={handleRangeChange}
        className="w-full h-4 bg-gray-300 rounded-lg appearance-none cursor-pointer focus:outline-none accent-blue-500 mt-8"
        style={{
          background: `linear-gradient(to right, #3b82f6 ${
            ((rangeValue - 4) / (100 - 4)) * 100
          }%, #e5e7eb ${((rangeValue - 4) / (100 - 4)) * 100}%)`
        }}
      />
      <div className="text-4xl mx-3 mt-10">
        <Options name="Uppercase letters" icon_name={RxLetterCaseUppercase} />
        <Options name="Lowercase letters" icon_name={RxLetterCaseLowercase} />
        <Options name="Numbers" icon_name={Bs123} />
        <Options name="Symbols" icon_name={RiEqualizer3Line} />
      </div>
    </div>
  );
};

const Options = ({ name, icon_name: Icon }) => {
  return (
    <div className="flex justify-between items-center py-6">
      <div className="flex justify-center gap-12 items-center">
        <Icon className="text-blue-500 text-4xl" />
        <p>{name}</p>
      </div>
      <ToggleSwitch />
    </div>
  );
};

const ToggleSwitch = () => {
  const [isOn, setIsOn] = useState(false);

  return (
    <div
      className={`w-12 h-6 flex items-center rounded-full p-1 cursor-pointer transition-all ${
        isOn ? "bg-blue-500" : "bg-gray-400"
      }`}
      onClick={() => setIsOn(!isOn)}
    >
      <div
        className={`w-4 h-4 bg-white rounded-full shadow-md transform transition-all ${
          isOn ? "translate-x-6" : "translate-x-0"
        }`}
      />
    </div>
  );
};
export default Form;
