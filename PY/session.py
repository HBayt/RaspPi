from flask import Flask, render_template, request, redirect, url_for, session
import datetime
from random import randint
import ctypes



app = Flask(__name__)
app.secret_key = "32fd6889e4848f91d1ec7e00c97463c3293b45a2d731c176dcf6139def3e32c7"

#__________________________________________________________
# ROUTE - HOME 
#__________________________________________________________
@app.route("/")
def welcome(): 
    # return redirect(url_for('login')) 
    return render_template("index.html")


@app.route("/index_ch")
def index_ch(): 
    return render_template("index_ch.html")

#______________________________________________________
# ROUTE - nav_session 
#______________________________________________________
@app.route("/navs_session")
def barrenav():
    return render_template("navs_session.html")


#__________________________________________________________
# ROUTE - erreur.html 
#__________________________________________________________
@app.route("/erreur")
def erreur():
    return render_template("erreur.html")

#__________________________________________________________
# ROUTE - LOGIN 
'''
Fonction login :
- Affiche le formulaire 
- Traite les données du formulaire 
'''
#__________________________________________________________

utilisateurs = [
    {"nom": "admin", "courriel": "admin@mail.com", "mdp": "1234"},
    {"nom": "Paul",  "courriel": "paul@mail.com", "mdp": "1234"},
    {"nom": "Marie",  "courriel": "marie@mail.com", "mdp": "1234"},
    
]

def recherche_utilisateur( mot_de_passe, adresse_mail): 
    for utilisateur in utilisateurs: 
        #  if utilisateur['nom'] == nom_utilisateur and 
        if utilisateur['mdp'] == mot_de_passe and utilisateur['courriel'] == adresse_mail: 
            return utilisateur
    return None 
#______________________________________________________

@app.route("/login", methods=["POST", "GET"])
def login(): 
    if request.method == "POST": 
    
        # Get form's datas (e-mail, password, radio_btn_value)
        donnees = request.form
        
        # Filter data into variables 
        form_courriel = donnees.get('in_courriel')
        form_mdp = donnees.get('in_mdp')
        form_souvenir = donnees.get('radio_souvenir')
        
        # Look for user, who wants to connect 
        utilisateur = recherche_utilisateur(form_mdp, form_courriel)
        print("user : ", utilisateur)
        
        # Control datas in the Terminal 
        # print("Donnees POST : ", donnees) # TEST DU DONNES DES FORMULAIRE (REQUEST get)
        # print("Donnees POST/FORM", form_courriel, form_mdp, form_souvenir) # AFFICHE VALEURS SAISIES DANS FORMULAIRE 
        
        if form_souvenir == 'remember-me' and utilisateur is not None :
            # return render_template("login.html", nom_utilisateur=nom) 
            
            # CREATE SESSION AND ADD SESSION'S VARIABLE 
            session['nom_utilisateur'] = utilisateur['nom']
            
             # Control datas in the Terminal 
            print("Utilisateur  trouvé : ", utilisateur['nom']," (", utilisateur['courriel'], ")")           
            print("Session info: ", session)
            
            # USER IS FOUND --> CAN BE REDIRECTED TO HOME PAGE 
            return redirect(url_for('welcome')) 
        else:  
            # print("Utilisateur inconnu") # En réalité : Message Flash utilisable avec Flask 
            
            # USER NOT FOUND  
            return redirect(url_for('erreur'))  
        
    else: #METHOD HTTP-GET OR USER ALREADY CONNECTED, FOR EXAMPLE 
        # TERMINAL CONTROL 
        # print("Session ouverte, utilisateur déjà identifié : ", session)
        
        # USER ALREADY CONNECTED AND ATTRIBUTED TO A SESSION 
        if 'nom_utilisateur' in session: 
             return redirect(url_for('welcome')) 
         
        # USER OR SESSION ERRORS
        return render_template("login.html")  #  return redirect(request.url) >>>> IDENTIQUE   
   
   
   
#______________________________________________________
# ROUTE - LOGOUT 
#______________________________________________________
@app.route("/logout")
def logout():
    print(session)
    session.pop('nom_utilisateur', None)
    print(session)
    return redirect(url_for('login')) 
   

#__________________________________________________________
# ROUTE - COMPTEUR DE COOKIES/SESSION  
#__________________________________________________________
@app.route("/compteur")
def compteur(): 
    if "compteur" not in session:
        session['compteur'] = 1
    else: 
        session['compteur'] = session['compteur'] + 1 
        
    print("MA SESSION :", session)
    # return "Nombre de visites"
    # TERMINAL >>>> MA SESSION : <SecureCookieSession {}>
    
    nb_visites = session['compteur'] 
    # return f"Vous avez visité cette page {nb_visites} fois"
    # return render_template("compteur.html")    
    return render_template("compteur.html", visites=nb_visites) 
   
#------------------------------------------------------------------------------------------
 # Route - Jeu du nombre mystère 
 # https://www.youtube.com/watch?v=TZGcVVB6COk&list=PLV1TsfPiCx8PXHsHeJKvSSC8zfi4Kvcfs&index=8
 #------------------------------------------------------------------------------------------ 
 

@app.route("/jeu", methods=["POST", "GET"])
def jeu(): 
    if request.method == "POST": 
        # Manage Form 
        # Get form's datas (number)
        reponse = int(request.form.get('nombre'))
        session['tab_essais'].append(reponse)
        
        if reponse == session['nb']: 
            session["jeu_enCours"] = False # GAME OVER ! (response == session['nb'] )
            msg = "Bravo, vous avez gagné!"
            
            # POPUP WINDOW
            # display = "Bravo! Vous avez gagné! !Le nombre mystère est bien "+str(reponse)
            # ctypes.windll.user32.MessageBoxW(0, display, "Nombre mystère", 0)
        elif reponse < session['nb']: 
            msg = "Non, le nombre mystère est supérieur!" # response > session['nb'] 
        else: 
            msg = "Non, le nombre mystère est inférieur!" # response < session['nb'] 
         
        # session counter - 1 
        session['nb_essais'] = session['nb_essais'] - 1
        
        # If game is ended (you have tried 10 times and not found the mystery number)
        if session['nb_essais'] == 0: 
            session['jeu_enCours'] = False
            msg = "Partie terminée!"
            
        print("Nombre mystère à trouver : ", session['nb'])    
        print("Varibles of current session : ", session)    
        return render_template('nombre-mystere.html', message=msg)   
    else: 
        # The Game is beginning     
           
        n_mystery = randint(0,100) # Generate number 
        session['nb'] = n_mystery # Create session variable nb (mystery number)
        session['jeu_enCours'] = True # Create session variable (Game is ended or is begun)
        session['nb_essais'] = 10 
        session['tab_essais'] = [] # Empty TAB 
        print("Session : ", session) # Display session elements in Terminal (Visual Studio Code)
        return render_template('nombre-mystere.html') # Send answer with instructions and variables to the template 
    
    
    
    '''
    
    Use:

        import ctypes
        ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
        
        The last number (here 1) can be changed to change the window style (not only buttons!):
        ## Button styles:
        # 0 : OK
        # 1 : OK | Cancel
        # 2 : Abort | Retry | Ignore
        # 3 : Yes | No | Cancel
        # 4 : Yes | No
        # 5 : Retry | No
        # 6 : Cancel | Try Again | Continue

        ## To also change icon, add these values to previous number
        # 16 Stop-sign icon
        # 32 Question-mark icon
        # 48 Exclamation-point icon
        # 64 Information-sign icon consisting of an 'i' in a circle
        For example,

        ctypes.windll.user32.MessageBoxW(0, "That's an error", "Warning!", 16)
    
    '''
    
    
   
 #------------------------------------------------------------------------------------------
 # TEMPLATES - Portail suisse 
 #------------------------------------------------------------------------------------------
 

#______________________________________________________
# ROUTE - montagnes.html
#______________________________________________________
@app.route("/montagnes")
def montagnes():
    return render_template("montagnes.html")

#______________________________________________________    
# ROUTE - geographie.html
#______________________________________________________
@app.route("/geographie")
def geographie():
    return render_template("geographie.html")


#______________________________________________________
# ROUTE - art.html
#______________________________________________________
@app.route("/art")
def art():
    return render_template("art.html")

#______________________________________________________   
# ROUTE - culture.html
#______________________________________________________
@app.route("/culture")
def culture():
    return render_template("culture.html")

#______________________________________________________
# ROUTE - economie.html
#______________________________________________________
@app.route("/economie")
def economie():
    return render_template("economie.html")


#______________________________________________________
# ROUTE - education.html
#______________________________________________________
@app.route("/education")
def education():
    return render_template("education.html")

#______________________________________________________
# ROUTE - histoire.html
#______________________________________________________
@app.route("/histoire")
def histoire():
    return render_template("histoire.html")

   

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
    * Running on http://127.0.0.1:8080
    Press CTRL+C to quit
'''

# REFERENCE 
# https://www.youtube.com/watch?v=QAhZ8nmmYxw&t=4s 
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions 