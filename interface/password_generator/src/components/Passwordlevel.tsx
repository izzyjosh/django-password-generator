import React from "react";

const Passwordlevel = ({ length, options }) => {
  const selectedOptions = Object.values(options).filter(Boolean).length;

  let level = "weak";
  if (length > 8 && selectedOptions >= 2) level = "medium";
  if (length > 12 && selectedOptions >= 3) level = "strong";

  const getClasses = current =>
    `rounded-2xl py-3 px-6 sm:py-5 sm:px-12 ${
      level === current ? "bg-blue-500 text-white" : ""
    }`;
  return (
    <div className="font-serif">
      <p className="bg-blue-100 text-center text-[12px] sm:text-[18px] lg:text-[30px] font-bold py-3">
        Generate random password
      </p>
      <p className="text-[12px] sm:text-[18px] pl-3 mt-8">
        Password Security Level:
      </p>
      <div className="flex justify-between text-[12px] sm:text-2xl text-black  border-4 border-blue-500 rounded-3xl mx-3 mt-5">
        <div className={getClasses("weak")}>weak</div>
        <div className={getClasses("medium")}>medium</div>
        <div className={getClasses("strong")}>strong</div>
      </div>
    </div>
  );
};

export default Passwordlevel;
