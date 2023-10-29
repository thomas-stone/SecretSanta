import React from "react";

interface Props {
  className?: string
  children: JSX.Element[] | JSX.Element | string;
  onClick: ()=> void
}

const SolidButton = ({children, onClick, className, ...attributes}: Props) => {
  return (
    <button
      className={`w-fit bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded ${className}`}
      onClick={onClick}
      {...attributes}
    >
        {children}
    </button>
  );
}

export default SolidButton