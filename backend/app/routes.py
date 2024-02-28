from flask import Blueprint, jsonify, request
from app.utils.get_analysis_report import get_analysis_report
from app.controllers.analysis_controller import (
    save_measurements_and_summary,
    get_analysis_by_date,
)
import copy
import re

main_bp = Blueprint("main", __name__)


@main_bp.route("/api/v1/load", methods=["POST"])
def load_data():
    measurement_details = request.get_json()
    print("Loading")

    try:
        # save_measurement_details(data)
        summary = get_analysis_report(copy.deepcopy(measurement_details))
        print("summary")

        print("\\\n\n\n\nmeasurement_details")
        print(measurement_details)
        print("\n\n\n\n")
        save_measurements_and_summary(measurement_details, summary)

        response = jsonify({"msg": " Success!"})
        response.status_code = 201
        return response
    except Exception as e:
        response = jsonify({"msg": " Error in the server!"})
        response.status_code = 500
        # There could be better error handling such as 400 checking the body of the request
        print()
        print()
        print()
        print(e)
        return response


@main_bp.route("/api/v1/list/<date>", methods=["GET"])
def retrieve_data(date):
    if not re.match("^\d{4}\-\d{2}\-\d{2}$", date):
        response = jsonify(
            {"msg": "Bad request, the date has to have a format of 'YYYY/MM/DD'"}
        )
        response.status_code = 400
        return response

    analysis = get_analysis_by_date(date)

    response = jsonify(analysis)

    response.status_code = 200
    return response
