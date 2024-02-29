import React from 'react';
import PropTypes from 'prop-types';
import style from './SummaryDisplay.module.css';

const SummaryDisplay = ({ summaryData }) => {
  return (
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
  );
};

SummaryDisplay.propTypes = {
  summaryData: PropTypes.array.isRequired,
};

export default SummaryDisplay;
