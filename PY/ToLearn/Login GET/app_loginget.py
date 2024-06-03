from flask import Flask, render_template, request, redirect, url_for
import datetime 


app = Flask(__name__)


# _______________________________________________________________________
# ROUTE - HOME 
# _______________________________________________________________________
@app.route("/")
def bonjour():
    return render_template("index.html")


# _______________________________________________________________________
# ROUTE - erreur.html 
# _______________________________________________________________________
@app.route("/erreur")
def erreur():
    return render_template("erreur.html")


# _______________________________________________________________________
# ROUTE - LOGIN 
# _______________________________________________________________________
@app.route("/login")
def login(): 
    return render_template("login.html") 



# _______________________________________________________________________
# ROUTE - TRAITEMENT FORM
# FORM WITH METHOD GET && @app.route("/traitement", methods=["GET"])
# _______________________________________________________________________
@app.route("/traitement", methods=["GET"])
def traitement(): 
    if request.method == "GET": 
    
        # REQUEST FORMS ARGUMENTS 
        donnees = request.args
        nom = request.args['name']
        mdp = request.args['password']
        
        
        # PRINT ON TERMINAL SCREAN 
        print('Donnees reçues : ', donnees) # all parameters in Browser URL 
        print('Nom : ', nom) # param1
        print('MDP : ', mdp) # param2  
            
        '''

        ON CHROME TYPE FOLLOWING URL 
        http://192.168.2.147:8080/traitement?name=Username2&password=my_password 
        
            
        RESULT ON TERMINAL  
            ImmutableMultiDict([('name', 'Username2'), ('password', 'my_password')])
            Username2 # param1
            my_password # param2 
  
        '''
        '''
            print(request.view_args) # CODE
            
            # RESULTATS DES TESTS 
            # VISUAL CODE   -->     127.0.0.1 - - [13/May/2024 13:09:29] "GET /traitement?name=User1&password=erterqeweqwewqe HTTP/1.1" 200 - 
            # OUTILS CHROME -->     traitement?name=User1&password=erterqeweqwewqe	     
        '''             
              
        if nom == "ADMIN-ABC" and mdp == 'admin1admin1':
            return render_template("traitement.html", nom_utilisateur=nom) 
        else: 
            return render_template("traitement.html")    
    else: # FOR METHODE POST
       return redirect(url_for('erreur')) 
    
    
#______________________________________________________________________
# LAUNCH SERVER 
#______________________________________________________________________   
if __name__ == '__main__': 
    #app.run(debug=True) # Running on http://127.0.0.1:5000
    app.run(host='0.0.0.0', port=8080, debug=True)
    
    
# SERVER LAUNCHING 
# python app_login.py
'''
    * Serving Flask app 'mon_app'
    * Debug mode: on
    * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
'''


#TESTS (CHROME)
'''
    1) HOME                                 : http://192.168.2.147:8080/ 
    2) LOGIN                                : http://192.168.2.147:8080/login (LIEN DE HOME )
    3) BUTTON SEND (FORM)                   : http://192.168.2.147:8080/traitement 
    2) Rafraichir page de traitement        : http://192.168.2.147:8080/erreur (REDIRECTION -> TRAITEMENT D'ERREUR AUCUNE DONNEE ENVOYEE)

'''
