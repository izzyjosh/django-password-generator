import React, { useState } from "react";
import Passwordlevel from "./Passwordlevel";
import { RxLetterCaseUppercase, RxLetterCaseLowercase } from "react-icons/rx";
import { Bs123 } from "react-icons/bs";
import { RiEqualizer3Line } from "react-icons/ri";

const Form = ({rangeValue, handleRangeChange, options, handleToggle}) => {
  return (
    <div className="mt-10 mx-3">
      <p className="text-[12px] sm:text-[18px] mt-8">
        Password length: <span>{rangeValue}</span>
      </p>
      <input
        type="range"
        min="4"
        max="100"
        step="1"
        value={rangeValue}
        onChange={handleRangeChange}
        className="w-full h-2 sm:h-4 bg-gray-300 rounded-lg appearance-none cursor-pointer focus:outline-none accent-blue-500 mt-8"
        style={{
          background: `linear-gradient(to right, #3b82f6 ${
            ((rangeValue - 4) / (100 - 4)) * 100
          }%, #e5e7eb ${((rangeValue - 4) / (100 - 4)) * 100}%)`
        }}
      />
      <div className="text-[12px] sm:text-3xl mx-3 mt-5 sm:mt-10">
        <Options
          name="Uppercase letters"
          icon_name={RxLetterCaseUppercase}
          isOn={options.uppercase}
          toggle={() => handleToggle("uppercase")}
        />
        <Options
          name="Lowercase letters"
          icon_name={RxLetterCaseLowercase}
          isOn={options.lowercase}
          toggle={() => handleToggle("lowercase")}
        />
        <Options
          name="Numbers"
          icon_name={Bs123}
          isOn={options.numbers}
          toggle={() => handleToggle("numbers")}
        />
        <Options
          name="Symbols"
          icon_name={RiEqualizer3Line}
          isOn={options.symbols}
          toggle={() => handleToggle("symbols")}
        />
      </div>
    </div>
  );
};

const Options = ({ name, icon_name: Icon, isOn, toggle }) => {
  return (
    <div className="flex justify-between items-center py-3 sm:py-6">
      <div className="flex justify-center gap-3 sm:gap-10 items-center">
        <Icon className="text-blue-500 text-[16px] sm:text-4xl" />
        <p>{name}</p>
      </div>
      <ToggleSwitch isOn={isOn} toggle={toggle} />
    </div>
  );
};

const ToggleSwitch = ({ isOn, toggle }) => {
  return (
    <div
      className={`w-8 sm:w-12 h-4 sm:h-6 flex items-center rounded-full p-1 cursor-pointer transition-all ${
        isOn ? "bg-blue-500" : "bg-gray-400"
      }`}
      onClick={toggle}
    >
      <div
        className={`w-2 sm:w-4 h-2 sm:h-4 bg-white rounded-full shadow-md transform transition-all ${
          isOn ? "translate-x-4 sm:translate-x-6" : "translate-x-0"
        }`}
      />
    </div>
  );
};
export default Form;
