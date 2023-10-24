import React from 'react'

const InputField = ({state, setState}) => {

  const handleInputChange = (event) => {
    const { value } = event.target;
    setState(value);
  };


  return (
    <div>
      <label>Name: </label>
      <input
        type="text"
        value={state}
        onChange={handleInputChange}
      />
    </div>
  );
}

export default InputField