from flask import Flask, render_template, request 
import datetime 


app = Flask(__name__)

#________________________________________________________________
# ROOT (HOME PAGE)
#________________________________________________________________
@app.route("/")
def bonjour():
    return render_template("index.html")
#________________________________________________________________
# Affiche l'heure sur heure.html 
#________________________________________________________________

@app.route("/heure")
def heure(): 
    date_heure = datetime.datetime.now() 
    h = date_heure.hour 
    m = date_heure.minute
    s = date_heure.second 
    # print(h,m,s)
    return render_template("heure.html", heure = h, minute = m , seconde = s)

#________________________________________________________________
# EXECUTE SERVER 
#________________________________________________________________

if __name__ == '__main__': 
    #app.run(debug=True) # Running on http://127.0.0.1:5000
    app.run(host='0.0.0.0', port=8080, debug=True)
    
    
#________________________________________________________________

# URL DU SERVEUR
# http://192.168.2.147:8080/ 
# http://127.0.0.1:8080 
    
# EXECUTION 
'''
1) STOP SERVER      -->  Touches CTRL + c 
2) LANCER SERVER    --> python app_heure.py 
3) 

'''


'''
    * Serving Flask app 'mon_app'
    * Debug mode: on
    * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
'''


