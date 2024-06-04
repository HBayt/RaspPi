from flask import Flask, render_template, request, redirect, url_for, session, flash
from random import randint
from db_eleves import (
    select_eleves,
    insert_eleve,
    select_all,
    select_eleve_by_id,
    update_eleve,
    delete_eleve,
)
from db_authentifications import (
    insert_authentification,
    select_one_authentification,
    select_many_authentifications, 
    select_oneby_mail, 
)

app = Flask(__name__)
"""
app = Flask(__name__) crée un OBJET de TYPE 'application Flask - app'  dans le module Python actuel (Projet actuel). 
Un module Python est un fichier Python, filename.py (.PY). 
Un OBJET (en Python et dans d'autres langages de programmation ORIENTE OBJET) est un TYPE DE DONNEES INCLUANT des fonctions, des méthodes et des attributs ...

"""

# __________________________________________________________
# SESSION KEY
# __________________________________________________________
# Nécessaire pour utiliser les messages flash
app.secret_key = "32fd6889e4848f91d1ec7e00c97463c3293b45a2d731c176dcf6139def3e32c7"


# __________________________________________________________
# ROUTE - HOME
# __________________________________________________________
@app.route("/")
def welcome():
    # return redirect(url_for('login'))
    return render_template("index.html")


@app.route("/index_ch")
def index_ch():
    return render_template("index_ch.html")


@app.route('/posts/<int:post_id>/<slug>')
def show_post(post_id, slug):
    # carry out some processing like
    # retrieval from a database
    return f"Post {post_id} - Slug: {slug}"


"""
#______________________________________________________
# ROUTE - nav_session 
#______________________________________________________
@app.route("/navs_session")
def barrenav():
    return render_template("navs_session.html")

"""


# __________________________________________________________
# ROUTE - erreur.html
# __________________________________________________________
@app.route("/erreur")
def erreur():
    return render_template("erreur.html")


# __________________________________________________________
# ROUTE - LOGIN
"""
Fonction login :
- Affiche le formulaire 
- Traite les données du formulaire 
"""
# __________________________________________________________

utilisateurs = [
    {"nom": "admin", "courriel": "admin@mail.com", "mdp": "1234"},
    {"nom": "Paul", "courriel": "paul@mail.com", "mdp": "1234"},
    {"nom": "Marie", "courriel": "marie@mail.com", "mdp": "1234"},
]


def recherche_utilisateurs(mot_de_passe, adresse_mail):
    for utilisateur in utilisateurs:
        #  if utilisateur['nom'] == nom_utilisateur and
        if (
            utilisateur["mdp"] == mot_de_passe
            and utilisateur["courriel"] == adresse_mail
        ):
            return utilisateur
    return None


# __________________________________________________________
# ROUTE - LOGIN
# __________________________________________________________


@app.route("/login", methods=["POST", "GET"])
def login():

    # Si requete POST -> Récupération des données
    if request.method == "POST":

        # Get form's datas (e-mail, password, radio_btn_value)
        donnees = request.form

        if donnees is not None:
            post_mail = donnees.get("in_courriel")  # Filter data into variable
            post_mdp = donnees.get("in_mdp")  # Filter data into variable
            post_action = donnees.get("rd_login")

            # DISPLAY AND CONTROL DATAT IN THE VS CODE TERMINAL
            print(
                "Donnees POST : ", donnees
            )  # TEST DU DONNES DES FORMULAIRE (REQUEST get)
            # print("mail: ", post_mail, "mdp : ", post_mdp, "bt_radio_value : ", post_action) # AFFICHE VALEURS SAISIES DANS FORMULAIRE
            
                 
            # IF Utilisateur Veut s'authentifier (login.html / Connexion)
            if str(post_action) == str("val_authentification"):
                
                # Chercher l'utilisateur dans BDD            
                utilisateur = select_one_authentification(post_mail, post_mdp)       
                #print("User to authenticate : ", utilisateur) # User to authenticate :  [('teacher@ecole.ch', 'teacher', 'TEACHER')]      
                
                # Utilisateur pas trouvé
                if utilisateur == []:
                    # AFFICHER MESSAGE D'ERREUR DANS PAGE login.html
                    msg = "Authentification impossible."
                    return render_template(
                        "login.html", message=msg
                    )  # Rediriger USER vers PAGE LOGIN (TRY AGAIN)
                # IF Utilisateur trouvé
                else:
                    for donnee in utilisateur:
                        sql_mail = donnee[0]
                        sql_mdp = donnee[1]
                        sql_role = donnee[2]
                        """
                            print("mail : ", donnee[0])
                            print("mdp : ", donnee[1])
                            print("Role : ", donnee[2])                
                        """

                    # Ouvrir session
                    session["session_user"] = utilisateur[0][0]  # == sql_mail
                    session["session_role"] = sql_role  # == utilisateur[0][2]
                    # print("session user : ", session['session_user'] , "session user role : ", session['session_role'] )

                    # AFFICHER BOUTON DANS BARRE DE MENUS
                    return render_template(
                        "index.html"
                    )  # Rediriger USER vers PAGE ACCEUIL

            # IF Utilisateur veut s'inscrire (= NEW USER)

            if str(post_action) == str("val_inscription"):
                # Chercher l'utilisateur dans BDD            
                utilisateur = select_oneby_mail(post_mail)  
                #print("User to authenticate : ", utilisateur) # User to authenticate :  [('teacher@ecole.ch', 'teacher', 'TEACHER')]       
                # print("Mail of user  : ", utilisateur[0][0]) # User to authenticate :  [('teacher@ecole.ch', 'teacher', 'TEACHER')]  
            

                # # Vérifie si l'utilisateur est déjà enregistré >>> Chercher l'utilisateur dans BDD
                if utilisateur != []:
                    print("utilisateur not null / val_inscription : ", utilisateur ) 
                    msg = "L'utilisateur est déjà enregistré."
                    return render_template("login.html", message=msg)
                else:
                    print("utilisateur null / val_inscription : ", utilisateur ) # print("utilisateur : ", utilisateur, "", utilisateur[0][0])
                    # Enregistrer USER dans la BDD
                    user = {"mail": post_mail,
                            "mdp": post_mdp, "role": "NEW USER"}

                    insert_authentification(user)

                    # Ouvrir session
                    session["session_user"] = user["mail"]
                    session["session_role"] = "NEW ELEVE"
                    print(
                        "session user : ",
                        session["session_user"],
                        "session user role : ",
                        session["session_role"],
                    )

                    # Rediriger USER vers PAGE ACCEUIL
                    return render_template(
                        "index.html"
                    )  # Rediriger USER vers PAGE ACCEUIL

    return render_template("login.html")

# ______________________________________________________
# ROUTE - LOGOUT
# ______________________________________________________
@app.route("/logout")
def logout():
    print(session)
    session.pop("session_user", None)
    print(session)
    return redirect(url_for("welcome"))


# ______________________________________________________
# ROUTE - insert_eleve
# ______________________________________________________
@app.route("/register", methods=["GET", "POST"])
def register():

    msg = "" if request.method == "GET" else None

    # Si requete POST -> Récupération des données
    if request.method == "POST":

        # Get form's datas (e-mail, password, radio_btn_value)
        donnees = request.form

        # prenom = request.form['first_name']
        # nom = request.form['last_name']

        if donnees is not None:
            prenom = donnees.get("first_name")  # Filter data into variable
            nom = donnees.get("last_name")
            age = donnees.get("age")
            classe = donnees.get("classe")

            eleve = []
            eleve.append(nom)
            eleve.append(prenom)
            eleve.append(age)
            eleve.append(classe)

            insert_eleve(eleve)

            # AFFICHER MESSAGE D'ERREUR DANS PAGE login.html
            msg = "Eleve enregistré."

        else:
            msg = "Erreur d'insertion."

    return render_template(
        "register.html", message=msg
    )  # Rediriger USER vers PAGE LOGIN (TRY AGAIN)


# ______________________________________________________
# ROUTE - Liste des eleves
# ______________________________________________________
@app.route("/eleves")
def eleves():
    students = select_all()
    # print("Route eleves : ", students)

    return render_template("eleves.html", students=students)


# ______________________________________________________
# ROUTE - Update des eleves
# ______________________________________________________
@app.route("/delete/<int:student_id>", methods=["GET", "POST"])
def delete(student_id):

    print("Student Id (app.py) : ", student_id)

    student = select_eleve_by_id(student_id)
    delete_eleve(student_id)

    '''
    a = 3
    message = "message {} message continues".format(a)  # Using the format method
    message = f"message {a} message continues"  # Using f-strings (Python >= 3.6)
    message = "message %d message continues" % (a)  # % Formatting
    message = "message " + str(a) + " message continues"  # Concatenation
    flash(message)
    '''
    msg = f"Elève {student[1]} {student[2]} supprimé avec succès ...!"
    flash(msg, 'success')
    # return render_template("eleves.html", message=msg)
    # return redirect(url_for("eleves", message=msg))
    return redirect(url_for("eleves"))


# ______________________________________________________
# ROUTE - Update des eleves
# ______________________________________________________
@app.route("/update/<int:student_id>", methods=["GET", "POST"])
def update(student_id):

    if request.method == "POST":

        # Get form's datas (e-mail, password, radio_btn_value)
        donnees = request.form
        print("Donnee : ", donnees)

        # prenom = request.form['first_name']
        # nom = request.form['last_name']

        # eleve_id = request.form['eleve_id']
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        age = request.form["age"]
        class_name = request.form["class"]

        update_eleve(last_name, first_name, age, class_name, student_id)

        '''
        a = 3
        message = "message {} message continues".format(a)  # Using the format method
        message = f"message {a} message continues"  # Using f-strings (Python >= 3.6)
        message = "message %d message continues" % (a)  # % Formatting
        message = "message " + str(a) + " message continues"  # Concatenation
        flash(message)
        '''
        msg = f"Elève {first_name} {last_name} mis à jour avec succès ...!"
        flash(msg, 'success')
        # return render_template("eleves.html", message=msg)
        # return redirect(url_for("eleves", message=msg))
        return redirect(url_for("eleves"))

        return redirect(url_for("eleves"))
    else:
        student = select_eleve_by_id(student_id)
        return render_template("update.html", student=student)


# __________________________________________________________
# ROUTE - COMPTEUR DE COOKIES/SESSION
# __________________________________________________________
@app.route("/compteur")
def compteur():
    if "compteur" not in session:
        session["compteur"] = 1
    else:
        session["compteur"] = session["compteur"] + 1

    print("MA SESSION :", session)
    # return "Nombre de visites"
    # TERMINAL >>>> MA SESSION : <SecureCookieSession {}>

    nb_visites = session["compteur"]
    # return f"Vous avez visité cette page {nb_visites} fois"
    # return render_template("compteur.html")
    return render_template("compteur.html", visites=nb_visites)


# ------------------------------------------------------------------------------------------
# Route - Jeu du nombre mystère
# https://www.youtube.com/watch?v=TZGcVVB6COk&list=PLV1TsfPiCx8PXHsHeJKvSSC8zfi4Kvcfs&index=8
# ------------------------------------------------------------------------------------------


@app.route("/jeu", methods=["POST", "GET"])
def jeu():
    if request.method == "POST":
        # Manage Form
        # Get form's datas (number)
        reponse = int(request.form.get("nombre"))
        session["tab_essais"].append(reponse)

        if reponse == session["nb"]:
            # GAME OVER ! (response == session['nb'] )
            session["jeu_enCours"] = False
            msg = "Bravo, vous avez gagné!"

            # POPUP WINDOW
            # display = "Bravo! Vous avez gagné! !Le nombre mystère est bien "+str(reponse)
            # ctypes.windll.user32.MessageBoxW(0, display, "Nombre mystère", 0)
        elif reponse < session["nb"]:
            # response > session['nb']
            msg = "Non, le nombre mystère est supérieur!"
        else:
            # response < session['nb']
            msg = "Non, le nombre mystère est inférieur!"

        # session counter - 1
        session["nb_essais"] = session["nb_essais"] - 1

        # If game is ended (you have tried 10 times and not found the mystery number)
        if session["nb_essais"] == 0:
            session["jeu_enCours"] = False
            msg = "Partie terminée!"

        print("Nombre mystère à trouver : ", session["nb"])
        print("Varibles of current session : ", session)
        return render_template("nombre-mystere.html", message=msg)
    else:
        # The Game is beginning

        n_mystery = randint(0, 100)  # Generate number
        # Create session variable nb (mystery number)
        session["nb"] = n_mystery
        session["jeu_enCours"] = (
            True  # Create session variable (Game is ended or is begun)
        )
        session["nb_essais"] = 10
        session["tab_essais"] = []  # Empty TAB
        print(
            "Session : ", session
        )  # Display session elements in Terminal (Visual Studio Code)
        return render_template(
            "nombre-mystere.html"
        )  # Send answer with instructions and variables to the template

    """
    
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
    
    """


# ________________________________________________________________
# Route - eleves
# ________________________________________________________________
@app.route("/recherche", methods=["GET", "POST"])
def recherche():

    if request.method == "POST":
        # Si le formulaie est envoyé
        donnees = request.form
        print(donnees)  # TEST 1
        eleve_nom = donnees.get("elevenom")
        # liste_eleves = select_eleves_par_nom(eleve_nom)
        liste_eleves = select_eleves(eleve_nom)
        print(liste_eleves)  # TEST 2
    else:
        # Methode GET
        liste_eleves = None

        # pass # Commande si ELSE vide (Empty)

    return render_template("recherche.html", eleves=liste_eleves)


# ------------------------------------------------------------------------------------------
# TEMPLATES - Portail suisse
# ------------------------------------------------------------------------------------------


# ______________________________________________________
# ROUTE - montagnes.html
# ______________________________________________________
@app.route("/montagnes")
def montagnes():
    return render_template("montagnes.html")


# ______________________________________________________
# ROUTE - geographie.html
# ______________________________________________________
@app.route("/geographie")
def geographie():
    return render_template("geographie.html")


# ______________________________________________________
# ROUTE - art.html
# ______________________________________________________
@app.route("/art")
def art():
    return render_template("art.html")


# ______________________________________________________
# ROUTE - culture.html
# ______________________________________________________
@app.route("/culture")
def culture():
    return render_template("culture.html")


# ______________________________________________________
# ROUTE - economie.html
# ______________________________________________________
@app.route("/economie")
def economie():
    return render_template("economie.html")


# ______________________________________________________
# ROUTE - education.html
# ______________________________________________________
@app.route("/education")
def education():
    return render_template("education.html")


# ______________________________________________________
# ROUTE - histoire.html
# ______________________________________________________
@app.route("/histoire")
def histoire():
    return render_template("histoire.html")


# __________________________________________________________
# EXECUTE SERVEUR --> SEE console & browser to test.
# __________________________________________________________
if __name__ == "__main__":
    app.run(debug=True)  # LOCALHOST: http://127.0.0.1:5000

    # app.run(host='192.168.2.147', port=8080, debug=True) # BATTEN.
    # app.run(host='172.20.10.3', port=8080, debug=True)  # HOME
    # app.run(host='0.0.0.0', port=8080, debug=True) # EVERYWHERE

    """
    http://192.168.2.147:8080/
    http://127.0.0.1:8080/ 
    
    
    """


# EXECUTION
"""
    * Serving Flask app 'mon_app'
    * Debug mode: on
    * Running on http://127.0.0.1:8080
    Press CTRL+C to quit
"""

# REFERENCE
# https://www.youtube.com/watch?v=QAhZ8nmmYxw&t=4s
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions
