from ..config import get_connection


def save_measurement_details(measurement_details, cursor):
    sql_query = "INSERT INTO measurement_detail (name_sensor, value, unit, timestamp) VALUES (%s, %s, %s, %s)"
    for data_of_sensor in measurement_details:
        try:
            print("\n\nsaving data\n\n\n")
            # Extract the values from the dictionary
            name_sensor = data_of_sensor["name_sensor"]
            value = data_of_sensor["value"]
            unit = data_of_sensor["unit"]
            timestamp = data_of_sensor["timestamp"]

            print("before inserting into the table")

            # Execute the INSERT statement with the values as parameters
            cursor.execute(sql_query, (name_sensor, value, unit, timestamp))

            print("after inserting into the table")

        except Exception as e:
            # Handle the exception
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
            # Handle the exception
            print("An error occurred:", str(e))
            raise e


def save_measurements_and_summary(measurement_details, summary):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        print("saving the measurements")
        save_measurement_details(measurement_details, cursor)
        print("saved the measurements")
        print("saving the summary")
        save_summary_details(summary, cursor)
        print("saved the summary")
        # Commit the transaction
        connection.commit()
    except Exception as e:
        raise e
    finally:
        cursor.close
