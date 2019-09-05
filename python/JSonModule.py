import json

employee_data='''
{
"people" :[
{
"name":"Antonio",
"email":["ag@gmail.com","gg@gmail.com"],
"married":false
},
{
"name":"Juan",
"email":["adsg@gmail.com","gdddg@gmail.com"],
"married":true
}
]}
'''
print(employee_data)

data=json.loads(employee_data)
print(data)

