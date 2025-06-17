import React, { useState } from 'react';
import './App.css';
import Navbar from './components/NavBar';
import ConsultaSelector from './components/ConsultaSelector';
import ResultViewer from './components/ResultViewer';
import axios from 'axios';

function App() {
  const [modo, setModo] = useState('mongo'); // mongo o neo4j
  const [consultaSeleccionada, setConsultaSeleccionada] = useState(null);
  const [resultado, setResultado] = useState(null);
  const [busqueda, setBusqueda] = useState('');

  const manejarConsulta = async (numero) => {
    setConsultaSeleccionada(numero);
    try {
      const res = await axios.get(`http://localhost:3000/api/${modo}/consulta${numero}`);
      setResultado(res.data);
    } catch (err) {
      setResultado({ error: 'Error al obtener datos' });
    }
  };

  const manejarBusqueda = async () => {
    try {
      const res = await axios.get(`http://localhost:3000/api/${modo}/buscar/${busqueda}`);
      setResultado(res.data);
      setConsultaSeleccionada(null);
    } catch (err) {
      setResultado({ error: 'Usuario no encontrado' });
    }
  };

  return (
    <div className="App">
      <Navbar setModo={setModo} busqueda={busqueda} setBusqueda={setBusqueda} buscar={manejarBusqueda} />
      <h2>{modo.toUpperCase()} - Consultas</h2>
      <ConsultaSelector modo={modo} onSelectConsulta={manejarConsulta} />
      <ResultViewer resultado={resultado} consulta={consultaSeleccionada} />
    </div>
  );
}

export default App;
