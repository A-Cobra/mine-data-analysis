from ..config import get_connection


def save_measurement_details(data_of_sensors):
    connection = get_connection()
    cursor = connection.cursor()
    sql_query = "INSERT INTO measurement_detail (name_sensor, value, unit, timestamp) VALUES (%s, %s, %s, %s)"
    for data_of_sensor in data_of_sensors:
        try:
            # Extract the values from the dictionary
            name_sensor = data_of_sensor["name_sensor"]
            value = data_of_sensor["value"]
            unit = data_of_sensor["unit"]
            timestamp = data_of_sensor["timestamp"]

            # Execute the INSERT statement with the values as parameters
            cursor.execute(sql_query, (name_sensor, value, unit, timestamp))

        except Exception as e:
            # Handle the exception
            print("An error occurred:", str(e))
            connection.rollback()
            cursor.close()
            raise e

    # Commit the transaction
    connection.commit()

    # Close the cursor and the database connection
    cursor.close()
