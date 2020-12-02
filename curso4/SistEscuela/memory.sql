BEGIN TRANSACTION;
CREATE TABLE "profesor"(
	"id"	INTEGER,
	"nombre"	TEXT,
	"apellido"	TEXT,
	PRIMARY KEY("id")
);
CREATE TABLE "curso"(
	"id"	INTEGER,
	"nombre"	TEXT,
	PRIMARY KEY("id")
);
CREATE TABLE "horario"(
	"dia"	INTEGER,
	"cursoId"	INTEGER,
	"profesorId"	INTEGER,
	"desdeHs"	INTEGER,
	"hastaHs"	INTEGER,
	PRIMARY KEY("dia","cursoId","profesorId"),
	FOREIGN KEY("profesorId") REFERENCES "profesor"("id"),
	FOREIGN KEY("cursoId") REFERENCES "curso"("id")
);
CREATE TABLE "alumno"(
	"id"	INTEGER,
	"nombre"	TEXT,
	"apellido"	TEXT,
	"cursoId"	INTEGER,
	PRIMARY KEY("id"),
	FOREIGN KEY("cursoId") REFERENCES "curso"("id")
);
COMMIT;