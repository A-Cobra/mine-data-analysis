import React, { useState } from 'react';

const FileUploader = () => {
  const [file, setFile] = useState(null);
  function handleFileChange(event) {
    const newFile = event.target.files[0];
    console.log('newFile');
    console.log(newFile);
    setFile(newFile);
  }

  function handleFileUpload() {
    if (!file) {
      alert('Es necesario un archivo, seleccionelo por favor');
      return;
    }
    const body = new FormData();
    body.append('analysis-file', file);

    console.log('body');
    console.log(body);

    return;
    fetch('url', {
      method: 'POST',
      body,
    })
      .then((data) => {
        console.log(data);
        alert('Archivo subido adecuadamente');
      })
      .catch((err) => {
        console.log(err);
        alert('Hubo un error, por favor intente nuevamente');
      });
  }

  return (
    <>
      <input
        id="analysis-file"
        type="file"
        accept=".csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel"
        onChange={handleFileChange}
      />
      <button onClick={handleFileUpload}>Upload</button>
    </>
  );
};

export default FileUploader;
