def get_analysis_report (data_of_sensors):
  print(data_of_sensors)
  analysis = {}
  counter = {}
  for data_of_sensor in data_of_sensors:
    name_sensor = data_of_sensor['name_sensor']
    isWithinAnalysis = name_sensor in analysis.keys()
    # print()
    # print(name_sensor)
    # print(data_of_sensor)
    print()
    # print(name_sensor in analysis.keys())
    if not name_sensor in analysis:
      print(f'No se encontro de momento {name_sensor}')
      analysis[name_sensor] = data_of_sensor
      counter[name_sensor] = 1
      continue
    analysis_item = analysis[name_sensor]
    print(analysis_item)
    analysis[name_sensor]['value'] += data_of_sensor['value']
    counter[name_sensor] += 1
    print(counter)
  
  for name_sensor, data_of_current_sensor in analysis.items():
    data_of_current_sensor['value'] /= counter[name_sensor]

  print()
  print()
  print()
  # print('analysis')
  # print(analysis)

  analysis_list = [value for value in analysis.values()]
  
  for analysis_field in analysis_list:
    analysis_field['average']=analysis_field['value']
    del analysis_field['value']
  
  print('analysis_list')
  print(analysis_list)
  return analysis_list
# [value for value in analysis.values()]