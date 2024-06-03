import sqlite3

def select_one_authentification(mail, mdp): 
    conn = sqlite3.connect('db_flaskapi.db') 
    cur = conn.cursor()
    res = cur.execute("SELECT mail, mdp, role FROM Authentifications WHERE mail = ? AND mdp = ?", (str(mail), str(mdp)))
    eleve = res.fetchall() # On stock les résultats pour pouvoir les renvoyer 
    conn.close() 
    return eleve # après avoir fermé la connexion 

# print("select_one_authentification : ", select_one_authentification("mail@mail.com", "pass11"))


def select_many_authentifications(): 
    conn = sqlite3.connect('db_flaskapi.db') 
    cur = conn.cursor()
    # res = cur.execute("SELECT nom, prenom, age, classe FROM Eleves WHERE nom LIKE ? OR prenom LIKE ?", ('%'+saisie+'%', '%'+saisie+'%'))
    res = cur.execute("SELECT mail, mdp, role FROM Authentifications")
    list_authentifications = res.fetchall() # On stock les résultats pour pouvoir les renvoyer 
    # print(list_authentifications )
    conn.close() 
    return list_authentifications # après avoir fermé la connexion 


# select_authentifications()


def insert_authentification(user): 
     # -------- DB CONNECTION --------
    conn = sqlite3.connect('db_flaskapi.db') 
    
    # -------- RESULTSET FOR SQL REQUESTS -------- 
    cur = conn.cursor() # 
    
    # --------  INSERT/ TUPLE --------
    cur.execute("""INSERT INTO Authentifications(mail, mdp, role) VALUES (:mail, :mdp, :role)""", user) 
    # COMMIT REQUEST --> VALIDATION DE LA REQUETE / EXECUTION -> PERSISTANCE/ENREGISTREMENT DE L'ELEVE 
    conn.commit() 
    
    '''
    def mysql(): 
        # import mysql.connector

        mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="mydatabase"
        )

        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM customers")
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)
    '''   
