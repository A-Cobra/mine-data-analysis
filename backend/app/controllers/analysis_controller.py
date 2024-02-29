from ..config import get_connection
from ..utils.db_helpers import save_measurement_details, save_summary_details


def save_measurements_and_summary(measurement_details, summary):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        save_measurement_details(measurement_details, cursor)
        save_summary_details(summary, cursor)
        connection.commit()
    except Exception as e:
        raise e
    finally:
        cursor.close
        connection.close()


def get_analysis_by_date(date):
    connection = get_connection()
    cursor = connection.cursor()
    sql_query = "SELECT * FROM summary WHERE timestamp LIKE %s"
    cursor.execute(sql_query, (f"{date}%"))

    rows = cursor.fetchall()

    analysis = []

    for row in rows:
        obj = {
            "average": row[0],
            "name_sensor": row[1],
            "timestamp": str(row[2]),
            "unit": row[3],
        }
        analysis.append(obj)

    cursor.close()
    connection.close()

    return analysis
