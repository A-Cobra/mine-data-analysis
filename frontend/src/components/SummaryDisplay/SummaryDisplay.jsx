import React from 'react';
import PropTypes from 'prop-types';
import style from './SummaryDisplay.module.css';

const SummaryDisplay = ({ summaryData }) => {
  return summaryData.length > 0 ? (
    <>
      <div className={`${style.cards_container}`}>
        {summaryData.map((summaryRecord, index) => {
          return (
            <div className={`${style.card}`} key={index}>
              <h2>Nombre de sensor: {summaryRecord.name_sensor}</h2>
              <h3>
                Promedio: {summaryRecord.average + ' ' + summaryRecord.unit}
              </h3>
              <h3>Fecha: {summaryRecord.timestamp}</h3>
            </div>
          );
        })}
      </div>
      <div
        style={{
          marginTop: '30px',
          display: 'grid',
          gap: '20px',
        }}
      >
        <h2>Resumen en tabla</h2>
        <table>
          <thead>
            <tr>
              <th>Sensor</th>
              <th>Valor Promedio</th>
              <th>Unidad</th>
              <th>Marca de Tiempo</th>
            </tr>
          </thead>
          <tbody>
            {summaryData.map((summaryRecord, index) => {
              return (
                <tr key={index}>
                  <td>{summaryRecord.name_sensor}</td>
                  <td>{summaryRecord.average}</td>
                  <td>{summaryRecord.unit}</td>
                  <td>{new Date(summaryRecord.timestamp).toISOString()}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </>
  ) : (
    <h2 className="error">
      No hay registros para dicha fecha, por favor elija otra
    </h2>
  );
};

SummaryDisplay.propTypes = {
  summaryData: PropTypes.array.isRequired,
};

export default SummaryDisplay;
