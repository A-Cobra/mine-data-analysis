import React, { useEffect, useState } from 'react';
import SummaryDisplay from '../components/SummaryDisplay/SummaryDisplay';

const Summary = () => {
  function handleDateChange(event) {
    const dateValue = event.target.value;
    setDate(dateValue);
  }
  const [summaryData, setSummaryData] = useState(null);
  const [date, setDate] = useState('2023-04-17');

  useEffect(() => {
    const API_BASE_URL = 'http://127.0.0.1:5000';
    const URL = `${API_BASE_URL}/api/v1/list/${date}`;

    fetch(URL, { method: 'GET' })
      .then(async (response) => {
        const data = await response.json();
        setSummaryData(data);
      })
      .catch((err) => {
        console.log(err);
        alert('Hubo un problema, intenta nuevamente');
      });
  }, [date]);
  return (
    <>
      <label htmlFor="date">Seleccione una fecha</label>
      <input type="date" id="date" onChange={handleDateChange}></input>
      <h2>Resumen</h2>
      {summaryData && <SummaryDisplay summaryData={summaryData} />}
    </>
  );
};

export default Summary;
