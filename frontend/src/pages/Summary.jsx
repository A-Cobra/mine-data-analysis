import React, { useEffect } from 'react';

const Summary = () => {
  useEffect(() => {
    const URL = '';
    console.log('Fetching data');
    // fetch(URL, { method: 'GET' })
    //   .then((data) => {
    //     console.log(data);
    //   })
    //   .catch((err) => {
    //     console.log(err);
    //   });
  }, []);
  return (
    <>
      <h2>Resumen</h2>
    </>
  );
};

export default Summary;
