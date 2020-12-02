from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///:memory:')
DBase = declarative_base()


class Curso(DBase):
    __tablename__ = 'curso'

    id = Column(Integer, Sequence('curso_id_seq'), primary_key=True)
    nombre = Column(String)

    alumnos = relationship('Alumno', back_populates='curso')
    horario = relationship('Horario', back_populates='curso')

    def registrar(self):
        Session = sessionmaker(bind=engine)
        Session().add(self)
        Session().commit()

    def __repr__(self):
        return '{}'.format(self.nombre)


class Profesor(DBase):
    __tablename__ = 'profesor'

    id = Column(Integer, Sequence('profesor_id_seq'), primary_key=True)
    nombre = Column(String)
    apellido = Column(String)

    horario = relationship('Horario', back_populates='profesor')

    def registrar(self):
        Session = sessionmaker(bind=engine)
        Session().add(self)
        Session().commit()

    def __repr__(self):
        return '{} {}'.format(self.nombre, self.apellido)


class Horario(DBase):
    __tablename__ = 'horario'

    cursoId = Column(Integer, ForeignKey('curso.id'), primary_key=True),
    profesorId = Column(Integer, ForeignKey('profesor.id'), primary_key=True),
    dia = Column(String, primary_key=True)
    desdeHs = Column(Integer)
    hastaHs = Column(Integer)

    profesor = relationship('Profesor', back_populates='horario')
    curso = relationship('Curos', back_populates='horario')

    def registrar(self):
        Session = sessionmaker(bind=engine)
        Session().add(self)
        Session().commit()

    def __repr__(self):
        return '{} de {}hs a {}hs'.format(self.dia, self.desdeHs, self.hastaHs)


class Alumno(DBase):
    __tablename__ = 'alumno'

    id = Column(Integer, Sequence('alumno_id_seq'), primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    cursoId = Column(Integer, ForeignKey('curso.id'))

    curso = relationship('Curso', back_populates='alumnos')

    def registrar(self):
        Session = sessionmaker(bind=engine)
        Session().add(self)
        Session().commit()

    def __repr__(self):
        return '{} {}'.format(self.nombre, self.apellido)


DBase.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

curso1 = Curso(nombre='Bases de Datos')
curso1.registrar()
curso2 = Curso(nombre='Algoritmos')
curso2.registrar()


profesor1 = Profesor(nombre='Horacio', apellido='Kans')
profesor1.registrar()
profesor2 = Profesor(nombre='Jorge', apellido='Mendoza')
profesor3 = Profesor(nombre='Manuel', apellido='Benitez')
profesor4 = Profesor(nombre='Angela', apellido='Lopez')

Session().addAll([profesor2, profesor3, profesor4])


horario1 = Horario(cursoId=1, profesorId=1, dia='Lunes', desdeHs=8, hastaHs=12)
horario1.registrar()
horario2 = Horario(cursoId=1, profesorId=2,
                   dia='Miercoles', desdeHs=18, hastaHs=22)
horario3 = Horario(cursoId=2, profesorId=3,
                   dia='Martes', desdeHs=18, hastaHs=23)
horario4 = Horario(cursoId=2, profesorId=4,
                   dia='Viernes', desdeHs=8, hastaHs=13)
horario5 = Horario(cursoId=2, profesorId=1,
                   dia='Jueves', desdeHs=14, hastaHs=19)

Session().addAll([horario2, horario3, horario4, horario5])


alumn1 = Alumno(nombre='Nacho', apellido='Garcia', cursoId=1)
alumn1.registrar()
alumn2 = Alumno(nombre='Juana', apellido='Perez', cursoId=1)
alumn3 = Alumno(nombre='Matias', apellido='Gonzales', cursoId=1)
alumn4 = Alumno(nombre='Liliana', apellido='Herrera', cursoId=1)
alumn5 = Alumno(nombre='Martin', apellido='Gimenez', cursoId=1)
alumn6 = Alumno(nombre='Sabrina', apellido='Sosa', cursoId=2)
alumn7 = Alumno(nombre='Santiago', apellido='Heredia', cursoId=2)
alumn8 = Alumno(nombre='Abril', apellido='Obispo', cursoId=2)
alumn9 = Alumno(nombre='Julian', apellido='Lopez', cursoId=2)

Session().addAll([alumn2, alumn3, alumn4,
                  alumn5, alumn6, alumn7, alumn8, alumn9])

Session().commit()

# Alumnos con curso
Session().query(Alumno).join(Curso, Alumno.cursoId == Curso.id).all()

# Horario de Profesores
Session().query(Profesor).join(Horario, Profesor.id == Horario.profesorId).all()

# Horario de Curso
Session().query(Curso).join(Horario, Curso.id == Horario.cursoId).all()
