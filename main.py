import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Para validar los nombres que están disponibles y que no haya un null
#class StudentsName(str, Enum):
  #  Ana = 'Ana'
 #   Pilar = 'Pilar'

#Students = {

    #StudentsName.Ana: {

      #  'name': StudentsName.Ana.value,
     #   'age': 19
    #}

    #StudentsName.Pilar: {

   #     'name': StudentsName.Pilar.value,
  #      'age': 19
 #   }

#}

#@app.get('/{name}', status_code=status.HTTP_200_OK)
#def hello_world(id: StudentsName = Patch(..., title='Nombre del estudiante',
  #                                          description='Nombre del estudiante que queremos validar'), 
 #                                           age: int = Query(..., title='Edad estudiante', description='La edad del estudiante')) -> Dict[str, Any]: #Los puntos significa que es un parámetro requerido
#      return {**Students[name], 'age_valid': Students[name][age] == age}

students = []

class Students(BaseModel):
    id: str
    name: str
    last_name: str
    dni: str


@app.get('/students')
def get_students():
   
    return students

@app.post('/students')
 def save_students(students: Students):
   
    students.append(students.dict())#Seimplementará en el array
   
    return students[-1] #Va a devolver el último añadido

@app.get('/students/{students_id}')
def ger_students(students_id: str):
    
    for student in students:

        if student['id'] == students_id

            return student

    return 'No encontrado'

@app.delete('/students/{students_id}')
def delete_student(students_id: str):

    for index,student in enumerate(students):

        if student['id'] == students_id:
            students.pop(index)

            return 'Estudiante eliminado'
 
    return'Estudiante no encontrado, por lo tanto no se ha podido eliminar'

@app.put('/students/{students_id}')
def update_students(students_id: str, updateStudents: Students):

    for index, student in enumerate(students):

        if student['id'] == students_id:

            students[index]['name'] == updateStudents.name
            students[index]['last_name'] == updateStudents.last_name
            students[index]['dni'] == updateStudents.dni

        return 'Estudiante modificado'

    return 'Estudiante no encontrado, por lo tanto no se ha podido modificar'