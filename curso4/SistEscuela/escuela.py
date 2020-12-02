from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

class DBMannager(object):
  def __init__(self):
    self.engine = create_engine('sqlite:///:memory:')
    self.base = declarative_base()
    Session = sessionmaker(bind=self.engine)
    self.session = Session()

  def listCursoAlumno(self):
    return self.session.execute("""
      SELECT *
      FROM alumno a, curso c
      WHERE a.cursoId = c.cursoId
      ORDER BY a.alumnoNombre, a.alumnoApellido, c.cursoNombre
    """).fetchall()

  def listHorarioProfesor(self):
    return self.session.execute("""
      SELECT *
      FROM horario h, profesor p
      WHERE h.profesorId = p.profesorId
      ORDER BY h.dia, p.profesorNombre, p.profesorApellido
    """).fetchall()

  def listHorarioCurso(self):
    return self.session.execute("""
      SELECT *
      FROM horario h, curso c
      WHERE h.cursoId = c.cursoId
      ORDER BY h.dia, c.cursoNombre
    """).fetchall()


  def saveObject(self, objeto):
    self.session.add(objeto)
    self.session.commit()

  def saveList(self, lista):
    self.session.add_all(lista)
    self.session.commit()

db = DBMannager()

class Horario(db.base):
  __tablename__ = 'horario'

  dia = Column('dia', String, primary_key=True)
  profesorId = Column('profesorId', Integer, ForeignKey('profesor.profesorId'), primary_key=True)
  cursoId = Column('cursoId', Integer, ForeignKey('curso.cursoId'), primary_key=True)
  desdeHs = Column('desdeHs', Integer)
  hastaHs = Column('hastaHs', Integer)

  profesores = relationship('Profesor', back_populates='horarios')
  cursos = relationship('Curso', back_populates='horarios')

  def __repr__(self):
    return '{} {} {}'.format(self.dia, self.desdeHs, self.hastaHs)


class Curso(db.base):
  __tablename__ = 'curso'

  cursoId = Column('cursoId', Integer, Sequence('curso_cursoId_seq'), primary_key=True)
  cursoNombre = Column('cursoNombre', String)

  alumnos = relationship('Alumno', back_populates='curso')
  horarios = relationship('Horario', back_populates='cursos')

  def __repr__(self):
    return '{}'.format(self.cursoNombre)


class Profesor(db.base):
  __tablename__ = 'profesor'

  profesorId = Column('profesorId', Integer, Sequence('profesor_profesorId_seq'), primary_key=True)
  profesorNombre = Column('profesorNombre', String)
  profesorApellido = Column('profesorApellido', String)

  horarios = relationship('Horario', back_populates='profesores')

  def __repr__(self):
    return '{} {}'.format(self.profesorNombre, self.profesorApellido)


class Alumno(db.base):
  __tablename__ = 'alumno'

  alumnoId = Column('alumnoId', Integer, Sequence('alumno_alumnoId_seq'), primary_key=True)
  alumnoNombre = Column('alumnoNombre', String)
  alumnoApellido = Column('alumnoApellido', String)
  cursoId = Column('cursoId', Integer, ForeignKey('curso.cursoId'))

  curso = relationship('Curso', back_populates='alumnos')

  def __repr__(self):
    return '{} {}'.format(self.alumnoNombre, self.alumnoApellido)

db.base.metadata.create_all(db.engine)

alumn1 = Alumno(alumnoNombre='Nacho', alumnoApellido='Garcia')
alumn2 = Alumno(alumnoNombre='Juana', alumnoApellido='Perez')
alumn3 = Alumno(alumnoNombre='Matias', alumnoApellido='Gonzales')
alumn4 = Alumno(alumnoNombre='Liliana', alumnoApellido='Herrera')
alumn5 = Alumno(alumnoNombre='Martin', alumnoApellido='Gimenez')
alumn6 = Alumno(alumnoNombre='Sabrina', alumnoApellido='Sosa')
alumn7 = Alumno(alumnoNombre='Santiago', alumnoApellido='Heredia')
alumn8 = Alumno(alumnoNombre='Abril', alumnoApellido='Obispo')
alumn9 = Alumno(alumnoNombre='Julian', alumnoApellido='Lopez')

curso1 = Curso(cursoNombre='Bases de Datos')
curso2 = Curso(cursoNombre='Algoritmos')

alumn1.curso = curso1
alumn2.curso = curso1
alumn3.curso = curso1
alumn4.curso = curso1
alumn5.curso = curso1
alumn6.curso = curso2
alumn7.curso = curso2
alumn8.curso = curso2
alumn9.curso = curso2

profesor1 = Profesor(profesorNombre='Horacio', profesorApellido='Kans')
profesor2 = Profesor(profesorNombre='Jorge', profesorApellido='Mendoza')
profesor3 = Profesor(profesorNombre='Manuel', profesorApellido='Benitez')
profesor4 = Profesor(profesorNombre='Angela', profesorApellido='Lopez')

horario1 = Horario(dia='Lunes', desdeHs=8, hastaHs=12)
horario2 = Horario(dia='Miercoles', desdeHs=18, hastaHs=22)
horario3 = Horario(dia='Martes', desdeHs=18, hastaHs=23)
horario4 = Horario(dia='Viernes', desdeHs=8, hastaHs=13)
horario5 = Horario(dia='Jueves', desdeHs=14, hastaHs=19)

horario1.cursos = curso1
horario1.profesores = profesor1
horario2.cursos = curso1
horario2.profesores = profesor2
horario3.cursos = curso2
horario3.profesores = profesor3
horario4.cursos = curso2
horario4.profesores = profesor4
horario5.cursos = curso2
horario5.profesores = profesor1

db.saveObject(alumn1)
db.saveObject(profesor1)
db.saveObject(horario1)
db.saveList([alumn2, alumn3, alumn4, alumn5, alumn6, alumn7, alumn8, alumn9])
db.saveList([curso1, curso2])
db.saveList([profesor2, profesor3, profesor4])
db.saveList([horario2, horario3, horario4, horario5])

for x in db.listCursoAlumno():
  print(x)

for x in db.listHorarioProfesor():
  print(x)

for x in db.listHorarioCurso():
  print(x)