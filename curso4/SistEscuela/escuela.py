from sqlalchemy import create_engine, Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

class DBMannager(object):
  def __init__(self):
    try:
      self.engine = create_engine('sqlite:///data.sqlite')
      self.base = declarative_base()
      Session = sessionmaker(bind=self.engine)
      self.session = Session()

      print('Conectado')
    except:
      raise

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

  def nuevoAlumno(self, nombre, apellido, cursoId):
    return Alumno(alumnoNombre=nombre, alumnoApellido=apellido, cursoId=cursoId)
  
  def nuevoProfesor(self, nombre, apellido):
    return Profesor(profesorNombre=nombre, profesorApellido=apellido)

  def nuevoCurso(self, nombre):
    return Curso(cursoNombre=nombre)

  def nuevoHorario(self, dia, desdeHs, hastaHs, cursoId, profesorId):
    return Horario(dia=dia, desdeHs=desdeHs, hastaHs=hastaHs, cursoId=cursoId, profesorId=profesorId)

  def saveObject(self, objeto):
    try:
        self.session.add(objeto)
        self.session.commit()
        return('Guardado')
    except:
        self.session.rollback()
        raise

  def saveList(self, lista):
    try:
        self.session.add_all(lista)
        self.session.commit()
        return('Guardado')
    except:
        self.session.rollback()
        raise

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

curso1 = db.nuevoCurso('Bases de Datos')
curso2 = db.nuevoCurso('Algoritmos')

alumn1 = db.nuevoAlumno('Nacho', 'Garcia', 1)
alumn2 = db.nuevoAlumno('Juana', 'Perez', 1)
alumn3 = db.nuevoAlumno('Matias', 'Gonzales', 1)
alumn4 = db.nuevoAlumno('Liliana', 'Herrera', 1)
alumn5 = db.nuevoAlumno('Martin', 'Gimenez', 1)
alumn6 = db.nuevoAlumno('Sabrina', 'Sosa', 2)
alumn7 = db.nuevoAlumno('Santiago', 'Heredia', 2)
alumn8 = db.nuevoAlumno('Abril', 'Obispo', 2)
alumn9 = db.nuevoAlumno('Julian', 'Lopez', 2)

profesor1 = db.nuevoProfesor('Horacio', 'Kans')
profesor2 = db.nuevoProfesor('Jorge', 'Mendoza')
profesor3 = db.nuevoProfesor('Manuel', 'Benitez')
profesor4 = db.nuevoProfesor('Angela', 'Lopez')

horario1 = db.nuevoHorario('Lunes', 8, 12, 1, 1)
horario2 = db.nuevoHorario('Miercoles', 18, 22, 1, 2)
horario3 = db.nuevoHorario('Martes', 18, 23, 2, 3)
horario4 = db.nuevoHorario('Viernes', 8, 13, 2, 4)
horario5 = db.nuevoHorario('Jueves', 14, 19, 2, 1)

print(db.saveObject(alumn1),
db.saveObject(profesor1),
db.saveObject(horario1),
db.saveList([alumn2, alumn3, alumn4, alumn5, alumn6, alumn7, alumn8, alumn9]),
db.saveList([curso1, curso2]),
db.saveList([profesor2, profesor3, profesor4]),
db.saveList([horario2, horario3, horario4, horario5]))

for x in db.listCursoAlumno():
  print(x)

for x in db.listHorarioProfesor():
  print(x)

for x in db.listHorarioCurso():
  print(x)