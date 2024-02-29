def get_analysis_report(data_of_sensors):
    analysis = {}
    counter = {}
    for data_of_sensor in data_of_sensors:
        name_sensor = data_of_sensor["name_sensor"]

        if not name_sensor in analysis:
            analysis[name_sensor] = data_of_sensor
            counter[name_sensor] = 1
            continue
        analysis[name_sensor]["value"] += data_of_sensor["value"]
        counter[name_sensor] += 1

    for name_sensor, data_of_current_sensor in analysis.items():
        data_of_current_sensor["value"] /= counter[name_sensor]

    analysis_list = [value for value in analysis.values()]

    for analysis_field in analysis_list:
        analysis_field["average"] = analysis_field["value"]
        del analysis_field["value"]

    return analysis_list
