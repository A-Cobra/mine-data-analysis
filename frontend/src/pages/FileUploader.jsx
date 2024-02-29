import React, { useState } from 'react';
import CSVReader from 'react-csv-reader';
import { transformRawDataIntoObjectsArray } from '../utils/transform-raw-data-into-objects-array';

const FileUploader = () => {
  const [measurementsData, setMeasurementsData] = useState(null);

  function handleFileLoaded(data, fileInfo, originalFile) {
    // A better error handling could be imposed
    if (!originalFile.name.match(/^.+\.csv$/)) {
      alert('Solo se permite archivos .csv');
      return;
    }
    setMeasurementsData(data);
  }

  function handleFileUpload() {
    if (!measurementsData) {
      alert('Es necesario un archivo, seleccionelo por favor');
      return;
    }

    const transformedData = transformRawDataIntoObjectsArray(measurementsData);

    const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;

    const API_BASE_URL = `${BACKEND_URL}:5000`;
    const URL = `${API_BASE_URL}/api/v1/load`;
    const body = JSON.stringify(transformedData);

    fetch(URL, {
      method: 'POST',
      body,
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((response) => {
        if (response.ok) {
          alert('Archivo subido adecuadamente');
        } else {
          throw new Error('Network response was not ok.');
        }
      })
      .catch((err) => {
        console.log(err);
        alert('Hubo un error, por favor intente nuevamente');
      });
  }

  return (
    <>
      <CSVReader onFileLoaded={handleFileLoaded} />
      <button onClick={handleFileUpload}>Upload</button>
    </>
  );
};

export default FileUploader;
