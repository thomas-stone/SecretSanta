import './App.css';
import { useState } from 'react';
import GetButton from './components/GetButton';

function App() {
  const [number, setNumber] = useState(0);

  return (
    <div className="App">
      <header className="App-header">

        <h2>THE AMAZING COUNTER</h2>
        
        <p>{number}</p>

      <div>
        <GetButton name={"TEST BUTTON"} urlPath={`/user/${}`}></GetButton>
        <button> Test API POST</button>
        <button> Test API</button>
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
