BEGIN TRANSACTION;
CREATE TABLE "profesor"(
	"profesorId"	INTEGER,
	"profesorNombre"	TEXT,
	"profesorApellido"	TEXT,
	PRIMARY KEY("profesorId")
);
CREATE TABLE "curso"(
	"cursoId"	INTEGER,
	"cursoNombre"	TEXT,
	PRIMARY KEY("cursoId")
);
CREATE TABLE "horario"(
	"dia"	INTEGER,
	"cursoId"	INTEGER,
	"profesorId"	INTEGER,
	"desdeHs"	INTEGER,
	"hastaHs"	INTEGER,
	PRIMARY KEY("dia","cursoId","profesorId"),
	FOREIGN KEY("profesorId") REFERENCES "profesor"("profesorId"),
	FOREIGN KEY("cursoId") REFERENCES "curso"("cursoId")
);
CREATE TABLE "alumno"(
	"alumnoId"	INTEGER,
	"alumnoNombre"	TEXT,
	"alumnoApellido"	TEXT,
	"cursoId"	INTEGER,
	PRIMARY KEY("alumnoId"),
	FOREIGN KEY("cursoId") REFERENCES "curso"("cursoId")
);
COMMIT;