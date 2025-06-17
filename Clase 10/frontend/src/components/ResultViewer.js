import React from 'react';

function ResultViewer({ resultado, consulta }) {
  if (!resultado) return null;

  return (
    <div className="resultado">
      <h3>{consulta ? `Resultado Consulta ${consulta}` : 'Resultado de Búsqueda'}</h3>
      <pre>{JSON.stringify(resultado, null, 2)}</pre>
    </div>
  );
}

export default ResultViewer;
