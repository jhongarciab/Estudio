from Cursor import CursorDelPool
import sys

class EjecutorSentencias:
    @classmethod
    def ejecutar_ddl(cls):
        sentencias = [
            """
            CREATE TABLE IF NOT EXISTS Estudiantes (
                id_estudiante SERIAL PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                correo VARCHAR(100) UNIQUE NOT NULL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS Proyectos (
                id_proyecto SERIAL PRIMARY KEY,
                titulo VARCHAR(150) NOT NULL,
                descripcion TEXT,
                fecha_inicio DATE,
                fecha_entrega DATE,
                id_estudiante INTEGER REFERENCES Estudiantes(id_estudiante)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS Archivos (
                id_archivo SERIAL PRIMARY KEY,
                nombre_archivo VARCHAR(100),
                tipo VARCHAR(50),
                ruta TEXT,
                id_proyecto INTEGER REFERENCES Proyectos(id_proyecto)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS Evaluaciones (
                id_evaluacion SERIAL PRIMARY KEY,
                calificacion NUMERIC(3,1),
                comentarios TEXT,
                id_proyecto INTEGER REFERENCES Proyectos(id_proyecto)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS Asignaturas (
                id_asignatura SERIAL PRIMARY KEY,
                nombre VARCHAR(100),
                semestre VARCHAR(20)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS Colaboradores (
                id_colaborador SERIAL PRIMARY KEY,
                nombre VARCHAR(100),
                rol VARCHAR(50),
                id_proyecto INTEGER REFERENCES Proyectos(id_proyecto)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS Proyecto_Asignatura (
                id_proyecto INTEGER REFERENCES Proyectos(id_proyecto),
                id_asignatura INTEGER REFERENCES Asignaturas(id_asignatura),
                PRIMARY KEY (id_proyecto, id_asignatura)
            )
            """
        ]
        
        try:
            with CursorDelPool() as cursor:
                for sentencia in sentencias:
                    cursor.execute(sentencia)
                print("Todas las sentencias DDL se ejecutaron correctamente")
        except Exception as e:
            print(f"Error al ejecutar DDL: {e}")
            sys.exit(1)

    @classmethod
    def ejecutar_dml(cls):
        sentencias = [
            """
            INSERT INTO Estudiantes (nombre, correo) 
            VALUES ('Laura Méndez', 'laura.mendez@uni.edu.co')
            """,
            """
            INSERT INTO Proyectos (titulo, descripcion, fecha_inicio, fecha_entrega, id_estudiante) 
            VALUES ('Simulación de Caída Libre', 'Proyecto para analizar el movimiento bajo gravedad', 
                    '2025-04-15', '2025-05-01', 1)
            """,
            """
            UPDATE Proyectos 
            SET titulo = 'Simulación de Movimiento Uniformemente Acelerado' 
            WHERE id_proyecto = 1
            """
        ]
        
        try:
            with CursorDelPool() as cursor:
                for sentencia in sentencias:
                    cursor.execute(sentencia)
                print("Todas las sentencias DML se ejecutaron correctamente")
        except Exception as e:
            print(f"Error al ejecutar DML: {e}")
            sys.exit(1)

    @classmethod
    def ejecutar_dcl(cls):
        sentencias = [
            """
            DO $$
            BEGIN
                IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'docente') THEN
                    CREATE ROLE docente LOGIN PASSWORD 'segura123';
                END IF;
            END
            $$;
            """,
            """
            GRANT SELECT, INSERT, UPDATE ON Estudiantes, Proyectos TO docente;
            """,
            """
            REVOKE UPDATE ON Proyectos FROM docente;
            """
        ]
        
        try:
            with CursorDelPool() as cursor:
                for sentencia in sentencias:
                    cursor.execute(sentencia)
                print("Todas las sentencias DCL se ejecutaron correctamente")
        except Exception as e:
            print(f"Error al ejecutar DCL: {e}")
            sys.exit(1)

    @classmethod
    def ejecutar_todo(cls):
        cls.ejecutar_ddl()
        cls.ejecutar_dml()
        cls.ejecutar_dcl()

if __name__ == '__main__':
    EjecutorSentencias.ejecutar_todo()