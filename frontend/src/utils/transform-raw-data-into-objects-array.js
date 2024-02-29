export function transformRawDataIntoObjectsArray(measurementsData) {
  const objectsArray = [];
  for (let measurement of measurementsData) {
    let [name_sensor, value, unit, timestamp] = measurement;
    name_sensor = name_sensor.trim();
    value = parseInt(value.trim());
    unit = unit.trim();
    timestamp = timestamp.trim();
    objectsArray.push({
      name_sensor,
      value,
      unit,
      timestamp,
    });
  }

  return objectsArray;
}
