import React from 'react';

function ConsultaSelector({ modo, onSelectConsulta }) {
  const consultas = Array.from({ length: modo === 'mongo' ? 16 : 12 }, (_, i) => i + 1);

  return (
    <div className="selector">
      <label>Selecciona una consulta:</label>
      <select onChange={(e) => onSelectConsulta(e.target.value)}>
        <option value="">-- Consulta --</option>
        {consultas.map((num) => (
          <option key={num} value={num}>Consulta {num}</option>
        ))}
      </select>
    </div>
  );
}

export default ConsultaSelector;
