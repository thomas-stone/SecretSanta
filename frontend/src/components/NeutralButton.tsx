import React from "react";

interface Props {
    children: React.ReactNode
    onClick: () => void;
}

const NeutralButton = ({children, onClick, ...attributes}: Props) => {
  return (
    <button
    className="w-fit bg-neutral-100 hover:bg-slate-200 font-bold py-2 px-4 rounded"
    onClick={onClick}
    {...attributes}
  >
      {children}
  </button>
  )
}

export default NeutralButton