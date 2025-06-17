import React from 'react';
import './Navbar.css';

function Navbar({ setModo, busqueda, setBusqueda, buscar }) {
  return (
    <nav className="navbar">
      <button onClick={() => setModo('mongo')}>Mongo</button>
      <button onClick={() => setModo('neo4j')}>Neo4j</button>
      <input
        type="text"
        value={busqueda}
        onChange={(e) => setBusqueda(e.target.value)}
        placeholder="Buscar estudiante"
      />
      <button onClick={buscar}>Buscar</button>
    </nav>
  );
}

export default Navbar;
