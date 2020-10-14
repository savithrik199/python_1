 # python_task3 on dictionary

# 1.
dict={
    "april_batch":{
        "student":{
            "name":"mike",
            "marks":{
                "python":80,
                "maths":70
            }
        }
    }
}
print(dict["april_batch"]["student"]["name"])
#  output=mike

print(dict["april_batch"]["student"]["marks"]["python"])
#  output=80

dict["april_batch"]["student"]["name"]="Savithri"
print(dict)
#  output={'april_batch': {'student': {'name': 'Savithri', 'marks': {'python': 80, 'maths': 70}}}}

'''dict["AD"]=80
dict["ML"]=90
print(dict)'''

print(dict["april_batch"]["student"]["marks"])

dict["april_batch"]["student"]["marks"]["ML"]=80
dict["april_batch"]["student"]["marks"]["DL"]=80
print(dict["april_batch"]["student"]["marks"])
#  output={'python': 80, 'maths': 70, 'ML': 80, 'DL': 80}
print(dict)
#  output={'april_batch': {'student': {'name': 'Savithri', 'marks': {'python': 80, 'maths': 70, 'ML': 80, 'DL': 80}}}}



