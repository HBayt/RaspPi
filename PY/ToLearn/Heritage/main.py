from flask import Flask, render_template



app = Flask(__name__)


# ACTIVATE VENV     -->         venv\Scripts\activate   
# STOP SERVER       --->        CTRL + C 
# LAUNCH SERVER     -->         python main.py 



#______________________________________________________
# ROUTE - HOME 
#______________________________________________________
@app.route("/")
def welcome():
    return render_template("index.html")

#______________________________________________________
# ROUTE - HOME 
#______________________________________________________
@app.route("/nav")
def barrenav():
    return render_template("nav.html")



#______________________________________________________
# ROUTE - erreur.html 
#______________________________________________________
@app.route("/erreur")
def erreur():
    return render_template("erreur.html")

#______________________________________________________
# ROUTE - LOGIN 
#______________________________________________________
@app.route("/login")
def login(): 
    return render_template("login.html") 


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
# ROUTE - montagnes.html
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


################################################################################
# NOT EXIST FILES 
################################################################################

#______________________________________________________
# ROUTE - faq.html
#______________________________________________________
@app.route("/faq")
def faq():
    return render_template("faq.html")

#______________________________________________________
# ROUTE - contact.html
#______________________________________________________
@app.route("/contact")
def contact():
    return render_template("contact.html")

#______________________________________________________
# ROUTE - administration.html
#______________________________________________________
@app.route("/administration")
def administration():
    return render_template("administration.html")

#______________________________________________________
# ROUTE - usercompte.html
#______________________________________________________
@app.route("/usercompte")
def usercompte():
    return render_template("usercompte.html")

#______________________________________________________
# ROUTE - apropos.html
#______________________________________________________
@app.route("/apropos")
def apropos():
    return render_template("apropos.html")

#______________________________________________________
# LAUNCH SERVER 
#______________________________________________________
if __name__ == '__main__': 
    #app.run(debug=True) # Running on http://127.0.0.1:5000
    app.run(host='0.0.0.0', port=8080, debug=True)
    
    
# SERVER IN EXECUTION 
'''
    * Serving Flask app 'mon_app'
    * Debug mode: on
    * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
'''
