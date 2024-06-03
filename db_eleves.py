import sqlite3



# ______________________________________
# FUNCTION TO CONNECT TO DB
# ______________________________________

def get_db_connection():
    # conn = sqlite3.connect("db_flaskapi.db", timeout=10)  # Ajout d'un timeout de 10 secondes
    conn = sqlite3.connect("db_flaskapi.db")  # Ajout d'un timeout de 10 secondes
    conn.row_factory = sqlite3.Row
    return conn


# ______________________________________
# DEFINE NEW FUNCTION (1/2)
# ______________________________________
def select_all():

    # -------- DB CONNECTION --------
    conn = get_db_connection()

    # -------- RESULTSET FOR SQL REQUESTS --------
    cur = conn.cursor()

    # -------- SELECT ALL TABLE ROWS --------
    # SQL REQUEST
    res1 = cur.execute("""SELECT * FROM Eleves""")
    eleves = res1.fetchall()  # On stock les résultats pour pouvoir les renvoyer
    # print("db eleves : ", eleves)
    # print(res1.fetchall()) OR (EQUALS )print(list(res1))

    # -------- CLOSE DB CONNECTION --------
    conn.close()
    return eleves  # après avoir fermé la connexion


def select_eleves_par_nom(nom):
    conn = get_db_connection()
    cur = conn.cursor()
    res = cur.execute(
        "SELECT nom, prenom, age, classe FROM Eleves WHERE nom = ?", (nom,)
    )
    eleves = res.fetchall()  # On stock les résultats pour pouvoir les renvoyer
    conn.close()
    return eleves  # après avoir fermé la connexion


def select_eleves(saisie):
    conn = get_db_connection()
    cur = conn.cursor()
    #     cur.execute("SELECT * FROM Eleves WHERE nom LIKE ? OR prenom LIKE ? OR classe LIKE ?", ('%' + query + '%', '%' + query + '%', '%' + query + '%'))
    # res = cur.execute("SELECT nom, prenom, age, classe FROM Eleves WHERE nom LIKE ? OR prenom LIKE ?", ('%'+saisie+'%', '%'+saisie+'%'))
    res = cur.execute(
        "SELECT nom, prenom, age, classe FROM Eleves WHERE nom LIKE ? OR prenom LIKE ? OR classe LIKE ?",
        ("%" + str(saisie) + "%", "%" + str(saisie) + "%", "%" + str(saisie) + "%"),
    )
    eleves = res.fetchall()  # On stock les résultats pour pouvoir les renvoyer
    conn.close()
    return eleves  # après avoir fermé la connexion


# ______________________________________
# select by ID
# ______________________________________
def select_eleve_by_id(student_id):
    conn = get_db_connection()
    cur = conn.cursor()

    res = cur.execute("SELECT * FROM Eleves WHERE id = ?", (student_id,))
    student = res.fetchone()  # On stock les résultats pour pouvoir les renvoyer

    conn.close()
    return student  # après avoir fermé la connexion


# ______________________________________
# INSERT NEW ROW
# ______________________________________
def insert_eleve(eleve):
    # -------- DB CONNECTION --------
    conn = get_db_connection()

    # -------- RESULTSET FOR SQL REQUESTS --------
    cur = conn.cursor()

    # EXECUTE SQL REQUEST
    cur.execute(
        """INSERT INTO Eleves(nom, prenom, age, classe) VALUES (?, ?, ?, ?)""", eleve
    )
    # COMMIT REQUEST --> VALIDATION DE LA REQUETE / EXECUTION -> PERSISTANCE/ENREGISTREMENT DE L'ELEVE
    conn.commit()
    # -------- CLOSE DB CONNECTION --------
    conn.close()


# ______________________________________
# DELETE ELEVE BY ID
# ______________________________________
def delete_eleve(student_id):
    # -------- DB CONNECTION --------
    conn = get_db_connection()

    # -------- RESULTSET FOR SQL REQUESTS --------
    cur = conn.cursor()

    # EXECUTE SQL REQUEST
    cur.execute("DELETE FROM Eleves WHERE id = ?", (student_id,))
    # COMMIT REQUEST --> VALIDATION DE LA REQUETE / EXECUTION -> PERSISTANCE/ENREGISTREMENT DE L'ELEVE

    conn.commit()
    
    print("Select ALL (File db_eleves.py) : ", select_all())
 

    # -------- CLOSE DB CONNECTION --------
    conn.close()


# ______________________________________
# INSERT NEW ROW
# ______________________________________


def update_eleve(last_name, first_name, age, classe, student_id):

    # -------- DB CONNECTION --------
    conn = get_db_connection()

    # -------- RESULTSET FOR SQL REQUESTS --------
    cur = conn.cursor()

    """
    eleve = []
    eleve.append(last_name)
    eleve.append(first_name)
    eleve.append(age)
    eleve.append(classe)
    # eleve.append(student_id)
    
    
    # -------- SECOND INSERT --------
    # DECLARE VARIABLE ELEVE (LIST)
    eleve = (last_name, first_name, age, classe)   
    
    """

    # EXECUTE SQL REQUEST
    cur.execute(
        """
        UPDATE Eleves
        SET nom = ?, prenom = ?, age = ?, classe = ?
        WHERE id = ?
    """,
        (last_name, first_name, age, classe, student_id),
    )  # (eleve, student_id))

    # COMMIT REQUEST --> VALIDATION DE LA REQUETE / EXECUTION -> PERSISTANCE/ENREGISTREMENT DE L'ELEVE
    conn.commit()

    # -------- CLOSE DB CONNECTION --------
    conn.close()



'''

The debugger caught an exception in your WSGI application. You can now look at the traceback which led to the error.

To switch between the interactive traceback and the plaintext one, you can click on the "Traceback" headline. 
From the text traceback you can also create a paste of it. 
For code execution mouse-over the frame you want to debug and click on the console icon on the right side.

You can execute arbitrary Python code in the stack frames and there are some extra helpers available for introspection:

    dump() shows all variables in the frame
    dump(obj) dumps all that's known about the object

'''