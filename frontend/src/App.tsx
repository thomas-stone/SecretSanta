import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import './index.css';

import Landing from "./pages/Landing";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Landing />} />
      </Routes>
    </Router>
  );
}

export default App;

