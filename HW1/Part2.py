import os
import json
import pydicom

path = "Data/"
folder_list = os.listdir(path)
folder_list.sort()

# Loading Files
for folder in folder_list:
    print("Processing : " + folder)
    folder_path = path + folder + "/"
    filename_list = os.listdir(folder_path)
    totaldata = dict()

    jsonFileName = folder + ".json"
    # print(jsonFileName)
    jsonFile = open(jsonFileName, "w")
    jStr = "{"
    firstData = 0
    for filename in filename_list:
        if firstData != 0:
            jStr += ", "
        data = dict()
        
        # Read DICOM
        image = pydicom.dcmread(folder_path + filename)
        # print(image.get_item)       # Show all item in dicom

        # get tag and data
        jStr += "\""+filename+"\":{"
        jStr += "\"PatientID\": "+"\""+image.PatientID+"\", "
        jStr += "\"ImageType\": "+"\""+str(image.ImageType)+"\", "
        jStr += "\"Modality\": "+"\""+image.Modality+"\", "
        jStr += "\"BodyPartExamined\": "+"\""+image.BodyPartExamined+"\", "
        jStr += "\"ContentDate\": "+"\""+image.ContentDate+"\", "
        jStr += "\"StudyDescription\": "+"\""+image.StudyDescription+"\", "
        jStr += "\"SeriesDescription\": "+"\""+image.SeriesDescription+"\", "
        jStr += "\"ImagePositionPatient\": "+"\""+str(image.ImagePositionPatient)+"\", "
        jStr += "\"ImageOrientationPatient\": "+"\""+str(image.ImageOrientationPatient)+"\""
        jStr += "}"
    
        firstData = 1
    jStr += "}"
    # print(jStr)
    jsonFile.writelines(jStr)
    jsonFile.close()

print("===== Finished ! =====")