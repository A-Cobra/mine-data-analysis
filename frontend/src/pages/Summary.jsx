import React, { useEffect, useState } from 'react';
import SummaryDisplay from '../components/SummaryDisplay/SummaryDisplay';

const Summary = () => {
  const [summaryData, setSummaryData] = useState(null);

  useEffect(() => {
    const API_BASE_URL = 'http://127.0.0.1:5000';
    const date = '2023-04-17';
    const URL = `${API_BASE_URL}/api/v1/list/${date}`;

    // console.log('Fetching data');
    fetch(URL, { method: 'GET' })
      .then(async (response) => {
        const data = await response.json();
        setSummaryData(data);
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);
  return (
    <>
      <h2>Resumen</h2>
      <pre>{summaryData && <SummaryDisplay summaryData={summaryData} />}</pre>
    </>
  );
};

export default Summary;
