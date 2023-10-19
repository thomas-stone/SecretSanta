import './App.css';
import { useState } from 'react';

function App() {
  const [number, setNumber] = useState(0);

  return (
    <div className="App">
      <header className="App-header">

        <h2>THE AMAZING COUNTER</h2>

        <p>{number}</p>

      <div>
        <button> Test API GET</button>
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
