import React, { useState } from 'react';
import CSVReader from 'react-csv-reader';
import { transformRawDataIntoObjectsArray } from '../utils/transform-raw-data-into-objects-array';

const FileUploader = () => {
  // const [file, setFile] = useState(null);
  const [measurementsData, setMeasurementsData] = useState(null);

  // function handleFileChange(event) {
  //   const newFile = event.target.files[0];
  //   console.log('newFile');
  //   console.log(newFile);
  //   setFile(newFile);
  // }

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

    const transformedData = transformRawDataIntoObjectsArray(measurementsData); // Returns an array of objects

    const API_BASE_URL = 'http://127.0.0.1:5000';
    const URL = `${API_BASE_URL}/api/v1/load`;
    const body = JSON.stringify(transformedData);

    fetch(URL, {
      method: 'POST',
      body,
      headers: {
        'Content-Type': 'application/json', // Set the Content-Type header
      },
    })
      .then((response) => {
        if (response.ok) {
          console.log(response);
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
      {/* <input
        id="analysis-file"
        type="file"
        accept=".csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel"
        onChange={handleFileChange}
      /> */}
      <button onClick={handleFileUpload}>Upload</button>
    </>
  );
};

export default FileUploader;
