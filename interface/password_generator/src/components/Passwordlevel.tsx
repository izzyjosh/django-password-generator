import React from "react";

const Passwordlevel = () => {
  return (
    <div className="font-serif">
      <p className="bg-blue-100 text-center text-3xl font-bold py-3">
        Generate random password
      </p>
      <p className="text-2xl pl-3 mt-8">Password Security Level:</p>
      <div className="flex justify-between text-3xl text-black  border-4 border-blue-500 rounded-3xl mx-3 mt-5">
        <div className="bg-blue-500 text-white rounded-2xl py-5 px-16">
          weak
        </div>
        <div className="rounded-2xl py-5 px-16">medium</div>
        <div className="rounded-2xl py-5 px-16">strong</div>
      </div>
    </div>
  );
};

export default Passwordlevel;
