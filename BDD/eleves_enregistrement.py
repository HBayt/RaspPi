import sqlite3 

#______________________________________
# DEFINE NEW FUNCTION (1/2)  
#______________________________________
def creer_table(): 
    conn = sqlite3.connect('eleves.db') 
    cur = conn.cursor() 

    # Before creating Table, Delete it to create it again 
    cur.execute("DROP TABLE IF EXISTS Eleves;")

    cur.execute("""CREATE TABLE Eleves(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT, 
        prenom TEXT, 
        age	INTEGER,
        classe	TEXT); 
    """)
    conn.close() 

#______________________________________
# EXECUTE FUNCTION (2/2) 
#______________________________________
creer_table()



#______________________________________
# INSERT NEW ROW
#______________________________________
def insert_eleve(): 
     # -------- DB CONNECTION --------
    conn = sqlite3.connect('eleves.db') 
    
    # -------- RESULTSET FOR SQL REQUESTS -------- 
    cur = conn.cursor() # 
    
    # -------- FIRST INSERT --------
    # SQL REQUEST 
    cur.execute("""INSERT INTO Eleves(id, nom, prenom, age, classe) VALUES (1, 'Dupont', 'Jean', 15, '2A')""")
    
    # VALIDATION DE LA REQUETE / EXECUTION -> PERSISTANCE/ENREGISTREMENT DE L'ELEVE 
    conn.commit() 

    
    # -------- SECOND INSERT --------
    # DECLARE VARIABLE ELEVE (LIST)
    eleve_2 = ('Dupont', 'Jeanne', 17, 'TG2')  
    # EXECUTE SQL REQUEST
    cur.execute("""INSERT INTO Eleves(nom, prenom, age, classe) VALUES (?, ?, ?, ?)""", eleve_2) 
    # COMMIT REQUEST --> VALIDATION DE LA REQUETE / EXECUTION -> PERSISTANCE/ENREGISTREMENT DE L'ELEVE 
    conn.commit() 
    
    
     # -------- THIRD INSERT/ TUPLE --------
    # DECLARE VARIABLE ELEVE (DICTIONARY)
    eleve_3 = {'nom':'Marchand', 'prenom':'Marie', 'age': 15, 'classe':'2A'}
    # EXECUTE SQL REQUEST
    cur.execute("""INSERT INTO Eleves(nom, prenom, age, classe) VALUES (:nom, :prenom, :age, :classe)""", eleve_3) 
    # COMMIT REQUEST --> VALIDATION DE LA REQUETE / EXECUTION -> PERSISTANCE/ENREGISTREMENT DE L'ELEVE 
    conn.commit()    
    
    
     # -------- MANY INSERTS --------
    # DECLARE VARIABLE LIST_ELEVES (LIST)
    list_eleves = [
        ('Martin', 'Adeline', 16, '1G1'), 
        ('Dupont', 'Lucas', 15, '2A'), 
        ('Richard', 'Louise', 15, '1G2'), 
        ('Rouger', 'Marius', 16, '1G2'), 
        ('Louapre', 'Lola', 18, 'TG2'), 
        ('Boudou', 'Lise', 17, 'TG1'), 
        ('Dupont', 'Aurélien', 16, '1G1'), 
        ('Laurent', 'Diego', 17, '1G2'), 
        ('Martin', 'Anaëlle', 16, 'TG1'), 
        ('Dubois', 'Marc', 18, 'TG2')
    ]
    
    '''
     for eleve in list_eleves: 
        # EXECUTE SQL REQUEST
        cur.execute("""INSERT INTO Eleves(nom, prenom, age, classe) VALUES (?, ?, ?, ?)""", eleve) 
        # COMMIT REQUEST --> VALIDATION DE LA REQUETE / EXECUTION -> PERSISTANCE/ENREGISTREMENT DE L'ELEVE    
    ''' 
    
    cur.executemany("""INSERT INTO Eleves(nom, prenom, age, classe) VALUES (?, ?, ?, ?)""", list_eleves)
    
    # DECLARE VARIABLE DICT_ELEVES (DICTIONARY)
    dict_eleves = [
        {'nom':'Martin', 'prenom':'Adeline', 'age': 16, 'classe':'1G1'}, 
        {'nom':'Dupont', 'prenom':'Lucas', 'age': 15, 'classe':'2A'}, 
        {'nom':'Richard', 'prenom':'Louise', 'age': 15, 'classe':'1G2'}, 
        {'nom':'Rouger', 'prenom':'Marius', 'age': 16, 'classe':'1G2'}, 
        {'nom':'Louapre', 'prenom':'Lola', 'age': 18, 'classe':'TG2'}, 
        {'nom':'Boudou', 'prenom':'Lise', 'age': 17, 'classe':'TG1'}, 
        {'nom':'Dupont', 'prenom':'Aurélien', 'age': 16, 'classe':'1G1'}, 
        {'nom':'Laurent', 'prenom':'Diego', 'age': 17, 'classe':'1G2'}, 
        {'nom':'Martin', 'prenom':'Anaëlle', 'age': 16, 'classe':'TG1'}, 
        {'nom':'Dubois', 'prenom':'Marc', 'age': 18, 'classe':'TG2'},       
        {'nom':'Martin', 'prenom':'Tim', 'age': 19, 'classe':'1G2'}, 
        {'nom':'Marchand', 'prenom':'Valérie', 'age': 15, 'classe':'2A'}
    ]
    
    cur.executemany("""INSERT INTO Eleves(nom, prenom, age, classe) VALUES (:nom, :prenom, :age, :classe)""", dict_eleves)
    
    # COMMIT REQUEST --> VALIDATION DE LA REQUETE / EXECUTION -> PERSISTANCE/ENREGISTREMENT DE L'ELEVE 
    conn.commit()
                
     # -------- CLOSE DB CONNECTION -------- 
    conn.close() 

#______________________________________
# INSTRUCTIONS SQL/PYTHON DE BASE 
#______________________________________

'''
        conn = sqlite3.connect('eleves.db') 
        cur = conn.cursor() 
        conn.close() 
'''


insert_eleve()


