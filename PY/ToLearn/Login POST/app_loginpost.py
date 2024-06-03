from flask import Flask, render_template, request, redirect, url_for
import datetime 


app = Flask(__name__)

#__________________________________________________________
# ROUTE - HOME 
#__________________________________________________________
@app.route("/")
def bonjour():
    return render_template("index.html")

#__________________________________________________________
# ROUTE - erreur.html 
#__________________________________________________________
@app.route("/erreur")
def erreur():
    return render_template("erreur.html")

#__________________________________________________________
# ROUTE - LOGIN 
#__________________________________________________________
@app.route("/login")
def login(): 
    return render_template("login.html") 

#__________________________________________________________
# ROUTE - TRAITEMENT FORM
#__________________________________________________________
@app.route("/traitement", methods=["POST", "GET"])
def traitement(): 
    if request.method == "POST": 
    
        donnees = request.form
        nom = donnees.get('name')
        mdp = donnees.get('password')
        print(donnees) # TEST DU DONNES DES FORMULAIRE (REQUEST get)
        print(nom, mdp) # AFFICHE VALEURS SAISIES DANS FORMULAIRE 
        
        if nom == "ADMIN-ABC" and mdp == 'admin1admin1':
            return render_template("traitement.html", nom_utilisateur=nom) 
        else: 
            return render_template("traitement.html")    
    else: #METHODE GET, FOR EXAMPLE 
       return redirect(url_for('erreur')) 
   
   #__________________________________________________________
    # METHOD POST 
    #__________________________________________________________
    '''
            if nom == "ADMIN-ABC" and mdp == 'admin1admin1':
            return f"Bonjour {nom}, vous êtes connecté !"
        else: 
            return f"Problème rencontré. impossible de connecter l'utilisateur '{nom}'" 
    '''
    
    '''
        donnees = request.form
        nom = donnees.get('name')
        mdp = donnees.get('password')
        print(donnees) # TEST DU DONNES DES FORMULAIRE (REQUEST get)
        print(nom, mdp) # AFFICHE VALEURS SAISIES DANS FORMULAIRE 
    '''
    
    
    '''
        print(request.view_args) # CODE
        
        # RESULTATS DES TESTS 
        # VISUAL CODE   -->     127.0.0.1 - - [13/May/2024 13:09:29] "GET /traitement?name=User1&password=erterqeweqwewqe HTTP/1.1" 200 - 
        # OUTILS CHROME -->     traitement?name=User1&password=erterqeweqwewqe	     
    '''
    
    #__________________________________________________________
    # METHOD GET  
    #__________________________________________________________
    '''
    # CODE 
        print(request.args) # all parameters in Browser URL 
        print(request.args['param1']) # param1
        print(request.args['param2']) # param2      
    '''
    
    # LAST COMMAND / INSTRUCTION 
    # return "Traitement des données"
    # return render_template("login.html") 
    
#__________________________________________________________
# EXECUTE SERVEUR --> SEE console & browser to test. 
#__________________________________________________________
if __name__ == '__main__': 
    #app.run(debug=True) # Running on http://127.0.0.1:5000
    app.run(host='0.0.0.0', port=8080, debug=True)
    
 
    
# EXECUTION 
'''
    * Serving Flask app 'mon_app'
    * Debug mode: on
    * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
'''
