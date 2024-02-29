def save_measurement_details(measurement_details, cursor):
    sql_query = "INSERT INTO measurement_detail (name_sensor, value, unit, timestamp) VALUES (%s, %s, %s, %s)"
    for data_of_sensor in measurement_details:
        try:
            # Extract the values from the dictionary
            name_sensor = data_of_sensor["name_sensor"]
            value = data_of_sensor["value"]
            unit = data_of_sensor["unit"]
            timestamp = data_of_sensor["timestamp"]

            # Execute the INSERT statement with the values as parameters
            cursor.execute(sql_query, (name_sensor, value, unit, timestamp))

        except Exception as e:
            print("An error occurred:", str(e))
            raise e


def save_summary_details(summary, cursor):
    sql_query = "INSERT INTO summary (name_sensor, average, unit, timestamp) VALUES (%s, %s, %s, %s)"
    for data_of_sensor in summary:
        try:
            # Extract the values from the dictionary
            name_sensor = data_of_sensor["name_sensor"]
            average = data_of_sensor["average"]
            unit = data_of_sensor["unit"]
            timestamp = data_of_sensor["timestamp"]

            # Execute the INSERT statement with the values as parameters
            cursor.execute(sql_query, (name_sensor, average, unit, timestamp))

        except Exception as e:
            print("An error occurred:", str(e))
            raise e
