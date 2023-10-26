interface State {
    name: string
    email: string
}

interface Props {
    state: State
    setState: Function
}

const InputField = ({state, setState}: Props) => {

  return (
    <div>
        <h1>Enter Name: </h1>
        <input
            className="border-b-2 border-black"
            value={state.name} // ...force the input's value to match the state variable...
            onChange={e => setState({...state, name: e.target.value})} // ... and update the state variable on any edits!
        />
    </div>
  )
}

export default InputField