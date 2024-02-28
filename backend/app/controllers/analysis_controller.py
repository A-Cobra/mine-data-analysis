from ..config import get_connection
from ..utils.db_helpers import save_measurement_details, save_summary_details


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


def get_analysis_by_date(date):
    connection = get_connection()
    cursor = connection.cursor()
    sql_query = "SELECT * FROM summary WHERE timestamp LIKE %s"
    cursor.execute(sql_query, (f"{date}%"))

    rows = cursor.fetchall()

    analysis = []

    # Iterate over the rows and create a dictionary object for each row
    for row in rows:
        obj = {
            "average": row[0],  # Replace with the appropriate column index
            "name_sensor": row[1],  # Replace with the appropriate column index
            "timestamp": str(row[2]),  # Replace with the appropriate column index
            "unit": row[3],  # Replace with the appropriate column index
        }
        analysis.append(obj)

    # Close the cursor and the database connection
    cursor.close()
    connection.close()

    return analysis
