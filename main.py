from Database import Database
from TeacherCrud import TeacherCrud

db = Database("bolt://44.211.230.85:7687", "neo4j", "amperes-compromise-interview")
db.drop_all()

teachers_database = TeacherCrud(db)


teachers_database.create_teacher("Chris Lima", 1956, "189.052.396-66")
print(teachers_database.get_teacher())
teachers_database.update_teacherCpf("189.052.396-66","162.052.777-77" )
print(teachers_database.get_teacher())

db.close()
