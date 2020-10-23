import json
import re
with open('test-payload.json') as json_file:
    data = json.load(json_file)
    serialNumber = data["serialNumber"]
    dataCenter = data["vdcLocation"]
    splittedSerialNumber = serialNumber.split("-") # returns splitted list
    firstPart = splittedSerialNumber[0] # accessing the first part of the splitted list
    splittedDataCenter = dataCenter.split("-")
    lastPart = splittedDataCenter[1]
    #dcVar = 
    if re.search(r'\(SDC\)$', dataCenter):
        print("SDC")
    else: 
        if re.search(r'\(ADC\)$', dataCenter):
            print("ADC")

#print(serialNumber)
#print(splittedSerialNumber)
print(firstPart)
#print(splittedDataCenter)
#print(lastPart)
