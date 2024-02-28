import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import FileUploader from './pages/FileUploader';
import Summary from './pages/Summary';

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path="/carga" element={<FileUploader />} />
          <Route path="/resumen" element={<Summary />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
