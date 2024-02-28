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
