import sqlite3 

#______________________________________
# DEFINE NEW FUNCTION (1/2)  
#______________________________________
def select_all(): 

        # -------- DB CONNECTION --------
        conn = sqlite3.connect('eleves.db') 
    
        # -------- RESULTSET FOR SQL REQUESTS -------- 
        cur = conn.cursor() 
    
    
        # -------- SELECT ALL TABLE ROWS --------
        '''
        # SQL REQUEST 
        res1 = cur.execute("""SELECT * FROM Eleves""")
        res1.fetchall()
        # print(res1.fetchall()) OR (EQUALS )print(list(res1))   
        '''

    
        # -------- SELECT ONLY ONE RESULT (ROW) AND SET CURSOR ON NEXT ROW --------
        '''  
        res2 = cur.execute("""SELECT * FROM Eleves """) # SQL REQUEST 
        res2.fetchone() # RETURN/SELECT ROW 1 AND SET CURSOR ON ROW 2
        res2.fetchone() # RETURN/SELECT ROW 2 AND SET CURSOR ON ROW 3
        res2.fetchone() # RETURN/SELECT ROW 3 AND SET CURSOR ON ROW 4
        # ... 
        
        # print(res2.fetchone()) OR print(list(res2)) 
        '''
    
    
        # -------- SELECT X RESULTS (ROWS) AND SET CURSOR ON X+1 ROWS --------
        '''
        res3 = cur.execute("""SELECT * FROM Eleves """) # SQL REQUEST 
        res3.fetchmany(3) # RETURN 3 ROWS (1-3) AND SET CURSOR ON 4TH ROWS 
        res3.fetchmany(3) # RETURN 3 ROWS (4-6) AND SET CURSOR ON 7TH ROWS 
        
        print(res3.fetchmany(3)) 
        print(res3.fetchmany(3)) 
        
        '''
        
        
        '''
        res4 = cur.execute("""SELECT id, nom, prenom FROM Eleves WHERE nom = ? """, ('Dupont',)) # Virgule obligatoire -> Python attend un TUPLE (TABLE ROW)
        print(res4.fetchall())    
        
        res5 = cur.execute("""SELECT id, nom, prenom FROM Eleves WHERE nom = :nom """, {'nom':'Dupont'}) # Virgule obligatoire -> Python attend un TUPLE (TABLE ROW)
        print(res5.fetchall())     
              
         
          
        '''


        
        
        # -------- CLOSE DB CONNECTION -------- 
        conn.close() 
        
        
#______________________________________
# EXECUTE FUNCTION (2/2) 
#______________________________________
select_all()


#______________________________________
# INSTRUCTIONS SQL/PYTHON DE BASE 
#______________________________________

'''
BILAN / RESUME

conn = sqlite3.connect('eleves.db') 
cur = conn.cursor() 

# EXECUTION DES REQUETES ICI (METHOD. CUR.EXECUTE() )

        # Insérer des enregistrements 
        cur.execute(" INSERT INTO ...")
        cur.execute(" INSERT INTO ... (?, ?, ....)", un_tuple)
        cur.execute(" INSERT INTO ... (:cle1, :cle2, ...)", un_dico)
        conn.commit() 
        
        cur.executemany(" INSERT INTO ... (?, ?, ....)", liste_tuples)
        cur.executemany(" INSERT INTO ... (:cle1, :cle2, ...)", liste_dicos)       
        conn.commit() 
        
        
        # Interroger la base de données 
        res1 = cur.execute("SELECT ...")
        res2 = cur.execute("SELECT ... WHERE ... ? ... ?", un_tuple)
        res3 = cur.execute("SELECT ... :cle1 .... :cle2", un_dico)
        
        res.fetchall() # récupérer tous les résultats (lignes)
        res.fetchone() # récupérer un résultat (ligne) et pointe sur la  ligne suivante
        res.fetchmany() # récupérer n résultats (n >= 1) et pointe sur la ligne suivante

conn.close() 
'''


def select_by_name(nom): 
        conn = sqlite3.connect('BD_Flask.db') 
        cur = conn.cursor() 
        
        # res = cur.execute("SELECT id, nom, prenom, age, classe classe FROM Eleves WHERE nom = ? ", (nom,))
        res = cur.execute("SELECT nom, prenom, age, classe FROM Eleves WHERE nom = ? ", (nom,))
        eleves = res.fetchall() # On stocke les résultats pour pouvoir les renvoyer 
        

        conn.close()    
        return eleves # après avoir fermé la connexion     
        
'''
        print(select_by_name('Martin')) 
        print(select_by_name('Richard')) 
        print(select_by_name('Obama')) 
'''
