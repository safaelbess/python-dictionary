entervalue=True
students=[]
 

while entervalue:
  student={}
  students.append(student)
  inserttimes = int(input ('how many elements do you want to have?'))
  deckey= input ('enter the key of the student')
  valueType =int(input ('enter the type of the value 1 for str 2 for int 3 for list 4 for dict'))
  if valueType ==1:
    student[deckey]=input ('enter the value')

  elif valueType==2:

    student[deckey]= int(input('enter the value'))  

  elif valueType==3:
    times = int (input('how many skills do you want to add'))
    for j in range(times):
      decValue=[]
      listValue =input('enter the value ')
      decValue.append(listValue)

  elif valueType==4:
    stdictionary={}
    times= int(input('how many dictionary keys do you want to add?'))
    for i in (times):
      deckey=input('enter the dictinary key :')   
      decValue =input ("enter the dictionary value") 
      stdictionary[deckey]=decValue
    print(students) 

  addother=input('do you want to add an other student?')     
  if addother=='no':
    entervalue=False

    
  print(students) 

