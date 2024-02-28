from flask import Blueprint, jsonify, request
from app.utils.get_analysis_report import get_analysis_report
from app.controllers.analysis_controller import save_measurements_and_summary
import copy

main_bp = Blueprint("main", __name__)


@main_bp.route("/api/v1/load", methods=["POST"])
def home():
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


@main_bp.route("/api/v1/list", methods=["GET"])
def about():
    return jsonify({"message": "This is a list"})
