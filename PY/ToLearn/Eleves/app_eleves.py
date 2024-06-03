from flask import Flask, render_template, request 
import datetime 


app = Flask(__name__)

#________________________________________________________________
# ROOT (HOME PAGE)
#________________________________________________________________
@app.route("/")
def bonjour():
    return render_template("index_eleves.html")

#________________________________________________________________
# LOGIN 
#________________________________________________________________
# LOGIN 
@app.route("/login")
def login(): 
    return render_template("login.html") 

#________________________________________________________________
# LIST liste_eleves
#________________________________________________________________
liste_eleves = [
    {'nom':'Dupont', 'prenom':'Jean','classe':'2A'}, 
    {'nom':'Martin', 'prenom':'Jeanne','classe':'TG2'}, 
    {'nom':'Ford', 'prenom':'Marie','classe':'2A' }, 
    {'nom':'Marchand', 'prenom':'Adeline','classe':'IG1'}, 
    {'nom':'Martin', 'prenom':'Lucas','classe':'TG2'}, 
    {'nom':'Dubois', 'prenom':'Melanie','classe':'2A'} 
]

#________________________________________________________________
 # REQUEST ALL PARAMETERES 
#________________________________________________________________
@app.route("/eleves") # http://192.168.2.147:8080/eleves?classe=IG1 
def eleves(): 
    classe = request.args.get('classe')
    if classe: 
        eleves_selectionnes = [eleve for eleve in liste_eleves if eleve['classe'] == classe]
    else: 
        eleves_selectionnes = [] 
        
    # EXCETION  FOR GET THE ELEVES LIST 
    # http://192.168.2.147:8080/eleves?classe=IG1
    
    
    #________________________________________________________________
    # TESTS TO UNDERSTAND THE APP (PYTHON)
    #________________________________________________________________ 
    
    '''
        # REQUEST PARAMETER 'classe'
        classe = request.args['classe'] # ERROR IF KEY DOES NOT EXIST 
        classe = request.args.get('classe') # NO ERROR EVEN KEY DOES NOT EXIST 
      
        print(classe) # INSTRUCTION FOR TERMINAL          

    # PRINT RESULTS  
    print(request.args) # all parameters in Browser URL 
    print(request.args['param1']) # param1
    print(request.args['param2']) # param2    
    
    
    # TEST WITH URL IN BROWSER 
    # http://127.0.0.1:8080/eleves?param1=2A&param2=Martin
    
        
    # RESULT IN VISUAL STUDIO CODE IDE      
    ImmutableMultiDict([('param1', '2A'), ('param2', 'Martin')])
    2A
    Martin
    
    '''
    
    
    return render_template("eleves_liste.html", eleves=eleves_selectionnes)  # SEND PARAMS TO eleves_liste.html 




#________________________________________________________________
# # SERVER EXECUTION 
#________________________________________________________________

if __name__ == '__main__': 
    #app.run(debug=True) # Running on http://127.0.0.1:5000
    app.run(host='0.0.0.0', port=8080, debug=True)
    
 
#________________________________________________________________   
# SERVER EXECUTION RESULT
#________________________________________________________________
'''
 * Serving Flask app 'mon_app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit

'''
