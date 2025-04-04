import React, { useState } from "react";
import { MdContentCopy } from "react-icons/md";

const PasswordDisplay = () => {
  const [password, setPassword] = useState("");
  const placeholder = "Tap on 'Generate New'";

  const handleCopy = () => {
    if (password) {
      navigator.clipboard.writeText(password);
      alert("Password copied to clipboard!");
    }
  };
  return (
    <div className="mt-5 sm:mt-10 mx-3">
      <p className="text-[12px] sm:text-[18px] mt-8">Generated password: </p>
      <div className="flex justify-between items-center text-[12px] sm:text-3xl mt-5 sm:mt-8 gap-4 sm:px-12">
        <p className="bg-white w-full text-gray-500 rounded-3xl py-3 sm:py-6 pl-10">
          {password || placeholder}
        </p>
        <MdContentCopy
          className={`text-[20px] sm:text-4xl cursor-pointer ${
            password ? "text-blue-500" : "text-gray-400"
          }`}
          onClick={handleCopy}
        />
      </div>
      <button className="bg-green-600 w-full text-center text-[12px] sm:text-3xl text-white rounded-2xl  py-4 sm:py-10 mt-6 sm:mt-14">
        Generate New
      </button>
    </div>
  );
};

export default PasswordDisplay;
