from ..config import get_connection


def save_measurement_details(measurement_details):
    connection = get_connection()
    cursor = connection.cursor()
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
            # Handle the exception
            print("An error occurred:", str(e))
            connection.rollback()
            cursor.close()
            raise e

    # Commit the transaction
    connection.commit()

    # Close the cursor and the database connection
    cursor.close()


def save_summary_details(summary):
    connection = get_connection()
    cursor = connection.cursor()
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
            # Handle the exception
            print("An error occurred:", str(e))
            connection.rollback()
            cursor.close()
            raise e

    # Commit the transaction
    connection.commit()

    # Close the cursor and the database connection
    cursor.close()


def save_measurements_and_summary(measurement_details, summary):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        pass
    except:
        pass
