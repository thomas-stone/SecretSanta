import './App.css';
import { useState } from 'react';
import GetButton from './components/GetButton';
import InputField from './components/InputField';

function App() {
  const [number, setNumber] = useState(0);
  const [name, setState] = useState("");

  return (
    <div className="App">
      <header className="App-header">

        <h2>THE AMAZING COUNTER</h2>

        <div>
          <InputField state={name} setState={setState}></InputField>
        </div>
        
        <p>{number}</p>

      <div>
        <GetButton name={`GET /users/${name}`} urlPath={`/user/${name}`}></GetButton>
      </div>

      <div>
        <button onClick={()=>setNumber(number+1)}> Count Up</button>
        <button onClick={()=>setNumber(number-1)}> Count Down</button>
      </div>

      
      </header>
    </div>
  );
}





export default App;
