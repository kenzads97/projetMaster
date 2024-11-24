from connexion_db import db_connxion
import sys
from flask_bootstrap import Bootstrap
from psycopg2 import extensions
import psycopg2.errorcodes
from flask import Flask, flash, redirect, render_template, request, session, abort,current_app, g, url_for
from werkzeug.security import check_password_hash, generate_password_hash
import os
import re
import psycopg2
from dateutil.relativedelta import relativedelta
from datetime import datetime
from datetime import date
from flask_mail import Mail
from flask_mail import Message
from config import config
import smtplib

#configure the app
app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'kds781228@gmail.com'
app.config['MAIL_PASSWORD'] = 'ynnpkyyfpzsirwis'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
MAIL_DEFAULT_SENDER : ('flask mailer','fausseadr@homail.com')

mail = Mail(app)
#main page
@app.route("/")
def index():
 return render_template('index.html')
@app.route("/se_deconnecter")
def se_deconnecter ():
    flash('Vous etes maintenant deconnecte')
    return render_template('index.html')

@app.route("/se_deconnecterr")
def se_deconnecterr ():
    flash('Vous etes maintenant deconnecte')
    return render_template('index.html')

@app.route("/se_deconnecters")
def se_deconnecteri ():
    flash('Vous etes maintenant deconnecte')
    return render_template('index.html')

# connexion auto 
@app.route("/connexion_auto")
def connxionauto():
 return render_template('connexion_auto.html')

@app.route("/aide")
def aide():
 return render_template('aide.html')

@app.route("/connexion_com")
def connxioncom():
 return render_template('connexion_com.html')

@app.route("/connexion_irdt")
def connxionirdt():
 return render_template('connexion_irdt.html')

@app.route("/inscription_auto")
def inscriptionauto():
 return render_template('inscription_auto.html')

@app.route("/inscription_com")
def inscriptioncom():
 return render_template('inscription_com.html')

@app.route("/inscription_irdt")
def inscriptionirdt():
 return render_template('inscription_irdt.html')

@app.route("/production")
def serviceproduction():
 return render_template('production.html', session = session['nom'],session2= session['mail'] )


@app.route("/sinistre")
def servicesinistre():
 return render_template('sinistre.html', session = session['nom'] ,session2= session['mail'] )


@app.route("/Rsimple")
def servicersimple():
 return render_template('Rsimple.html', session = session['nom'],session2= session['mail']  )


@app.route("/transport")
def servicetransport():
 return render_template('transport.html', session = session['nom'],session2= session['mail']  )



@app.route("/espaceagentirdt")
def retourespaceagentirdt():
    db =db_connxion.get_cnn()
    datenow = date.today()
    cura1 = db.cursor()
    cura3 = db.cursor()   
    usera1 = cura1.execute("""select * from message_irdt order by 4 DESC""")
    resultat1 = cura1.fetchall()
    usera3 = cura3.execute("""select count(id_msgirdt)  from message_irdt  where date = %s """,(datenow,))
    resultat3 = cura3.fetchone()
    return render_template('espaceagentirdt.html', session = session['nom'],  resultat11 =resultat3,resultat = resultat1,session2= session['mail']  )


@app.route("/espaceegentauto")
def retourespaceegentauto():
    db =db_connxion.get_cnn()
    datenow = date.today()
    cura1 = db.cursor()
    cura3 = db.cursor()
    usera1 = cura1.execute("""select * from message_auto order by 4 DESC""")
    resultat1 = cura1.fetchall()
    usera3 = cura3.execute("""select count(id_msgauto)  from message_auto  where date = %s """,(datenow,))
    resultat3 = cura3.fetchone()
    return render_template('espaceegentauto.html', session = session['nom'], resultat11 =resultat3,resultat = resultat1,session2= session['mail'] )

@app.route("/agricole")
def serviceagricole():
 return render_template('agricole.html', session = session['nom'],session2= session['mail'] )

@app.route("/formeetatautorecapgaran")
def formeetatautorecapgaran():
 return render_template('formeetatautorecapgaran.html', session = session['nom'] ,session2= session['mail'])


@app.route("/formetatautores")
def formetatautores():
 return render_template('formetatautores.html', session = session['nom'] ,session2= session['mail'])

@app.route("/formetatautoprodgeneprimenbre")
def formetatautoprodgeneprimenbre():
 return render_template('formetatautoprodgeneprimenbre.html', session = session['nom'],session2= session['mail'] )


@app.route("/formeautopourchaquegara")
def formeautopourchaquegara():
 return render_template('formeautopourchaquegara.html', session = session['nom'],session2= session['mail'] )

@app.route("/formeetatautosinistrmatshmoi")
def formeetatautosinistrmatshmoi():
 return render_template('formeetatautosinistrmatshmoi.html', session = session['nom'],session2= session['mail'] )

@app.route("/formeetatcomdecade")
def formeetatcomdecade():
 return render_template('formeetatcomdecade.html', session = session['nom'] ,session2= session['mail'])


@app.route("/formecomdecadetoutlesagen")
def formecomdecadetoutlesagen():
 return render_template('formecomdecadetoutlesagen.html', session = session['nom'] ,session2= session['mail'])

@app.route("/formedecadepourlesagencedirecte")
def formedecadepourlesagencedirecte():
 return render_template('formedecadepourlesagencedirecte.html', session = session['nom'],session2= session['mail'] )

@app.route("/formedecadepourlesagencesprivé")
def formedecadepourlesagencesprivé():
 return render_template('formedecadepourlesagencesprivé.html', session = session['nom'] ,session2= session['mail'])

@app.route("/formedecadepourlesbanquesass")
def formedecadepourlesbanquesass():
 return render_template('formedecadepourlesbanquesass.html', session = session['nom'] ,session2= session['mail'])

@app.route("/formecomdecadegeneralenbrecont")
def formecomdecadegeneralenbrecont():
 return render_template('formecomdecadegeneralenbrecont.html', session = session['nom'],session2= session['mail'] )

@app.route("/formecomdecadegeneraleenprime")
def formecomdecadegeneraleenprime():
 return render_template('formecomdecadegeneraleenprime.html', session = session['nom'] ,session2= session['mail'])

@app.route("/formecomcomparatifderealisationparagence")
def formecomcomparatifderealisationparagence():
 return render_template('formecomcomparatifderealisationparagence.html', session = session['nom'],session2= session['mail'] )

@app.route("/formerdcomparatifrppparproduit")
def formerdcomparatifrppparproduit():
 return render_template('formerdcomparatifrppparproduit.html', session = session['nom'],session2= session['mail'] )

@app.route("/formerdcomparatifrppparagence")
def formerdcomparatifrppparagence():
 return render_template('formerdcomparatifrppparagence.html', session = session['nom'],session2= session['mail'] )

@app.route("/formecomcomparatifderealisationparabranche")
def formecomcomparatifderealisationparabranche():
 return render_template('formecomcomparatifderealisationparabranche.html', session = session['nom'],session2= session['mail'] )

@app.route("/formeagricoleagenceproduit")
def formeagricoleagenceproduit():
 return render_template('formeagricoleagenceproduit.html', session = session['nom'] ,session2= session['mail'])

@app.route("/formeetatagricoleproductionmensuelle")
def formeetatagricoleproductionmensuelle():
 return render_template('formeetatagricoleproductionmensuelle.html', session = session['nom'] ,session2= session['mail'])

@app.route("/formetransportetatassurance")
def formetransportetatassurance():
 return render_template('formetransportetatassurance.html', session = session['nom'],session2= session['mail'] )

@app.route("/formetransportetatprodmensuelle")
def formetransportetatprodmensuelle():
 return render_template('formetransportetatprodmensuelle.html', session = session['nom'],session2= session['mail'] )

@app.route("/formeagricolereacapeannuelle")
def formeagricolereacapeannuelle():
 return render_template('formeagricolereacapeannuelle.html', session = session['nom'],session2= session['mail'] )

@app.route("/formetransportrecapeparproduit")
def formetransportrecapeparproduit():
 return render_template('formetransportrecapeparproduit.html', session = session['nom'],session2= session['mail'] )

@app.route("/formeetatautosinistrematahmoi")
def formeetatautosinistrematahmoi():
 return render_template('formeetatautosinistrematahmoi.html', session = session['nom'],session2= session['mail'] )

@app.route("/formeetatautosinstrecorp")
def formeetatautosinstrecorp():
 return render_template('formeetatautosinstrecorp.html', session = session['nom'],session2= session['mail'] )

@app.route("/formulaire_send_auto")
def formulaire_send_auto():
 return render_template('formulaire_send_auto.html', session = session['nom'],session2= session['mail'] )
@app.route("/formulaire_send_com")
def formulaire_send_com():
 return render_template('formulaire_send_com.html', session = session['nom'] ,session2= session['mail'] )

@app.route("/formulaire_send_irdt")
def formulaire_send_irdt():
 return render_template('formulaire_send_irdt.html', session = session['nom'],session2= session['mail']  )


@app.route("/modifiermotdepasse")
def modimodepas():
    return render_template('modifiermotdepasse.html', session = session['nom'],session2= session['mail'])

@app.route("/formemoddifiermotdepasseirdt")
def formemoddifiermotdepasseirdt():
    return render_template('formemoddifiermotdepasseirdt.html', session = session['nom'],session2= session['mail'])

@app.route("/modifierprofil")
def modipro():
  error = None
  db = db_connxion.get_cnn()
  cu = db.cursor()
  us = cu.execute("""select nom,email from user_auto where nom = %s """,(session['nom'],))
  res = cu.fetchone()
  if error is None :
    return render_template('modifierprofil.html', session = session['nom'], resultat= res, session2 = session['mail'])

@app.route("/commercial")
def commercial():
    db =db_connxion.get_cnn()
    datenow = date.today()
    decade1 = date(datenow.year, datenow.month, 4)
    decade2 = date(datenow.year, datenow.month, 20)
    decade3 = date(datenow.year, datenow.month, 1) + relativedelta(months=1, days=-1)
    cura1 = db.cursor()
    cura3 = db.cursor()   
    usera1 = cura1.execute("""select * from message_com order by 4 DESC""")
    resultat1 = cura1.fetchall()
    usera3 = cura3.execute("""select count(id_msgcom)  from message_com  where date = %s """,(datenow,))
    resultat3 = cura3.fetchone()
    return render_template('commercial.html', session = session['nom'],session2= session['mail']  ,resultat = resultat1, date1 = datenow,  resultat11 =resultat3,decade1 =decade1,decade2 =decade2,decade3 =decade3)


@app.route("/formemodifierprofilsirdt")
def formemodifierprofilsirdt():
  error = None
  db = db_connxion.get_cnn()
  cu = db.cursor()
  us = cu.execute("""select nom,email from user_irdt where nom = %s """,(session['nom'],))
  res = cu.fetchone()
  if error is None :
    return render_template('formemodifierprofilsirdt.html', session = session['nom'], resultat= res)

@app.route("/modifierprofils",methods=('GET', 'POST'))
def modiprs():
  if request.method == 'POST':
     nommo = request.form['nommo']
     email1 = request.form['email1']
     print(nommo,email1) 
     error = None
     patternuser1 ='^[a-zA-Z0-9]([._](?![._])|[a-zA-Z0-9]){6,18}[a-zA-Z0-9]$'
     exreguser1 = re.match(patternuser1 , nommo)
     db = db_connxion.get_cnn() 
     cu = db.cursor()
     curia2 = db.cursor()
     useria2 = curia2.execute("""select nom,email from user_auto where nom = %s or email =%s""",(nommo,email1,))
     resultia2 = curia2.fetchone()
     print (resultia2)
     
     if resultia2  is not None:
        error ="le nom d'utilisateur ou l'adresse email est déja pris !!!"
     if not exreguser1: 
        error ="veuillez respecter le format du nom d'utilisateur,il Contient uniquement les caractères alphanumérique, soulignement et point, et le nombre de caractères doit avoir au min 6 !!!" 
        
        
     if error is None:     
       us = cu.execute("UPDATE user_auto SET nom = %s, email= %s  where nom=%s",(nommo,email1,session['nom']))
       db.commit()  
       session.clear()
       session['nom'] = nommo
       session['mail'] = email1
       cur1 = db.cursor() 
       us1 = cur1.execute("""select nom, email from user_auto where nom=%s""",(session['nom'],))
       res = cur1.fetchone()
       flash('votre compte a été modifier avec succée')
       return render_template('modifierprofil.html', session = session['nom'], resultat=res, session2= session['mail'])
     return render_template('modifierprofil.html',session = session['nom'], error=error, resultat=resultia2, session2= session['mail'])

@app.route("/modifierprofilsirdt",methods=('GET', 'POST'))
def modiprsirdt():
  if request.method == 'POST':
     nommo = request.form['nommo']
     email1 = request.form['email1']
     print(nommo,email1) 
     error = None
     patternuser1 ='^[a-zA-Z0-9]([._](?![._])|[a-zA-Z0-9]){6,18}[a-zA-Z0-9]$'
     exreguser1 = re.match(patternuser1 , nommo)
     db = db_connxion.get_cnn() 
     cu = db.cursor()
     curia2 = db.cursor()
     useria2 = curia2.execute("""select nom,email from user_irdt where nom = %s or email =%s""",(nommo,email1,))
     resultia2 = curia2.fetchone()
     print (resultia2)
     
     if resultia2  is not None:
        error ="le nom d'utilisateur ou l'adresse email est déja pris !!!"
     if not exreguser1: 
        error ="veuillez respecter le format du nom d'utilisateur,il Contient uniquement les caractères alphanumérique, soulignement et point, et le nombre de caractères doit avoir au min 6 !!!" 
        
        
     if error is None:     
       us = cu.execute("UPDATE user_irdt SET nom = %s, email= %s  where nom=%s",(nommo,email1,session['nom']))
       db.commit()  
       session.clear()
       session['nom'] = nommo
       session['mail'] = email1
       cur1 = db.cursor() 
       us1 = cur1.execute("""select nom, email from user_irdt where nom=%s""",(session['nom'],))
       res = cur1.fetchone()
       flash('votre compte a été modifier avec succée')
       return render_template('formemodifierprofilsirdt.html', session = session['nom'], resultat=res, session2= session['mail'])
     return render_template('formemodifierprofilsirdt.html',session = session['nom'], error=error, resultat=resultia2, session2= session['mail'])



@app.route("/modifiermotdepasses",methods=('GET', 'POST'))
def modimodepass():
    if request.method == 'POST':
      pass1 = request.form['pass1']
      pass2 = request.form['pass2']
      pass3 = request.form['pass3']
      print(pass1,pass2,pass3)
      error = None
      patternpass = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$'
      exregpass = re.match(patternpass , pass2)
      db =db_connxion.get_cnn()
      cu3 = db.cursor()
      curia3 = db.cursor()
      seria3 = curia3.execute("""select mdp from user_auto where nom = %s""",(session['nom'],))
      resul3 = curia3.fetchone()
      if pass1 not in resul3[0]:
        error = "Mot de passe incorrect !!!"
        print(error)
      if pass2 not in  pass3:
            error =" les deux mot de passe ne sont pas compatible!!!"
            print(error)
      elif not exregpass: 
            error ="veuiller respecter le format du mot de passe Huit caractères au moins, au moins une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial(Exemple123* ) !!!"      
            print(error)
      if error is None :
        us3 = cu3.execute("UPDATE user_auto SET mdp = %s where nom=%s",(pass2,session['nom']))
        db.commit()
        flash('votre mot de passe a été modifier avec succée')
        
    return render_template('modifiermotdepasse.html', session = session['nom'], error= error, resultat= resul3,session2 = session['mail'])



@app.route("/modifiermotdepassesirdt",methods=('GET', 'POST'))
def modimodepassirdt():
    if request.method == 'POST':
      pass1 = request.form['pass1']
      pass2 = request.form['pass2']
      pass3 = request.form['pass3']
      print(pass1,pass2,pass3)
      error = None
      patternpass = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$'
      exregpass = re.match(patternpass , pass2)
      db =db_connxion.get_cnn()
      cu3 = db.cursor()
      curia3 = db.cursor()
      seria3 = curia3.execute("""select mdp from user_irdt where nom = %s""",(session['nom'],))
      resul3 = curia3.fetchone()
      if pass1 not in resul3[0]:
        error = "Mot de passe incorrect !!!"
        print(error)
      if pass2 not in  pass3:
            error =" les deux mot de passe ne sont pas compatible!!!"
            print(error)
      elif not exregpass: 
            error ="veuiller respecter le format du mot de passe Huit caractères au moins, au moins une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial(Exemple123* ) !!!"      
            print(error)
      if error is None :
        us3 = cu3.execute("UPDATE user_irdt SET mdp = %s where nom=%s",(pass2,session['nom']))
        db.commit()
        flash('votre mot de passe a été modifier avec succée')
      
    return render_template('formemoddifiermotdepasseirdt.html', session = session['nom'], error= error, resultat= resul3, session2 = session['mail'])

@app.route("/modifierprofilcom")
def modiproc():
  error = None
  db = db_connxion.get_cnn()
  cu = db.cursor()
  us = cu.execute("""select nom,email from user_com where nom = %s """,(session['nom'],))
  res = cu.fetchone()
  if error is None :
    return render_template('modifierprofilcom.html', session = session['nom'], resultat= res,session2 = session['mail'])


@app.route("/modifierprofilss",methods=('GET', 'POST'))
def modiprccoms():
  if request.method == 'POST':
     nommo = request.form['nommo']
     email1 = request.form['email1']
     print(nommo,email1) 
     error = None
     patternuser1 ='^[a-zA-Z0-9]([._](?![._])|[a-zA-Z0-9]){6,18}[a-zA-Z0-9]$'
     exreguser1 = re.match(patternuser1 , nommo)
     db = db_connxion.get_cnn() 
     cu = db.cursor()
     curia2 = db.cursor()
     useria2 = curia2.execute("""select nom,email from user_com where nom = %s or email =%s""",(nommo,email1,))
     resultia2 = curia2.fetchone()
     print (resultia2)
     
     if resultia2  is not None:
        error ="le nom d'utilisateur ou l'adresse email est déja pris !!!"
     if not exreguser1: 
        error ="veuillez respecter le format du nom d'utilisateur,il Contient uniquement les caractères alphanumérique, soulignement et point, et le nombre de caractères doit avoir au min 6 !!!" 
        
        
     if error is None:     
       us = cu.execute("UPDATE user_com SET nom = %s, email= %s  where nom=%s",(nommo,email1,session['nom']))
       db.commit()  
       session.clear()
       session['nom'] = nommo
       session['mail'] = email1
       cur1 = db.cursor() 
       us1 = cur1.execute("""select nom, email from user_com where nom=%s""",(session['nom'],))
       res = cur1.fetchone()
       print("session est ", session['nom'])
       flash('votre compte a été modifier avec succée')
       return render_template('modifierprofilcom.html', session = session['nom'], resultat=res)
     return render_template('modifierprofilcom.html',session = session['nom'], error=error, resultat=resultia2, session2 = session['mail'])


@app.route("/modifiermotdepassecom")
def modimodepascom():
    return render_template('modifiermotdepassecom.html', session = session['nom'])

@app.route("/modifiermotdepassess",methods=('GET', 'POST'))
def modimodepasss():
    if request.method == 'POST':
      pass1 = request.form['pass1']
      pass2 = request.form['pass2']
      pass3 = request.form['pass3']
      print(pass1,pass2,pass3)
      error = None
      patternpass = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$'
      exregpass = re.match(patternpass , pass2)
      db =db_connxion.get_cnn()
      cu3 = db.cursor()
      curia3 = db.cursor()
      seria3 = curia3.execute("""select mdp from user_com where nom = %s""",(session['nom'],))
      resul3 = curia3.fetchone()
      if pass1 not in resul3[0]:
        error = "Mot de passe incorrect !!!"
        print(error)
      if pass2 not in  pass3:
            error =" les deux mot de passe ne sont pas compatible!!!"
            print(error)
      elif not exregpass: 
            error ="veuiller respecter le format du mot de passe Huit caractères au moins, au moins une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial(Exemple123* ) !!!"      
            print(error)
      if error is None :
        us3 = cu3.execute("UPDATE user_com SET mdp = %s where nom=%s",(pass2,session['nom']))
        db.commit()
        flash('votre mot de passe a été modifier avec succée')
      
    return render_template('modifiermotdepassecom.html', session = session['nom'], error= error, resultat= resul3, session2 = session['mail'])





# connexion irdt
@app.route("/espaceagentirdt",methods=('GET', 'POST'))
def loginirdt():
     if request.method == 'POST':
        username = request.form['username']
        password = request.form['pass']
        print (username, password)
        db =db_connxion.get_cnn()
        datenow = date.today()
        cura2 = db.cursor()
        cura2.execute("""select date from message_irdt where date = %s group by 1""",(datenow,))
        resultata2 = cura2.fetchone()
        if resultata2 is None :
            db_connxion.rafrech_irdtmen()
            db_connxion.rafrech_irdtann()
        error = None
        
        cur = db.cursor()
        user = cur.execute("""select * from user_irdt where nom = %s""",(username,))
        result = cur.fetchone()
        cura1 = db.cursor()
        cura3 = db.cursor()   
        usera1 = cura1.execute("""select * from message_irdt order by 4 DESC""")
        resultat1 = cura1.fetchall()
        usera3 = cura3.execute("""select count(id_msgirdt)  from message_irdt  where date = %s """,(datenow,))
        resultat3 = cura3.fetchone()
        print (resultat3)
        if result  is  None:
            error = "Nom d'utilisateur incorrect !!!"
        elif password not in result[2]:
            error = "Mot de passe incorrect !!!"
            print(error)
        
        if error is None:
            session.clear()
            session['nom'] = result[0]
            session['mail'] = result[1]
            return render_template('espaceagentirdt.html',session=session['nom'], session2=session['mail'],resultat = resultat1, date1 = datenow,  resultat11 =resultat3  )
     return render_template('connexion_irdt.html',error =error)
# connexion com        
@app.route("/commercial",methods=('GET', 'POST'))
def logincom():
     if request.method == 'POST':
        username = request.form['usernamecom']
        password = request.form['passcom']
        print (username, password)
        error = None
        db =db_connxion.get_cnn()
        datenow = date.today()
        cura2 = db.cursor()
        curc = db.cursor()
        cura1 = db.cursor()
        cura3 = db.cursor()
        cura2.execute("""select date from message_com where date = %s group by 1""",(datenow,))
        resultata2 = cura2.fetchone()
        if resultata2 is None :
            db_connxion.rafrech_decadecom()
        userc = curc.execute("""select * from user_com where nom = %s""",(username,))
        resultc = curc.fetchone()
        usera1 = cura1.execute("""select * from message_com order by 4 DESC""")
        resultat1 = cura1.fetchall()
        usera3 = cura3.execute("""select count(id_msgcom)  from message_com  where date = %s """,(datenow,))
        resultat3 = cura3.fetchone()
        print (resultat3)
        if resultc  is  None:
            error = "Nom d'utilisateur incorrect !!!"
        elif password not in resultc[2]:
            error = "Mot de passe incorrect !!!"
            print(error)
                    
        
        if error is None:
            session.clear()
            session['nom'] = resultc[0]
            session['mail'] = resultc[1]
            return render_template('commercial.html',session=session['nom'],session2= session['mail'],resultat = resultat1, date1 = datenow,  resultat11 =resultat3)
     return render_template('connexion_com.html',error =error)
# connexion auto 
@app.route("/espaceegentauto",methods=('GET', 'POST'))
def loginauto():
     if request.method == 'POST':
        username = request.form['usernameauto']
        password = request.form['passauto']
        print (username, password)
        db =db_connxion.get_cnn()
        datenow = date.today()
        cura2 = db.cursor()
        cura2.execute("""select date from message_auto where date = %s group by 1""",(datenow,))
        resultata2 = cura2.fetchone()
        if resultata2 is None :
            db_connxion.rafrech_monauto()
        error = None
      
        cura = db.cursor()
        cura1 = db.cursor()
        cura2 = db.cursor()
        cura3 = db.cursor()
        usera = cura.execute("""select * from user_auto where nom = %s""",(username,))
        resulta = cura.fetchone()
        usera = cura.execute("""select * from user_auto where nom = %s""",(username,))
        resulta = cura.fetchone()
        usera1 = cura1.execute("""select * from message_auto order by 4 DESC""")
        resultat1 = cura1.fetchall()
        usera3 = cura3.execute("""select count(id_msgauto)  from message_auto  where date = %s """,(datenow,))
        resultat3 = cura3.fetchone()
        print (resultat3)
        
        if resulta  is  None:
            error = "Nom d'utilisateur incorrect !!!"
        elif password not in resulta[2]:
            error = "Mot de passe incorrect !!!"
            print(error)
        
        if error is None:
            session.clear()
            session['nom'] = resulta[0]
            session['mail'] = resulta[1]
            return render_template('espaceegentauto.html',session=session['nom'],session2= session['mail'], resultat = resultat1, date1 = datenow,  resultat11 =resultat3)
     return render_template('connexion_auto.html',error =error)  
# inscription auto
@app.route("/espaceegentautoo",methods=('GET', 'POST'))
def inscauto():
     if request.method == 'POST':
        username = request.form['inscuserauto']
        email = request.form['inscemailauto']
        password = request.form['mdpauto']
        password2 = request.form['mdpauto2']
        print (username,email, password,password2)
        error = None
        patternuser ='^[a-zA-Z0-9]([._](?![._])|[a-zA-Z0-9]){6,18}[a-zA-Z0-9]$'
        patternpass = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$'
        exreguser = re.match(patternuser , username)
        exregpass = re.match(patternpass , password)
        db =db_connxion.get_cnn()
        curia = db.cursor()
        datenow = date.today()
        cura1 = db.cursor()
        cura3 = db.cursor()
        usera1 = cura1.execute("""select * from message_auto order by 4 DESC""")
        resultat1 = cura1.fetchall()
        usera3 = cura3.execute("""select count(id_msgauto)  from message_auto  where date = %s """,(datenow,))
        resultat3 = cura3.fetchone()
        useria = curia.execute("""select nom,email from user_auto where nom = %s or email =%s""",(username,email,))
        
        resultia = curia.fetchone()
       
        print (resultia)

        if resultia  is not None:
            error ="le nom d'utilisateur ou l'adresse email est deja pris !!!"
            
    

        elif password not in  password2:
            error =" les deux mot de passe ne sont pas compatible!!!"
            
          
        if not exreguser: 
            error ="veuiller respecter le format du nom d'utilisateur Contient uniquement alphanumérique caractères, soulignement et point,Le nombre de caractères avoir au min 6 !!!" 
           

        elif not exregpass: 
            error ="veuiller respecter le format du mot de passe Huit caractères au moins, au moins une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial(Exemple123* ) !!!"    
            
        
           
        if error is None:
            curia.execute("""INSERT INTO user_auto VALUES (%s,%s,%s);""", (username, email, password))
            db.commit()
            session.clear()
            session['nom'] = username
            session['mail'] = email
            print("session est",session['nom'])
            return render_template('espaceegentauto.html',session=session['nom'],resultat11 =resultat3, date1 = datenow,resultat = resultat1,session2= session['mail'])   
             
     return render_template('inscription_auto.html',error=error)    
# inscription com
@app.route("/commerciale",methods=('GET', 'POST'))
def inscom():
     if request.method == 'POST':
        username = request.form['inscuserauto']
        email = request.form['inscemailauto']
        password = request.form['mdpauto']
        password2 = request.form['mdpauto2']
        print (username,email, password,password2)
        error = None
        patternuser ='^[a-zA-Z0-9]([._](?![._])|[a-zA-Z0-9]){6,18}[a-zA-Z0-9]$'
        patternpass = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$'
        exreguser = re.match(patternuser , username)
        exregpass = re.match(patternpass , password)
        db =db_connxion.get_cnn()
        curia = db.cursor()
        datenow = date.today()
        decade1 = date(datenow.year, datenow.month, 4)
        decade2 = date(datenow.year, datenow.month, 20)
        decade3 = date(datenow.year, datenow.month, 1) + relativedelta(months=1, days=-1)
        cura1 = db.cursor()
        cura3 = db.cursor()   
        usera1 = cura1.execute("""select * from message_com order by 4 DESC""")
        resultat1 = cura1.fetchall()
        usera3 = cura3.execute("""select count(id_msgcom)  from message_com  where date = %s """,(datenow,))
        resultat3 = cura3.fetchone()
        useria = curia.execute("""select nom,email from user_com where nom = %s or email =%s""",(username,email,))
        
        resultia = curia.fetchone()
       
        print (resultia)

        if resultia  is not None:
            error ="le nom d'utilisateur ou l'adresse email est deja pris !!!"
            
    

        elif password not in  password2:
            error =" les deux mot de passe ne sont pas compatible!!!"
            
          
        if not exreguser: 
            error ="veuiller respecter le format du nom d'utilisateur Contient uniquement alphanumérique caractères, soulignement et point,Le nombre de caractères avoir au min 6 !!!" 
           

        elif not exregpass: 
            error ="veuiller respecter le format du mot de passe Huit caractères au moins, au moins une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial: Exemple123*  !!!"    
            
        
           
        if error is None:
            curia.execute("""INSERT INTO user_com VALUES (%s,%s,%s);""", (username, email, password))
            db.commit()
            session.clear()
            session['nom'] = username
            session['mail'] = email
            print("session est",session['nom'])
            return render_template('commercial.html',session=session['nom'], date1 = datenow,session2= session['mail'] ,resultat11 =resultat3,resultat = resultat1)   
             
     return render_template('inscription_com.html',error=error,session2= session['mail'] )      
# inscription irdt
@app.route("/espaceagentirdtt",methods=('GET', 'POST'))
def insirdt():
     if request.method == 'POST':
        username = request.form['inscuserauto']
        email = request.form['inscemailauto']
        password = request.form['mdpauto']
        password2 = request.form['mdpauto2']
        print (username,email, password,password2)
        error = None
        patternuser ='^[a-zA-Z0-9]([._](?![._])|[a-zA-Z0-9]){6,18}[a-zA-Z0-9]$'
        patternpass = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$'
        exreguser = re.match(patternuser , username)
        exregpass = re.match(patternpass , password)
        db =db_connxion.get_cnn()
        datenow = date.today()
        cura1 = db.cursor()
        cura3 = db.cursor()   
        usera1 = cura1.execute("""select * from message_irdt order by 4 DESC""")
        resultat1 = cura1.fetchall()
        usera3 = cura3.execute("""select count(id_msgirdt)  from message_irdt  where date = %s """,(datenow,))
        resultat3 = cura3.fetchone()
        curia = db.cursor()
        useria = curia.execute("""select nom,email from user_irdt where nom = %s or email =%s""",(username,email,))
        
        resultia = curia.fetchone()
       
        print (resultia)

        if resultia  is not None:
            error ="le nom d'utilisateur ou l'adresse email est deja pris !!!"
            
    

        elif password not in  password2:
            error =" les deux mot de passe ne sont pas compatible!!!"
            
          
        if not exreguser: 
            error ="veuiller respecter le format du nom d'utilisateur Contient uniquement alphanumérique caractères, soulignement et point,Le nombre de caractères avoir au min 6 !!!" 
           

        elif not exregpass: 
            error ="veuiller respecter le format du mot de passe Huit caractères au moins, au moins une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial: Exemple123*  !!!"    
            
        
           
        if error is None:
            curia.execute("""INSERT INTO user_irdt VALUES (%s,%s,%s);""", (username, email, password))
            db.commit()
            session.clear()
            session['nom'] = username
            session['mail'] = email
            print("session est",session['nom'])
            return render_template('espaceagentirdt.html',session=session['nom'], date1 = datenow,session2= session['mail'] ,resultat11 =resultat3,resultat = resultat1)   
             
     return render_template('inscription_irdt.html',error=error,session2= session['mail'] )     

@app.route("/etatrecappargaraparagen",methods=('GET', 'POST'))
def etatrecappargaraparagen():
     if request.method == 'POST':
        mois = request.form['mois']
        annee = request.form['annee']
        print (mois, annee)
        db =db_connxion.get_cnn()
        error = None
        cur1 = db.cursor()
        cur2 = db.cursor()
        etat1 = cur1.execute("""select  agen.numagen  ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_rc else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_rcarab  else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_rcfront  else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_ro  else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_tr  else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_dasc200000  else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_dasc300000  else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_dasc500000  else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_DC10000 else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_DC20000 else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_DC30000 else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_DC40000 else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_DC50000 else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_DCVV else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_VIV else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_VAR else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_BDG else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_pdga else 0 end) ,
         max(case when cast(p.numagen as integer)= agen.numagen then p.prime_DR else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_assistvehi else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_assisttunis else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_ATES else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_PEA else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_toprep else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then  p.prime_rachat else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then  p.prime_tromb else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_emeut else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_rno  else 0 end) ,
         sum((case when cast(p.numagen as integer)= agen.numagen then p.prime_ro  else 0 end)+
          (case when cast(p.numagen as integer)= agen.numagen then p.prime_rno  else 0 end) ) 
       from  prodpargaraparagen p, agence_saa agen where   mois = %s and annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

        etat2 = cur2.execute("""select sum (prime_rc),sum (prime_rcarab),  sum ( prime_rcfront), sum ( prime_ro) ,sum (prime_tr),sum (prime_dasc200000),
        sum ( prime_dasc300000),sum (prime_dasc500000),sum (prime_DC10000),sum ( prime_DC20000),sum ( prime_DC30000),
        sum ( prime_DC40000),sum ( prime_DC50000),sum (prime_DCVV ),sum ( prime_VIV),sum ( prime_VAR),sum ( prime_BDG),sum ( prime_pdga),
        sum ( prime_DR),sum ( prime_assistvehi),sum ( prime_assisttunis),sum ( prime_ATES),sum ( prime_PEA),sum ( prime_toprep),sum ( prime_rachat),
        sum ( prime_tromb),sum ( prime_emeut), sum ( prime_rno)
            from  prodpargaraparagen  where   mois = %s and annee =%s  """,(mois,annee,))
        result1 = cur1.fetchall()
        result2 = cur2.fetchone()
        print(result1 )
        if result1 == []: 
            error ="l'etat n'est pas disponible  "
            print(error)
        if error is None:

            return render_template('etatrecappargaraparagen.html',session=session['nom'],resultat =result1, resultat2 =result2  ,mois =mois,annee =annee ,session2= session['mail'] )
     return render_template('formeetatautorecapgaran.html',error =error,session=session['nom'],session2= session['mail'] )  


@app.route("/etatautorecapgenerec",methods=('GET', 'POST'))
def etatautorecapgenerec():
     if request.method == 'POST':
        mois = request.form['mois']
        annee = request.form['annee']
        print (mois, annee)
        db =db_connxion.get_cnn()
        error = None
        cur1 = db.cursor()
        cur2 = db.cursor()

        etat1 = cur1.execute("""select  agen.numagen  ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_rc else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_rcarab  else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_rcfront  else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_ro  else 0 end),
         sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_tr  else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_dasc200000  else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_dasc300000  else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_dasc500000  else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_DC10000 else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_DC20000 else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_DC30000 else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_DC40000 else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_DC50000 else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_DCVV else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_VIV else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_VAR else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_BDG else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_pdga else 0 end) ,
         max(case when cast(p.numagen as integer)= agen.numagen then p.rec_DR else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_assistvehi else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_assisttunis else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_ATES else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_PEA else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_toprep else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then  p.rec_rachat else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then  p.rec_tromb else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_emeut else 0 end), 
         sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_rno else 0 end), 
         sum((case when cast(p.numagen as integer)= agen.numagen then p.rec_ro  else 0 end) +
         (case when cast(p.numagen as integer)= agen.numagen then p.rec_rno else 0 end))
        from  prodpargaraparagen p, agence_saa agen where   mois = %s and annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

        etat2 = cur2.execute("""select sum (rec_rc),sum (rec_rcarab),  sum ( rec_rcfront), 
        sum (rec_ro) ,sum (rec_tr),sum (rec_dasc200000),
        sum ( rec_dasc300000),sum (rec_dasc500000),sum (rec_DC10000),sum ( rec_DC20000),sum (rec_DC30000),
        sum ( rec_DC40000),sum ( rec_DC50000),sum (rec_DCVV ),sum (rec_VIV),sum ( rec_VAR),sum ( rec_BDG),sum ( rec_pdga),
        sum ( rec_DR),sum (rec_assistvehi),sum ( rec_assisttunis),sum ( rec_ATES),sum ( rec_PEA),sum (rec_toprep),sum (rec_rachat),
        sum ( rec_tromb),sum (rec_emeut),sum (rec_rno)
        from  prodpargaraparagen  where   mois = %s and annee =%s  """,(mois,annee,))
        result1 = cur1.fetchall()
        result2 = cur2.fetchone()
        print(result1 )
        if result1 == []: 
            error ="l'etat n'est pas disponible "
            print(error)
        if error is None:
            
            return render_template('etatautorecapgenerec.html',session=session['nom'],resultat =result1,resultat2 =result2  ,mois =mois,annee =annee,session2= session['mail']  )
     return render_template('formetatautores.html',error =error,session=session['nom'],session2= session['mail'] )  

@app.route("/etatautoprodgeneprimenbre",methods=('GET', 'POST'))
def etatautoprodgeneprimenbre():
     if request.method == 'POST':
        mois = request.form['mois']
        annee = request.form['annee']
        print (mois, annee)
        db =db_connxion.get_cnn()
        error = None
        cur1 = db.cursor()
        cur2 = db.cursor()
        etat1 = cur1.execute("""select  agen.numagen  ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_rc else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_rcarab  else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_rcfront  else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_ro  else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_tr  else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_dasc200000  else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_dasc300000  else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_dasc500000  else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_DC10000 else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_DC20000 else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_DC30000 else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_DC40000 else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_DC50000 else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_DCVV else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_VIV else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_VAR else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_BDG else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_pdga else 0 end) ,
         max(case when cast(p.numagen as integer)= agen.numagen then p.nombre_DR else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_assistvehi else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_assisttunis else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_ATES else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_PEA else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_toprep else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then  p.nombre_rachat else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then  p.nombre_tromb else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_emeut else 0 end) ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_rno  else 0 end) ,
         sum((case when cast(p.numagen as integer)= agen.numagen then p.nombre_ro  else 0 end) +
         (case when cast(p.numagen as integer)= agen.numagen then p.nombre_rno else 0 end))
       from  prodpargaraparagen p, agence_saa agen where   mois = %s and annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

        etat2 = cur2.execute("""select sum (nombre_rc),sum (nombre_rcarab),  sum ( nombre_rcfront), 
        sum (nombre_ro) ,sum (nombre_tr),sum (nombre_dasc200000),
        sum ( nombre_dasc300000),sum (nombre_dasc500000),sum (nombre_DC10000),sum ( nombre_DC20000),sum (nombre_DC30000),
        sum ( nombre_DC40000),sum ( nombre_DC50000),sum (nombre_DCVV ),sum (nombre_VIV),sum ( nombre_VAR),sum ( nombre_BDG),sum ( nombre_pdga),
        sum (nombre_DR),sum (nombre_assistvehi),sum (nombre_assisttunis),sum ( nombre_ATES),sum ( nombre_PEA),sum (nombre_toprep),sum (nombre_rachat),
        sum ( nombre_tromb),sum (nombre_emeut),sum (nombre_rno) from  prodpargaraparagen  where   mois = %s and annee =%s  """,(mois,annee,))
        result1 = cur1.fetchall()
        result2 = cur2.fetchone()
        print(result1 )
        if result1 == []: 
            error ="l'etat n'est pas disponible  "
            print(error)
        if error is None:

            return render_template('etatautoprodgeneprimenbre.html',session=session['nom'],resultat =result1,resultat2 =result2  ,mois =mois,annee =annee,session2= session['mail']  )
     return render_template('formetatautoprodgeneprimenbre.html',error =error,session=session['nom'],session2= session['mail'] )  

@app.route("/etatstatpourchaquegaraparagen",methods=('GET', 'POST'))
def etatstatpourchaquegaraparagen():
     if request.method == 'POST':
        mois = request.form['mois']
        annee = request.form['annee']
        garantie = request.form['garantie']
        print (mois, annee, garantie)
        db =db_connxion.get_cnn()
        error = None
        cur2 = db.cursor()
        cur3 = db.cursor()
        if (garantie == 'RC'):
             etat2 = cur2.execute("""select  agen.numagen  ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_rc else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_rc else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_rc  else 0 end) 
             from  prodpargaraparagen p, agence_saa agen where   p.mois = %s and p.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

             etat3 = cur3.execute("""select sum (prime_rc),sum (rec_rc),  sum (  nombre_rc)
            from  prodpargaraparagen  where   mois = %s and annee =%s  """,(mois,annee,))
        elif (garantie == 'RC interarab'):
             etat2 = cur2.execute("""select  agen.numagen  ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_rcarab else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_rcarab else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_rcarab  else 0 end) 
             from  prodpargaraparagen p, agence_saa agen where   p.mois = %s and p.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))
            
             etat3 = cur3.execute("""select sum (prime_rcarab),sum (rec_rcarab),  sum (  nombre_rcarab)
            from  prodpargaraparagen  where   mois = %s and annee =%s  """,(mois,annee,))
        elif (garantie == 'RC frontiere'):
             etat2 = cur2.execute("""select  agen.numagen  ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_rcfront else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_rcfront else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_rcfront  else 0 end) 
             from  prodpargaraparagen p, agence_saa agen where   p.mois = %s and p.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

             etat3 = cur3.execute("""select sum (prime_rcfront),sum (rec_rcfront),  sum (  nombre_rcfront)
            from  prodpargaraparagen  where   mois = %s and annee =%s  """,(mois,annee,))
        elif (garantie == 'TR simple'):
             etat2 = cur2.execute("""select  agen.numagen  ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_tr else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_tr else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_tr  else 0 end) 
             from  prodpargaraparagen p, agence_saa agen where   p.mois = %s and p.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

             
             etat3 = cur3.execute("""select sum (prime_tr),sum (rec_tr),  sum (  nombre_tr)
            from  prodpargaraparagen  where   mois = %s and annee =%s  """,(mois,annee,))

        elif (garantie == 'DASC 200 000'):
             etat2 = cur2.execute("""select  agen.numagen  ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_dasc200000 else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_dasc200000 else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_dasc200000  else 0 end) 
             from  prodpargaraparagen p, agence_saa agen where   p.mois = %s and p.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

             etat3 = cur3.execute("""select sum (prime_dasc200000),sum (rec_dasc200000),  sum (  nombre_dasc200000)
            from  prodpargaraparagen  where   mois = %s and annee =%s  """,(mois,annee,))
        elif (garantie == 'DASC 300 000'):
             etat2 = cur2.execute("""select  agen.numagen  ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_dasc300000 else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_dasc300000 else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_dasc300000  else 0 end) 
             from  prodpargaraparagen p, agence_saa agen where   p.mois = %s and p.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))
    
             etat3 = cur3.execute("""select sum (prime_dasc300000),sum (rec_dasc300000),  sum (  nombre_dasc300000)
            from  prodpargaraparagen  where   mois = %s and annee =%s  """,(mois,annee,))
        elif (garantie == 'DASC 500 000'):
             etat2 = cur2.execute("""select  agen.numagen  ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_dasc500000 else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_dasc500000 else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_dasc500000  else 0 end) 
             from  prodpargaraparagen p, agence_saa agen where   p.mois = %s and p.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

             etat3 = cur3.execute("""select sum (prime_dasc500000),sum (rec_dasc500000),  sum (  nombre_dasc500000)
            from  prodpargaraparagen  where   mois = %s and annee =%s  """,(mois,annee,))
        elif (garantie == 'DC 10 000'):
             etat2 = cur2.execute("""select  agen.numagen  ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_DC10000 else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_DC10000 else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_DC10000  else 0 end) 
             from  prodpargaraparagen p, agence_saa agen where   p.mois = %s and p.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

             etat3 = cur3.execute("""select sum (prime_DC10000),sum (rec_DC10000),  sum (  nombre_DC10000)
            from  prodpargaraparagen  where   mois = %s and annee =%s  """,(mois,annee,))
        elif (garantie == 'DC 20 000'):
             etat2 = cur2.execute("""select  agen.numagen  ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_DC20000 else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_DC20000 else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_DC20000  else 0 end) 
             from  prodpargaraparagen p, agence_saa agen where   p.mois = %s and p.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

             etat3 = cur3.execute("""select sum (prime_DC20000),sum (rec_DC20000),  sum (  nombre_DC20000)
            from  prodpargaraparagen  where   mois = %s and annee =%s  """,(mois,annee,))
        elif (garantie == 'DC 30 000'):
             etat2 = cur2.execute("""select  agen.numagen  ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_DC30000 else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_DC30000 else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_DC30000  else 0 end) 
             from  prodpargaraparagen p, agence_saa agen where  p.mois = %s and p.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

             etat3 = cur3.execute("""select sum (prime_DC30000),sum (rec_DC30000),  sum (  nombre_DC30000)
            from  prodpargaraparagen  where   mois = %s and annee =%s  """,(mois,annee,))
        elif (garantie == 'DC 40 000'):
             etat2 = cur2.execute("""select  agen.numagen  ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_DC40000 else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_DC40000 else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_DC40000  else 0 end) 
             from  prodpargaraparagen p, agence_saa agen where   p.mois = %s and p.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

             etat3 = cur3.execute("""select sum (prime_DC40000),sum (rec_DC40000),  sum (  nombre_DC40000)
            from  prodpargaraparagen  where   mois = %s and annee =%s  """,(mois,annee,))
        elif (garantie == 'DC 50 000'):
             etat2 = cur2.execute("""select  agen.numagen  ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_DC50000 else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_DC50000 else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_DC50000  else 0 end) 
             from  prodpargaraparagen p, agence_saa agen where   p.mois = %s and p.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

             etat3 = cur3.execute("""select sum (prime_DC50000),sum (rec_DC50000),  sum (  nombre_DC50000)
            from  prodpargaraparagen  where   mois = %s and annee =%s  """,(mois,annee,))
        elif (garantie == 'DC VV'):
             etat2 = cur2.execute("""select  agen.numagen  ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_DCVV else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_DCVV else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_DCVV  else 0 end) 
             from  prodpargaraparagen p, agence_saa agen where   p.mois = %s and p.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

             etat3 = cur3.execute("""select sum (prime_DCVV),sum (rec_DCVV),  sum (  nombre_DCVV)
            from  prodpargaraparagen  where   mois = %s and annee =%s  """,(mois,annee,))
        elif (garantie == 'VIV'):
             etat2 = cur2.execute("""select  agen.numagen  ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_VIV else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_VIV else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_VIV  else 0 end) 
             from  prodpargaraparagen p, agence_saa agen where  p.mois = %s and p.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

             etat3 = cur3.execute("""select sum (prime_VIV),sum (rec_VIV),  sum (  nombre_VIV)
            from  prodpargaraparagen  where   mois = %s and annee =%s  """,(mois,annee,))          
        elif (garantie == 'VAR'):
             etat2 = cur2.execute("""select  agen.numagen  ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_VAR else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_VAR else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_VAR  else 0 end) 
             from  prodpargaraparagen p, agence_saa agen where   p.mois = %s and p.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

             etat3 = cur3.execute("""select sum (prime_VAR),sum (rec_VAR),  sum (  nombre_VAR)
            from  prodpargaraparagen  where   mois = %s and annee =%s  """,(mois,annee,)) 
        elif (garantie == 'BDG'):
             etat2 = cur2.execute("""select  agen.numagen  ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_BDG else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_BDG else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_BDG  else 0 end) 
             from  prodpargaraparagen p, agence_saa agen where  p.mois = %s and p.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

             etat3 = cur3.execute("""select sum (prime_BDG),sum (rec_BDG),  sum (  nombre_BDG)
            from  prodpargaraparagen  where   mois = %s and annee =%s  """,(mois,annee,)) 
        elif (garantie == 'BDG anoramique'):
             etat2 = cur2.execute("""select  agen.numagen  ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_pdga else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_pdga else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_pdga  else 0 end) 
             from  prodpargaraparagen p, agence_saa agen where   p.mois = %s and p.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

             etat3 = cur3.execute("""select sum (prime_pdga),sum (rec_pdga),  sum (  nombre_pdga)
            from  prodpargaraparagen  where   mois = %s and annee =%s  """,(mois,annee,)) 
        elif (garantie == 'DR'):
             etat2 = cur2.execute("""select  agen.numagen  ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_DR else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_DR else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_DR  else 0 end) 
             from  prodpargaraparagen p, agence_saa agen where   p.mois = %s and p.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

             etat3 = cur3.execute("""select sum (prime_DR),sum (rec_DR),  sum (  nombre_DR)
            from  prodpargaraparagen  where  mois = %s and annee =%s  """,(mois,annee,)) 

        elif (garantie == 'assist vehicule'):
             etat2 = cur2.execute("""select  agen.numagen  ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_assistvehi else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_assistvehi else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_assistvehi  else 0 end) 
             from  prodpargaraparagen p, agence_saa agen where  p.mois = %s and p.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

             etat3 = cur3.execute("""select sum (prime_assistvehi),sum (rec_assistvehi),  sum (nombre_assistvehi)
            from  prodpargaraparagen  where   mois = %s and annee =%s  """,(mois,annee,)) 
        elif (garantie == 'assist tunisie'):
             etat2 = cur2.execute("""select  agen.numagen  ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_assisttunis else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_assisttunis else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_assisttunis  else 0 end) 
             from  prodpargaraparagen p, agence_saa agen where   p.mois = %s and p.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

             etat3 = cur3.execute("""select sum (prime_assisttunis),sum (rec_assisttunis),  sum (  nombre_assisttunis)
            from  prodpargaraparagen  where   mois = %s and annee =%s  """,(mois,annee,)) 
        elif (garantie == 'ATES'):
             etat2 = cur2.execute("""select  agen.numagen  ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_ATES else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_ATES else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_ATES  else 0 end) 
             from  prodpargaraparagen p, agence_saa agen where  p.mois = %s and p.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

             etat3 = cur3.execute("""select sum (prime_ATES),sum (rec_ATES),  sum (  nombre_ATES)
            from  prodpargaraparagen  where   mois = %s and annee =%s  """,(mois,annee,)) 
        elif (garantie == 'PEA'):
             etat2 = cur2.execute("""select  agen.numagen  ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_PEA else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_PEA else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_PEA  else 0 end) 
             from  prodpargaraparagen p, agence_saa agen where   p.mois = %s and p.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

             etat3 = cur3.execute("""select sum (prime_PEA),sum (rec_PEA),  sum (  nombre_PEA)
            from  prodpargaraparagen  where   mois = %s and annee =%s  """,(mois,annee,)) 
        elif (garantie == 'TOP reparateur'):
             etat2 = cur2.execute("""select  agen.numagen  ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_toprep else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_toprep else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_toprep  else 0 end) 
             from  prodpargaraparagen p, agence_saa agen where   p.mois = %s and p.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

             etat3 = cur3.execute("""select sum (prime_toprep),sum (rec_toprep),  sum (  nombre_toprep)
            from  prodpargaraparagen  where   mois = %s and annee =%s  """,(mois,annee,)) 
        elif (garantie == 'rachat vetustee'):
             etat2 = cur2.execute("""select  agen.numagen  ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_rachat else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_rachat else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_rachat  else 0 end) 
             from  prodpargaraparagen p, agence_saa agen where   p.mois = %s and p.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

             etat3 = cur3.execute("""select sum (prime_rachat),sum (rec_rachat),  sum (  nombre_rachat)
            from  prodpargaraparagen  where  mois = %s and annee =%s  """,(mois,annee,)) 
        elif (garantie == 'tremblement terre'):
             etat2 = cur2.execute("""select  agen.numagen  ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_tromb else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_tromb else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_tromb  else 0 end) 
             from  prodpargaraparagen p, agence_saa agen where   p.mois = %s and p.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

             etat3 = cur3.execute("""select sum (prime_tromb),sum (rec_tromb),  sum (  nombre_tromb)
            from  prodpargaraparagen  where   mois = %s and annee =%s  """,(mois,annee,)) 
        elif (garantie == 'emeut mouv pop'):
             etat2 = cur2.execute("""select  agen.numagen  ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_emeut else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_emeut else 0 end) ,
             sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_emeut  else 0 end) 
             from  prodpargaraparagen p, agence_saa agen where   p.mois = %s and p.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

             etat3 = cur3.execute("""select sum (prime_emeut),sum (rec_emeut),  sum (  nombre_emeut)
            from  prodpargaraparagen  where  mois = %s and annee =%s  """,(mois,annee,)) 
        result2 = cur2.fetchall()
        result3 = cur3.fetchone()
        print(result2 )
        if result2 == []: 
            error ="l'etat n'est pas disponible  "
            print(error)
        if error is None:

            return render_template('etatstatpourchaquegaraparagen.html',session=session['nom'],resultat =result2,resultat2 =result3 ,mois =mois,annee =annee, garantie=garantie ,session2= session['mail'] )
     return render_template('formeautopourchaquegara.html',error =error,session=session['nom'],session2= session['mail'] )  

@app.route("/etatautosinimatshono" ,methods=('GET', 'POST'))
def etatautosinimatshono():
     if request.method == 'POST':
        mois = request.form['mois']
        annee = request.form['annee']
        print (mois, annee)
        months = dict(jan=1, feb=2, mar=3,apr=4,may=5, jun=6,jul=7, aug=8, Sep=9,oct=10,nov=11,dec=12 )
        print(months[mois])
        sut = months[mois] -1
        print(sut)
        db =db_connxion.get_cnn()
        error = None
        cur1 = db.cursor()
        cur2 = db.cursor()
        cur3 = db.cursor()
        cur4 = db.cursor()
        etatsini1 = cur1.execute("""select agen.numagen , 
         sum( case when (stk.numagen = agen.numagen) then  stk.nombre_ancienstk else 0 end) ,
         sum(case when stk.numagen = agen.numagen then stk.nombre_declarer else 0 end) ,
         sum(case when stk.numagen = agen.numagen then stk.nombre_regle else 0 end) ,

         (sum( case when (stk.numagen = agen.numagen) then  stk.nombre_ancienstk else 0 end)  +
         sum(case when stk.numagen = agen.numagen then stk.nombre_declarer else 0 end)- 
         sum(case when stk.numagen = agen.numagen then stk.nombre_regle else 0 end)),
         sum (((case when stk.numagen = agen.numagen then stk.nombre_regle else 0 end) * 100) / 
         (case when stk.numagen = agen.numagen then stk.nombre_declarer else 1 end))::integer,
         sum(case when stk.numagen = agen.numagen then stk.reglement else 0 end) 
         from agence_saa agen,sinistremat_nvxstok stk  where  stk.mois = %s and stk.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

        etatsini2 = cur2.execute("""select sum (stk.nombre_ancienstk),sum (stk.nombre_declarer),  sum (  stk.nombre_regle),
        sum ( stk.nombre_ancienstk)+sum (stk.nombre_declarer)- sum (  stk.nombre_regle),
        (sum(stk.nombre_regle) * 100 / sum(stk.nombre_declarer))::integer, sum(stk.reglement )
        from  sinistremat_nvxstok stk  where   mois = %s and annee =%s  """,(mois,annee,)) 
        if sut == 0 :
            etatsini1 = cur3.execute("""select agen.numagen ,
            sum( case when (stk.numagen = agen.numagen) then  stk.nvx_stk else 0 end) 
            from agence_saa agen,sinistremat_nvxstok stk  where  
            stk.mois =to_char(to_timestamp(to_char(date_part('MON', to_timestamp('dec', ' mon')::date) -1,'999'),'MM'), 'mon')  and
            cast(stk.annee as integer) =%s-1   GROUP BY 1 ORDER BY 1""",(annee,))
            etatsini1 = cur4.execute("""select  sum( stk.nvx_stk)  
            from sinistremat_nvxstok stk  where  
            stk.mois =to_char(to_timestamp(to_char(date_part('MON', to_timestamp('dec', ' mon')::date) -1,'999'),'MM'), 'mon')  and
             cast(stk.annee as integer) =%s-1  """,(annee,))
            
        else:

            etatsini1 = cur3.execute("""select agen.numagen ,
            sum( case when (stk.numagen = agen.numagen) then  stk.nvx_stk else 0 end) 
            from agence_saa agen,sinistremat_nvxstok stk  where  
            stk.mois =to_char(to_timestamp(to_char(date_part('MON', to_timestamp(%s, ' mon')::date) -1,'999'),'MM'), 'mon')  
            and stk.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))
            etatsini1 = cur4.execute("""select  sum( stk.nvx_stk) 
            from sinistremat_nvxstok stk  where  
            stk.mois =to_char(to_timestamp(to_char(date_part('MON', to_timestamp(%s, ' mon')::date) -1,'999'),'MM'), 'mon')  
            and stk.annee =%s """,(mois,annee,))

        result1 = cur1.fetchall()
        result2 = cur2.fetchone()
        result3 = cur3.fetchall()
        result4 = cur4.fetchone()
       
        print(result1 )
        print(result2 )
        print(result3 )
         
        datenow = datetime.now()
        date_finmois = datetime(datenow.year, datenow.month, 1) + relativedelta(months=1, days=-1) 
       
        print(datenow)
        anneeact = datenow.year
        moisact = datenow.month
        
        if date_finmois > datenow and months[mois]== moisact and int(annee)== anneeact: 
            error = "l'etat que vous_avez demandée n'est pas encore prét"
        if result1 == []: 
            error ="l'etat n'est pas disponible  "
        if error is None:
            return render_template('etatautosinimatshono.html',session=session['nom'],resultats1 =result1,resultats2 =result2,resultats3 =result3,mois =mois,annee =annee, resultats4 =result4 ,session2= session['mail'] )
     return render_template('formeetatautosinistrmatshmoi.html',error =error,session=session['nom'],session2= session['mail'] )  
    

@app.route("/etatsuiviedecadeduportfeuille",methods=('GET', 'POST'))
def etatsuiviedecadeduportfeuille():
     if request.method == 'POST':
        numd = request.form['numd']
        mois = request.form['mois']
        annee = request.form['annee']
        agence = request.form['agence']
        print (numd,mois, annee,agence)
        db =db_connxion.get_cnn()
        error = None
        cur1 = db.cursor()
        cur2 = db.cursor()
        if (numd =='01'):
            etat1com = cur1.execute("""select nombre_ro, prime_ro, nombre_rno, prime_rno, nombre_assistauto, prime_assistauto,
            nombre_ro +nombre_rno + nombre_assistauto , prime_ro +prime_rno + prime_assistauto,nombre_rs, 
            prime_rs , nombre_ri, prime_ri, nombre_agricole,prime_agricole , nombre_transport, prime_transport,
            nombre_ri + nombre_agricole + nombre_transport,
            prime_ri + prime_agricole + prime_transport ,
            nombre_ro +nombre_rno + nombre_assistauto +nombre_rs + nombre_ri + nombre_agricole + nombre_transport +nombre_rs,
            prime_ro +prime_rno + prime_assistauto + prime_ri + prime_agricole + prime_transport +prime_rs
            from premieredecade_com where mois= %s and annee =%s and numagen=%s""",(mois,annee,agence,)) 
        
            etat1com = cur2.execute("""select nombre_ro, prime_ro, nombre_rno, prime_rno, nombre_assistauto, 
            prime_assistauto,nombre_ro +nombre_rno + nombre_assistauto , prime_ro +prime_rno + prime_assistauto,nombre_rs, 
            prime_rs , nombre_ri, prime_ri, nombre_agricole,prime_agricole ,
            nombre_transport, prime_transport, nombre_ri + nombre_agricole + nombre_transport,
            prime_ri + prime_agricole + prime_transport ,
            nombre_ro +nombre_rno + nombre_assistauto +nombre_rs + nombre_ri + nombre_agricole + nombre_transport +nombre_rs,
            prime_ro +prime_rno + prime_assistauto + prime_ri + prime_agricole + prime_transport +prime_rs
            from premieredecade_com where mois= %s and annee =cast(%s as integer)-1 and numagen=%s""",(mois,annee,agence,))
           
        elif (numd =='02'):
            etat1com = cur1.execute("""select nombre_ro, prime_ro, nombre_rno, prime_rno, nombre_assistauto, prime_assistauto,
            nombre_ro +nombre_rno + nombre_assistauto , prime_ro +prime_rno + prime_assistauto,nombre_rs, 
            prime_rs , nombre_ri, prime_ri, nombre_agricole,prime_agricole , nombre_transport, prime_transport,
            nombre_ri + nombre_agricole + nombre_transport,
            prime_ri + prime_agricole + prime_transport ,
            nombre_ro +nombre_rno + nombre_assistauto +nombre_rs + nombre_ri + nombre_agricole + nombre_transport +nombre_rs,
            prime_ro +prime_rno + prime_assistauto + prime_ri + prime_agricole + prime_transport +prime_rs
            from deuxiemedecade_com where mois= %s and annee =%s and numagen=%s""",(mois,annee,agence,)) 
        
            etat1com = cur2.execute("""select nombre_ro, prime_ro, nombre_rno, prime_rno, nombre_assistauto, prime_assistauto,
            nombre_ro +nombre_rno +nombre_assistauto , prime_ro +prime_rno + prime_assistauto,nombre_rs, 
            prime_rs , nombre_ri, prime_ri, nombre_agricole,prime_agricole , nombre_transport, prime_transport, 
            nombre_ri + nombre_agricole + nombre_transport,
            prime_ri + prime_agricole + prime_transport ,
            nombre_ro +nombre_rno + nombre_assistauto +nombre_rs + nombre_ri + nombre_agricole + nombre_transport +nombre_rs,
            prime_ro +prime_rno + prime_assistauto + prime_ri + prime_agricole + prime_transport +prime_rs
            from deuxiemedecade_com where mois= %s and annee =cast(%s as integer)-1 and numagen=%s""",(mois,annee,agence,))

        elif (numd =='03'):
            etat1com = cur1.execute("""select nombre_ro, prime_ro, nombre_rno, prime_rno, nombre_assistauto, prime_assistauto,
            nombre_ro +nombre_rno +nombre_assistauto , prime_ro +prime_rno + prime_assistauto,nombre_rs, 
            prime_rs , nombre_ri, prime_ri, nombre_agricole,prime_agricole , nombre_transport, prime_transport, 
            nombre_ri + nombre_agricole + nombre_transport,
            prime_ri + prime_agricole + prime_transport ,
            nombre_ro +nombre_rno + nombre_assistauto +nombre_rs + nombre_ri + nombre_agricole + nombre_transport +nombre_rs,
            prime_ro +prime_rno + prime_assistauto + prime_ri + prime_agricole + prime_transport +prime_rs
            from troisiemedecade_com where mois= %s and annee =%s and numagen=%s""",(mois,annee,agence,)) 
        
            etat1com2 = cur2.execute("""select nombre_ro, prime_ro, nombre_rno, prime_rno, nombre_assistauto,
            prime_assistauto,nombre_ro +nombre_rno + nombre_assistauto , prime_ro +prime_rno + prime_assistauto,nombre_rs, 
            prime_rs , nombre_ri, prime_ri, nombre_agricole,prime_agricole , nombre_transport, prime_transport, 
            nombre_ri + nombre_agricole + nombre_transport,
            prime_ri + prime_agricole + prime_transport ,
            nombre_ro +nombre_rno + nombre_assistauto +nombre_rs + nombre_ri + nombre_agricole + nombre_transport +nombre_rs,
            prime_ro +prime_rno + prime_assistauto + prime_ri + prime_agricole + prime_transport +prime_rs
            from troisiemedecade_com where mois= %s and annee =cast(%s as integer)-1 and numagen=%s""",(mois,annee,agence,))           
        result1 = cur1.fetchone()  
        result2 = cur2.fetchone()
        if result1 is None :
            error  = "l'etat demandé n'est pos disponible !!!"
        if result2 is None : 
            flash(" Nous n'avons pas pu effectuer l'valuation car des  données passée ne sont plus disponible")
        print(result1) 
        print(result2) 
        if error is None:

            return render_template('etatsuiviedecadeduportfeuille.html',session=session['nom'] ,numerod=numd, mois =mois,annee =annee, agenceg = agence , resultat =result1, resultat2 =result2 ,session2= session['mail']  )
     return render_template('formeetatcomdecade.html',error =error,session=session['nom'],session2= session['mail'] )  



@app.route("/etatcomdecadetoutlesagen",methods=('GET', 'POST'))
def etatcomdecadetoutlesagen():
     if request.method == 'POST':
        numd = request.form['numd']
        mois = request.form['mois']
        annee = request.form['annee']
        print (numd,mois, annee)
        db =db_connxion.get_cnn()
        error = None
        cur1 = db.cursor()
        cur2 = db.cursor()
        if (numd =='01'):
            etat1com = cur1.execute("""select 
                                     sum(nombre_ro),
                                     sum( prime_ro),
                                     sum (nombre_rno),
                                     sum(prime_rno),
                                     sum (nombre_assistauto),
                                     sum(prime_assistauto),
                                     sum(nombre_ro) +sum(nombre_rno) +sum(nombre_assistauto) ,
                                     sum( prime_ro) +sum(prime_rno) + sum(prime_assistauto),
                                     sum(nombre_rs), 
                                     sum(prime_rs) ,
                                     sum( nombre_ri),
                                     sum( prime_ri),
                                     sum (nombre_agricole),
                                     sum(prime_agricole) ,
                                     sum(nombre_transport),
                                     sum (prime_transport),
                                     sum(nombre_ri) + sum(nombre_agricole) +sum (nombre_transport),
                                     sum(prime_ri) + sum(prime_agricole) +sum( prime_transport) ,
                                     sum(nombre_ro )+sum(nombre_rno) +sum( nombre_assistauto) +sum(nombre_rs) + sum(nombre_ri) + sum(nombre_agricole) +sum( nombre_transport )+sum(nombre_rs),
                                     sum( prime_ro) +sum(prime_rno) + sum(prime_assistauto) + sum(prime_ri) + sum(prime_agricole) +sum( prime_transport) +sum(prime_rs)
                                     from premieredecade_com where mois= %s and annee =%s """,(mois,annee,)) 
            etat1com2 = cur2.execute("""select 
                                     sum(nombre_ro),
                                     sum( prime_ro),
                                     sum (nombre_rno),
                                     sum(prime_rno),
                                     sum (nombre_assistauto),
                                     sum(prime_assistauto),
                                     sum(nombre_ro) +sum(nombre_rno) +sum(nombre_assistauto) ,
                                     sum( prime_ro) +sum(prime_rno) + sum(prime_assistauto),
                                     sum(nombre_rs), 
                                     sum(prime_rs) ,
                                     sum( nombre_ri),
                                     sum( prime_ri),
                                     sum (nombre_agricole),
                                     sum(prime_agricole) ,
                                     sum(nombre_transport),
                                     sum (prime_transport),
                                     sum(nombre_ri) + sum(nombre_agricole) +sum (nombre_transport),
                                     sum(prime_ri) + sum(prime_agricole) +sum( prime_transport) ,
                                     sum(nombre_ro )+sum(nombre_rno) +sum( nombre_assistauto) +sum(nombre_rs) + sum(nombre_ri) + sum(nombre_agricole) +sum( nombre_transport )+sum(nombre_rs),
                                     sum( prime_ro) +sum(prime_rno) + sum(prime_assistauto) + sum(prime_ri) + sum(prime_agricole) +sum( prime_transport) +sum(prime_rs)

                                     from premieredecade_com where mois= %s and annee =cast(%s as integer)-1 """,(mois,annee,))

        elif (numd =='02'):
            etat1com = cur1.execute("""select 
                                     sum(nombre_ro),
                                     sum( prime_ro),
                                     sum (nombre_rno),
                                     sum(prime_rno),
                                     sum (nombre_assistauto),
                                     sum(prime_assistauto),
                                     sum(nombre_ro) +sum(nombre_rno) +sum(nombre_assistauto) ,
                                     sum( prime_ro) +sum(prime_rno) + sum(prime_assistauto),
                                     sum(nombre_rs), 
                                     sum(prime_rs) ,
                                     sum( nombre_ri),
                                     sum( prime_ri),
                                     sum (nombre_agricole),
                                     sum(prime_agricole) ,
                                     sum(nombre_transport),
                                     sum (prime_transport),
                                     sum(nombre_ri) + sum(nombre_agricole) +sum (nombre_transport),
                                     sum(prime_ri) + sum(prime_agricole) +sum( prime_transport) ,
                                     sum(nombre_ro )+sum(nombre_rno) +sum( nombre_assistauto) +sum(nombre_rs) + sum(nombre_ri) + sum(nombre_agricole) +sum( nombre_transport )+sum(nombre_rs),
                                     sum( prime_ro) +sum(prime_rno) + sum(prime_assistauto) + sum(prime_ri) + sum(prime_agricole) +sum( prime_transport) +sum(prime_rs)
                                     from deuxiemedecade_com where mois= %s and annee =%s """,(mois,annee,)) 
            etat1com2 = cur2.execute("""select 
                                     sum(nombre_ro),
                                     sum( prime_ro),
                                     sum (nombre_rno),
                                     sum(prime_rno),
                                     sum (nombre_assistauto),
                                     sum(prime_assistauto),
                                     sum(nombre_ro) +sum(nombre_rno) +sum(nombre_assistauto) ,
                                     sum( prime_ro) +sum(prime_rno) + sum(prime_assistauto),
                                     sum(nombre_rs), 
                                     sum(prime_rs) ,
                                     sum( nombre_ri),
                                     sum( prime_ri),
                                     sum (nombre_agricole),
                                     sum(prime_agricole) ,
                                     sum(nombre_transport),
                                     sum (prime_transport),
                                     sum(nombre_ri) + sum(nombre_agricole) +sum (nombre_transport),
                                     sum(prime_ri) + sum(prime_agricole) +sum( prime_transport) ,
                                     sum(nombre_ro )+sum(nombre_rno) +sum( nombre_assistauto) +sum(nombre_rs) + sum(nombre_ri) + sum(nombre_agricole) +sum( nombre_transport )+sum(nombre_rs),
                                     sum( prime_ro) +sum(prime_rno) + sum(prime_assistauto) + sum(prime_ri) + sum(prime_agricole) +sum( prime_transport) +sum(prime_rs)

                                     from deuxiemedecade_com where mois= %s and annee =cast(%s as integer)-1 """,(mois,annee,))

        elif (numd =='03'):
            etat1com = cur1.execute("""select 
                                     sum(nombre_ro),
                                     sum( prime_ro),
                                     sum (nombre_rno),
                                     sum(prime_rno),
                                     sum (nombre_assistauto),
                                     sum(prime_assistauto),
                                     sum(nombre_ro) +sum(nombre_rno) +sum(nombre_assistauto) ,
                                     sum( prime_ro) +sum(prime_rno) + sum(prime_assistauto),
                                     sum(nombre_rs), 
                                     sum(prime_rs) ,
                                     sum( nombre_ri),
                                     sum( prime_ri),
                                     sum (nombre_agricole),
                                     sum(prime_agricole) ,
                                     sum(nombre_transport),
                                     sum (prime_transport),
                                     sum(nombre_ri) + sum(nombre_agricole) +sum (nombre_transport),
                                     sum(prime_ri) + sum(prime_agricole) +sum( prime_transport) ,
                                     sum(nombre_ro )+sum(nombre_rno) +sum( nombre_assistauto) +sum(nombre_rs) + sum(nombre_ri) + sum(nombre_agricole) +sum( nombre_transport )+sum(nombre_rs),
                                     sum( prime_ro) +sum(prime_rno) + sum(prime_assistauto) + sum(prime_ri) + sum(prime_agricole) +sum( prime_transport) +sum(prime_rs)
                                     from troisiemedecade_com where mois= %s and annee =%s """,(mois,annee,)) 
            etat1com2 = cur2.execute("""select 
                                     sum(nombre_ro),
                                     sum( prime_ro),
                                     sum (nombre_rno),
                                     sum(prime_rno),
                                     sum (nombre_assistauto),
                                     sum(prime_assistauto),
                                     sum(nombre_ro) +sum(nombre_rno) +sum(nombre_assistauto) ,
                                     sum( prime_ro) +sum(prime_rno) + sum(prime_assistauto),
                                     sum(nombre_rs), 
                                     sum(prime_rs) ,
                                     sum( nombre_ri),
                                     sum( prime_ri),
                                     sum (nombre_agricole),
                                     sum(prime_agricole) ,
                                     sum(nombre_transport),
                                     sum (prime_transport),
                                     sum(nombre_ri) + sum(nombre_agricole) +sum (nombre_transport),
                                     sum(prime_ri) + sum(prime_agricole) +sum( prime_transport) ,
                                     sum(nombre_ro )+sum(nombre_rno) +sum( nombre_assistauto) +sum(nombre_rs) + sum(nombre_ri) + sum(nombre_agricole) +sum( nombre_transport )+sum(nombre_rs),
                                     sum( prime_ro) +sum(prime_rno) + sum(prime_assistauto) + sum(prime_ri) + sum(prime_agricole) +sum( prime_transport) +sum(prime_rs)

                                     from troisiemedecade_com where mois= %s and annee =cast(%s as integer)-1 """,(mois,annee,))
        result1 = cur1.fetchone()   
        result2 = cur2.fetchone()  
        if result1 is None :
            error  = "l'etat demandé n'est pos disponible !!!"
        if result2[0] is None : 
            flash(" Nous n'avons pas pu effectuer l'valuation car des  données passée ne sont plus disponible")        
        print(result1) 
        print(result2) 
        if error is None:

            return render_template('etatcomdecadetoutlesagen.html',session=session['nom'] ,numerod=numd, mois =mois,annee =annee , resultat =result1, resultat2 =result2 ,session2= session['mail'] )
     return render_template('formecomdecadetoutlesagen.html',error =error,session=session['nom'],session2= session['mail'] )  

@app.route("/etatdecadepourlesagencesdirecte",methods=('GET', 'POST'))
def etatdecadepourlesagencesdirecte():
     if request.method == 'POST':
        numd = request.form['numd']
        mois = request.form['mois']
        annee = request.form['annee']
        
        print (numd,mois, annee)
        db =db_connxion.get_cnn()
        error = None
        cur1 = db.cursor()
        cur2 = db.cursor()

        if (numd =='01'):
            etat1com = cur1.execute("""select 
            nbrero_direct,
            primero_direct,
            nbrerno_direct,
            primerno_direct,
            nbreassistauto_direct,
            primeassistauto_direct,
            nbrero_direct +nbrerno_direct+nbreassistauto_direct,
            primero_direct + primerno_direct + primeassistauto_direct,
            nbrers_direct,
            primers_direct,
            nbreri_direct,
            primeri_direct,
            nbreagricole_direct,
            primeagricole_direct,
            nbretransport_direct,
            primetransport_direct,
            nbreri_direct+nbreagricole_direct+nbretransport_direct,
            primeri_direct+primeagricole_direct+primetransport_direct,
            nbrero_direct +nbrerno_direct+nbreassistauto_direct + nbrers_direct+ nbreri_direct+nbreagricole_direct+nbretransport_direct,
            primero_direct + primerno_direct + primeassistauto_direct +primers_direct +primeri_direct+primeagricole_direct+primetransport_direct
            from premieredecate_directe where mois= %s and annee =%s """,(mois,annee,)) 
            
      
            etat2com = cur2.execute("""select 
            nbrero_direct,
            primero_direct,
            nbrerno_direct,
            primerno_direct,
            nbreassistauto_direct,
            primeassistauto_direct,
            nbrero_direct +nbrerno_direct+nbreassistauto_direct,
            primero_direct + primerno_direct + primeassistauto_direct,
            nbrers_direct,
            primers_direct,
            nbreri_direct,
            primeri_direct,
            nbreagricole_direct,
            primeagricole_direct,
            nbretransport_direct,
            primetransport_direct,
            nbreri_direct+nbreagricole_direct+nbretransport_direct,
            primeri_direct+primeagricole_direct+primetransport_direct,
            nbrero_direct +nbrerno_direct+nbreassistauto_direct + nbrers_direct+ nbreri_direct+nbreagricole_direct+nbretransport_direct,
            primero_direct + primerno_direct + primeassistauto_direct +primers_direct +primeri_direct+primeagricole_direct+primetransport_direct            
            from premieredecate_directe where mois= %s and annee =cast(%s as integer)-1 """,(mois,annee,))

        elif (numd =='02'):
            etat1com = cur1.execute("""select 
            nbrero_direct,
            primero_direct,
            nbrerno_direct,
            primerno_direct,
            nbreassistauto_direct,
            primeassistauto_direct,
            nbrero_direct +nbrerno_direct+nbreassistauto_direct,
            primero_direct + primerno_direct + primeassistauto_direct,
            nbrers_direct,
            primers_direct,
            nbreri_direct,
            primeri_direct,
            nbreagricole_direct,
            primeagricole_direct,
            nbretransport_direct,
            primetransport_direct,
            nbreri_direct+nbreagricole_direct+nbretransport_direct,
            primeri_direct+primeagricole_direct+primetransport_direct,
            nbrero_direct +nbrerno_direct+nbreassistauto_direct + nbrers_direct+ nbreri_direct+nbreagricole_direct+nbretransport_direct,
            primero_direct + primerno_direct + primeassistauto_direct +primers_direct +primeri_direct+primeagricole_direct+primetransport_direct
            from deuxiemedecade_directe where mois= %s and annee =%s """,(mois,annee,)) 
            
      
            etat2com = cur2.execute("""select 
            nbrero_direct,
            primero_direct,
            nbrerno_direct,
            primerno_direct,
            nbreassistauto_direct,
            primeassistauto_direct,
            nbrero_direct +nbrerno_direct+nbreassistauto_direct,
            primero_direct + primerno_direct + primeassistauto_direct,
            nbrers_direct,
            primers_direct,
            nbreri_direct,
            primeri_direct,
            nbreagricole_direct,
            primeagricole_direct,
            nbretransport_direct,
            primetransport_direct,
            nbreri_direct+nbreagricole_direct+nbretransport_direct,
            primeri_direct+primeagricole_direct+primetransport_direct,
            nbrero_direct +nbrerno_direct+nbreassistauto_direct + nbrers_direct+ nbreri_direct+nbreagricole_direct+nbretransport_direct,
            primero_direct + primerno_direct + primeassistauto_direct +primers_direct +primeri_direct+primeagricole_direct+primetransport_direct            
            from deuxiemedecade_directe where mois= %s and annee =cast(%s as integer)-1 """,(mois,annee,))
        elif (numd =='03'):
            etat1com = cur1.execute("""select 
            nbrero_direct,
            primero_direct,
            nbrerno_direct,
            primerno_direct,
            nbreassistauto_direct,
            primeassistauto_direct,
            nbrero_direct +nbrerno_direct+nbreassistauto_direct,
            primero_direct + primerno_direct + primeassistauto_direct,
            nbrers_direct,
            primers_direct,
            nbreri_direct,
            primeri_direct,
            nbreagricole_direct,
            primeagricole_direct,
            nbretransport_direct,
            primetransport_direct,
            nbreri_direct+nbreagricole_direct+nbretransport_direct,
            primeri_direct+primeagricole_direct+primetransport_direct,
            nbrero_direct +nbrerno_direct+nbreassistauto_direct + nbrers_direct+ nbreri_direct+nbreagricole_direct+nbretransport_direct,
            primero_direct + primerno_direct + primeassistauto_direct +primers_direct +primeri_direct+primeagricole_direct+primetransport_direct
            from troisiemedecade_directe where mois= %s and annee =%s """,(mois,annee,)) 
            
      
            etat2com = cur2.execute("""select 
            nbrero_direct,
            primero_direct,
            nbrerno_direct,
            primerno_direct,
            nbreassistauto_direct,
            primeassistauto_direct,
            nbrero_direct +nbrerno_direct+nbreassistauto_direct,
            primero_direct + primerno_direct + primeassistauto_direct,
            nbrers_direct,
            primers_direct,
            nbreri_direct,
            primeri_direct,
            nbreagricole_direct,
            primeagricole_direct,
            nbretransport_direct,
            primetransport_direct,
            nbreri_direct+nbreagricole_direct+nbretransport_direct,
            primeri_direct+primeagricole_direct+primetransport_direct,
            nbrero_direct +nbrerno_direct+nbreassistauto_direct + nbrers_direct+ nbreri_direct+nbreagricole_direct+nbretransport_direct,
            primero_direct + primerno_direct + primeassistauto_direct +primers_direct +primeri_direct+primeagricole_direct+primetransport_direct            
            from troisiemedecade_directe where mois= %s and annee =cast(%s as integer)-1 """,(mois,annee,))
            
        result1 = cur1.fetchone()
        result2 = cur2.fetchone()
        if result1 is None :
            error  = "l'etat demandé n'est pos disponible !!!"
        if result2 is None : 
            flash(" Nous n'avons pas pu effectuer l'valuation car des  données passée ne sont plus disponible")   
        print(result1) 
        print(result2) 
        if error is None:

            return render_template('etatdecadepourlesagencesdirecte.html',session=session['nom'] ,numerod=numd, mois =mois,annee =annee , resultat =result1,resultat2 =result2,session2= session['mail']   )
     return render_template('formedecadepourlesagencedirecte.html',error =error,session=session['nom'],session2= session['mail'] )  

@app.route("/etatcomdecadepourlesagencesprive",methods=('GET', 'POST'))
def etatcomdecadepourlesagencesprive():
     if request.method == 'POST':
        numd = request.form['numd']
        mois = request.form['mois']
        annee = request.form['annee']
        
        print (numd,mois, annee)
        db =db_connxion.get_cnn()
        error = None
        cur1 = db.cursor()
        cur2 = db.cursor()

        if (numd =='01'):
            etat1com = cur1.execute("""select 
             nbrero_prive,
             primero_prive,
             nbrerno_prive,
             primerno_prive,
             nbreassistauto_prive,
             primeassistauto_prive,
             nbrero_prive + nbrerno_prive + nbreassistauto_prive,
             primero_prive +primerno_prive + primeassistauto_prive,
             nbrers_prive,
             primers_prive,
             nbreri_prive,
             primeri_prive,
             nbreagricole_prive,
             primeagricole_prive,
             nbretransport_prive,
             primetransport_prive,
             nbreri_prive +nbreagricole_prive +nbretransport_prive,
             primeri_prive +primeagricole_prive +primetransport_prive,
             nbrero_prive + nbrerno_prive + nbreassistauto_prive +nbrers_prive +nbreri_prive +nbreagricole_prive +nbretransport_prive,
             primero_prive +primerno_prive + primeassistauto_prive +primers_prive +primeri_prive +primeagricole_prive +primetransport_prive

            from premieredecate_prive where mois= %s and annee =%s """,(mois,annee,)) 
            
      
            etat2com = cur2.execute("""select 
             nbrero_prive,
             primero_prive,
             nbrerno_prive,
             primerno_prive,
             nbreassistauto_prive,
             primeassistauto_prive,
             nbrero_prive + nbrerno_prive + nbreassistauto_prive,
             primero_prive +primerno_prive + primeassistauto_prive,
             nbrers_prive,
             primers_prive,
             nbreri_prive,
             primeri_prive,
             nbreagricole_prive,
             primeagricole_prive,
             nbretransport_prive,
             primetransport_prive,
             nbreri_prive +nbreagricole_prive +nbretransport_prive,
             primeri_prive +primeagricole_prive +primetransport_prive,
             nbrero_prive + nbrerno_prive + nbreassistauto_prive +nbrers_prive +nbreri_prive +nbreagricole_prive +nbretransport_prive,
             primero_prive +primerno_prive + primeassistauto_prive +primers_prive +primeri_prive +primeagricole_prive +primetransport_prive

            from premieredecate_prive where mois= %s and annee =cast(%s as integer)-1 """,(mois,annee,))

        elif (numd =='02'):
            etat1com = cur1.execute("""select 
             nbrero_prive,
             primero_prive,
             nbrerno_prive,
             primerno_prive,
             nbreassistauto_prive,
             primeassistauto_prive,
             nbrero_prive + nbrerno_prive + nbreassistauto_prive,
             primero_prive +primerno_prive + primeassistauto_prive,
             nbrers_prive,
             primers_prive,
             nbreri_prive,
             primeri_prive,
             nbreagricole_prive,
             primeagricole_prive,
             nbretransport_prive,
             primetransport_prive,
             nbreri_prive +nbreagricole_prive +nbretransport_prive,
             primeri_prive +primeagricole_prive +primetransport_prive,
             nbrero_prive + nbrerno_prive + nbreassistauto_prive +nbrers_prive +nbreri_prive +nbreagricole_prive +nbretransport_prive,
             primero_prive +primerno_prive + primeassistauto_prive +primers_prive +primeri_prive +primeagricole_prive +primetransport_prive

            from deuxiemedecade_prive where mois= %s and annee =%s """,(mois,annee,)) 
            
      
            etat2com = cur2.execute("""select 
             nbrero_prive,
             primero_prive,
             nbrerno_prive,
             primerno_prive,
             nbreassistauto_prive,
             primeassistauto_prive,
             nbrero_prive + nbrerno_prive + nbreassistauto_prive,
             primero_prive +primerno_prive + primeassistauto_prive,
             nbrers_prive,
             primers_prive,
             nbreri_prive,
             primeri_prive,
             nbreagricole_prive,
             primeagricole_prive,
             nbretransport_prive,
             primetransport_prive,
             nbreri_prive +nbreagricole_prive +nbretransport_prive,
             primeri_prive +primeagricole_prive +primetransport_prive,
             nbrero_prive + nbrerno_prive + nbreassistauto_prive +nbrers_prive +nbreri_prive +nbreagricole_prive +nbretransport_prive,
             primero_prive +primerno_prive + primeassistauto_prive +primers_prive +primeri_prive +primeagricole_prive +primetransport_prive

            from deuxiemedecade_prive where mois= %s and annee =cast(%s as integer)-1 """,(mois,annee,))

        elif (numd =='03'):
            etat1com = cur1.execute("""select 
             nbrero_prive,
             primero_prive,
             nbrerno_prive,
             primerno_prive,
             nbreassistauto_prive,
             primeassistauto_prive,
             nbrero_prive + nbrerno_prive + nbreassistauto_prive,
             primero_prive +primerno_prive + primeassistauto_prive,
             nbrers_prive,
             primers_prive,
             nbreri_prive,
             primeri_prive,
             nbreagricole_prive,
             primeagricole_prive,
             nbretransport_prive,
             primetransport_prive,
             nbreri_prive +nbreagricole_prive +nbretransport_prive,
             primeri_prive +primeagricole_prive +primetransport_prive,
             nbrero_prive + nbrerno_prive + nbreassistauto_prive +nbrers_prive +nbreri_prive +nbreagricole_prive +nbretransport_prive,
             primero_prive +primerno_prive + primeassistauto_prive +primers_prive +primeri_prive +primeagricole_prive +primetransport_prive

            from troisiemedecade_prive where mois= %s and annee =%s """,(mois,annee,)) 
            
      
            etat2com = cur2.execute("""select 
             nbrero_prive,
             primero_prive,
             nbrerno_prive,
             primerno_prive,
             nbreassistauto_prive,
             primeassistauto_prive,
             nbrero_prive + nbrerno_prive + nbreassistauto_prive,
             primero_prive +primerno_prive + primeassistauto_prive,
             nbrers_prive,
             primers_prive,
             nbreri_prive,
             primeri_prive,
             nbreagricole_prive,
             primeagricole_prive,
             nbretransport_prive,
             primetransport_prive,
             nbreri_prive +nbreagricole_prive +nbretransport_prive,
             primeri_prive +primeagricole_prive +primetransport_prive,
             nbrero_prive + nbrerno_prive + nbreassistauto_prive +nbrers_prive +nbreri_prive +nbreagricole_prive +nbretransport_prive,
             primero_prive +primerno_prive + primeassistauto_prive +primers_prive +primeri_prive +primeagricole_prive +primetransport_prive

            from troisiemedecade_prive where mois= %s and annee =cast(%s as integer)-1 """,(mois,annee,))
        result1 = cur1.fetchone()
        result2 = cur2.fetchone()
        if result1 is None :
            error  = "l'etat demandé n'est pos disponible !!!"
        if result2 is None : 
            flash(" Nous n'avons pas pu effectuer l'valuation car des  données passée ne sont plus disponible")   
        print(result1) 
        print(result2) 
        if error is None:

            return render_template('etatcomdecadepourlesagencesprive.html',session=session['nom'] ,numerod=numd, mois =mois,annee =annee , resultat =result1,resultat2 =result2,session2= session['mail']   )
     return render_template('formedecadepourlesagencedirecte.html',error =error,session=session['nom'],session2= session['mail'] )  

@app.route("/etatcomdecadepourlesbanqueassurance",methods=('GET', 'POST'))
def etatcomdecadepourlesbanqueassurance():
     if request.method == 'POST':
        numd = request.form['numd']
        mois = request.form['mois']
        annee = request.form['annee']
        
        print (numd,mois, annee)
        db =db_connxion.get_cnn()
        error = None
        cur1 = db.cursor()
        cur2 = db.cursor()

        if (numd =='01'):
            etat1com = cur1.execute("""select 
            nbrero_banque,
            primero_banque,
            nbrerno_banque,
            primerno_banque,
            nbreassistauto_banque,
            primeassistauto_banque,
            nbrero_banque + nbrerno_banque + nbreassistauto_banque,
            primero_banque + primerno_banque + primeassistauto_banque,
            nbrers_banque,
            primers_banque,
            nbreri_banque,
            primeri_banque,
            nbreagricole_banque,
            primeagricole_banque,
            nbretransport_banque,
            primetransport_banque,
            nbreri_banque +nbreagricole_banque +nbretransport_banque ,
            primeri_banque+primeagricole_banque+primetransport_banque,
            nbrero_banque + nbrerno_banque + nbreassistauto_banque +nbrers_banque +nbreri_banque +nbreagricole_banque +nbretransport_banque,
            primero_banque + primerno_banque + primeassistauto_banque+ primers_banque+ primeri_banque+primeagricole_banque+primetransport_banque
            from premieredecate_banque where mois= %s and annee =%s """,(mois,annee,)) 
            
      
            etat2com = cur2.execute("""select 
            nbrero_banque,
            primero_banque,
            nbrerno_banque,
            primerno_banque,
            nbreassistauto_banque,
            primeassistauto_banque,
            nbrero_banque + nbrerno_banque + nbreassistauto_banque,
            primero_banque + primerno_banque + primeassistauto_banque,
            nbrers_banque,
            primers_banque,
            nbreri_banque,
            primeri_banque,
            nbreagricole_banque,
            primeagricole_banque,
            nbretransport_banque,
            primetransport_banque,
            nbreri_banque +nbreagricole_banque +nbretransport_banque ,
            primeri_banque+primeagricole_banque+primetransport_banque,
            nbrero_banque + nbrerno_banque + nbreassistauto_banque +nbrers_banque +nbreri_banque +nbreagricole_banque +nbretransport_banque,
            primero_banque + primerno_banque + primeassistauto_banque+ primers_banque+ primeri_banque+primeagricole_banque+primetransport_banque
            from premieredecate_banque where mois= %s and annee =cast(%s as integer)-1 """,(mois,annee,))

        elif (numd =='02'):
            etat1com = cur1.execute("""select 
            nbrero_banque,
            primero_banque,
            nbrerno_banque,
            primerno_banque,
            nbreassistauto_banque,
            primeassistauto_banque,
            nbrero_banque + nbrerno_banque + nbreassistauto_banque,
            primero_banque + primerno_banque + primeassistauto_banque,
            nbrers_banque,
            primers_banque,
            nbreri_banque,
            primeri_banque,
            nbreagricole_banque,
            primeagricole_banque,
            nbretransport_banque,
            primetransport_banque,
            nbreri_banque +nbreagricole_banque +nbretransport_banque ,
            primeri_banque+primeagricole_banque+primetransport_banque,
            nbrero_banque + nbrerno_banque + nbreassistauto_banque +nbrers_banque +nbreri_banque +nbreagricole_banque +nbretransport_banque,
            primero_banque + primerno_banque + primeassistauto_banque+ primers_banque+ primeri_banque+primeagricole_banque+primetransport_banque
            from deuxiemedecade_banque where mois= %s and annee =%s """,(mois,annee,)) 
            
      
            etat2com = cur2.execute("""select 
            nbrero_banque,
            primero_banque,
            nbrerno_banque,
            primerno_banque,
            nbreassistauto_banque,
            primeassistauto_banque,
            nbrero_banque + nbrerno_banque + nbreassistauto_banque,
            primero_banque + primerno_banque + primeassistauto_banque,
            nbrers_banque,
            primers_banque,
            nbreri_banque,
            primeri_banque,
            nbreagricole_banque,
            primeagricole_banque,
            nbretransport_banque,
            primetransport_banque,
            nbreri_banque +nbreagricole_banque +nbretransport_banque ,
            primeri_banque+primeagricole_banque+primetransport_banque,
            nbrero_banque + nbrerno_banque + nbreassistauto_banque +nbrers_banque +nbreri_banque +nbreagricole_banque +nbretransport_banque,
            primero_banque + primerno_banque + primeassistauto_banque+ primers_banque+ primeri_banque+primeagricole_banque+primetransport_banque
            from deuxiemedecade_banque where mois= %s and annee =cast(%s as integer)-1 """,(mois,annee,))


        elif (numd =='03'):
            etat1com = cur1.execute("""select 
            nbrero_banque,
            primero_banque,
            nbrerno_banque,
            primerno_banque,
            nbreassistauto_banque,
            primeassistauto_banque,
            nbrero_banque + nbrerno_banque + nbreassistauto_banque,
            primero_banque + primerno_banque + primeassistauto_banque,
            nbrers_banque,
            primers_banque,
            nbreri_banque,
            primeri_banque,
            nbreagricole_banque,
            primeagricole_banque,
            nbretransport_banque,
            primetransport_banque,
            nbreri_banque +nbreagricole_banque +nbretransport_banque ,
            primeri_banque+primeagricole_banque+primetransport_banque,
            nbrero_banque + nbrerno_banque + nbreassistauto_banque +nbrers_banque +nbreri_banque +nbreagricole_banque +nbretransport_banque,
            primero_banque + primerno_banque + primeassistauto_banque+ primers_banque+ primeri_banque+primeagricole_banque+primetransport_banque
            from troisiemedecade_banque where mois= %s and annee =%s """,(mois,annee,)) 
            
      
            etat2com = cur2.execute("""select 
            nbrero_banque,
            primero_banque,
            nbrerno_banque,
            primerno_banque,
            nbreassistauto_banque,
            primeassistauto_banque,
            nbrero_banque + nbrerno_banque + nbreassistauto_banque,
            primero_banque + primerno_banque + primeassistauto_banque,
            nbrers_banque,
            primers_banque,
            nbreri_banque,
            primeri_banque,
            nbreagricole_banque,
            primeagricole_banque,
            nbretransport_banque,
            primetransport_banque,
            nbreri_banque +nbreagricole_banque +nbretransport_banque ,
            primeri_banque+primeagricole_banque+primetransport_banque,
            nbrero_banque + nbrerno_banque + nbreassistauto_banque +nbrers_banque +nbreri_banque +nbreagricole_banque +nbretransport_banque,
            primero_banque + primerno_banque + primeassistauto_banque+ primers_banque+ primeri_banque+primeagricole_banque+primetransport_banque
            from troisiemedecade_banque where mois= %s and annee =cast(%s as integer)-1 """,(mois,annee,))
        result1 = cur1.fetchone()
        result2 = cur2.fetchone()
        if result1 is None :
            error  = "l'etat demandé n'est pos disponible !!!"
        if result2 is None : 
            flash(" Nous n'avons pas pu effectuer l'valuation car des  données passée ne sont plus disponible")   
        print(result1) 
        print(result2) 
        if error is None:

            return render_template('etatcomdecadepourlesbanqueassurance.html',session=session['nom'] ,numerod=numd, mois =mois,annee =annee , resultat =result1,resultat2 =result2 ,session2= session['mail']  )
     return render_template('formedecadepourlesbanquesass.html',error =error,session=session['nom'],session2= session['mail'] )  
@app.route("/etatcomdecadegenenbrecont",methods=('GET', 'POST'))
def etatcomdecadegenenbrecont():
     if request.method == 'POST':
        numd = request.form['numd']
        mois = request.form['mois']
        annee = request.form['annee']
        
        print (numd,mois, annee)
        db =db_connxion.get_cnn()
        error = None
        cur1 = db.cursor()
        cur2 = db.cursor()

        if (numd =='01'):
            etat1com = cur1.execute("""select agen.numagen,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_ro else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_rno else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_assistauto else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_ro else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_rno else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_assistauto else 0 end),

            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_rs else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_ri else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_agricole else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_transport else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_ri else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_agricole else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_transport else 0 end), 

            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_ro else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_rno else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_assistauto else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_rs else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_ri else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_agricole else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_transport else 0 end)
            from premieredecade_com p, agence_saa agen where p.mois= %s and p.annee =%s GROUP BY 1 ORDER BY 1 """,(mois,annee,)) 
            etat2com = cur2.execute("""select sum(nombre_ro),sum(nombre_rno), sum(nombre_assistauto), 
            sum(nombre_ro)+sum(nombre_rno)+ sum(nombre_assistauto),
            sum(nombre_rs),sum(nombre_ri), sum(nombre_agricole), sum(nombre_transport) ,
            sum(nombre_ri)+ sum(nombre_agricole)+ sum(nombre_transport) ,
            sum(nombre_ro)+sum(nombre_rno)+ sum(nombre_assistauto)+ sum(nombre_rs) +sum(nombre_ri)+ sum(nombre_agricole)+ sum(nombre_transport)
            from premieredecade_com  where mois= %s and annee =%s  """,(mois,annee,)) 


        elif (numd =='02'):
            etat1com = cur1.execute("""select agen.numagen,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_ro else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_rno else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_assistauto else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_ro else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_rno else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_assistauto else 0 end),

            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_rs else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_ri else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_agricole else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_transport else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_ri else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_agricole else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_transport else 0 end), 

            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_ro else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_rno else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_assistauto else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_rs else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_ri else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_agricole else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_transport else 0 end)
            from deuxiemedecade_com p, agence_saa agen where p.mois= %s and p.annee =%s GROUP BY 1 ORDER BY 1 """,(mois,annee,)) 
            etat2com = cur2.execute("""select sum(nombre_ro),sum(nombre_rno), sum(nombre_assistauto), 
            sum(nombre_ro)+sum(nombre_rno)+ sum(nombre_assistauto),
            sum(nombre_rs),sum(nombre_ri), sum(nombre_agricole), sum(nombre_transport) ,
            sum(nombre_ri)+ sum(nombre_agricole)+ sum(nombre_transport) ,
            sum(nombre_ro)+sum(nombre_rno)+ sum(nombre_assistauto)+ sum(nombre_rs) +sum(nombre_ri)+ sum(nombre_agricole)+ sum(nombre_transport)
            from deuxiemedecade_com  where mois= %s and annee =%s  """,(mois,annee,)) 


        elif (numd =='03'):
            etat1com = cur1.execute("""select agen.numagen,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_ro else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_rno else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_assistauto else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_ro else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_rno else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_assistauto else 0 end),

            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_rs else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_ri else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_agricole else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_transport else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_ri else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_agricole else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_transport else 0 end), 

            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_ro else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_rno else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_assistauto else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_rs else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_ri else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_agricole else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_transport else 0 end)
            from troisiemedecade_com p, agence_saa agen where p.mois= %s and p.annee =%s GROUP BY 1 ORDER BY 1 """,(mois,annee,)) 
            etat2com = cur2.execute("""select sum(nombre_ro),sum(nombre_rno), sum(nombre_assistauto), 
            sum(nombre_ro)+sum(nombre_rno)+ sum(nombre_assistauto),
            sum(nombre_rs),sum(nombre_ri), sum(nombre_agricole), sum(nombre_transport) ,
            sum(nombre_ri)+ sum(nombre_agricole)+ sum(nombre_transport) ,
            sum(nombre_ro)+sum(nombre_rno)+ sum(nombre_assistauto)+ sum(nombre_rs) +sum(nombre_ri)+ sum(nombre_agricole)+ sum(nombre_transport)
            from troisiemedecade_com  where mois= %s and annee =%s  """,(mois,annee,)) 
        result1 = cur1.fetchall()
        result2 = cur2.fetchone()
        if result1 is None :
            error  = "l'etat demandé n'est pos disponible !!!"
        
        print(result1) 
       
        if error is None:

            return render_template('etatcomdecadegenenbrecont.html',session=session['nom'] ,numerod=numd, mois =mois,annee =annee , resultat =result1 ,resultat2 =result2 ,session2= session['mail'] )
     return render_template('formecomdecadegeneralenbrecont.html',error =error,session=session['nom'],session2= session['mail'] )        
          
@app.route("/etatcomdecadegeneraleenprime",methods=('GET', 'POST'))
def etatcomdecadegeneraleenprime():
     if request.method == 'POST':
        numd = request.form['numd']
        mois = request.form['mois']
        annee = request.form['annee']
        
        print (numd,mois, annee)
        db =db_connxion.get_cnn()
        error = None
        cur1 = db.cursor()
        cur2 = db.cursor()

        if (numd =='01'):
            etat1com = cur1.execute("""select agen.numagen,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_ro else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_rno else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_assistauto else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_ro else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_rno else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_assistauto else 0 end),

            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_rs else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_ri else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_agricole else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_transport else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_ri else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_agricole else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_transport else 0 end), 

            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_ro else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_rno else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_assistauto else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_rs else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_ri else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_agricole else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_transport else 0 end)
            from premieredecade_com p, agence_saa agen where p.mois= %s and p.annee =%s GROUP BY 1 ORDER BY 1 """,(mois,annee,)) 
            etat2com = cur2.execute("""select sum(prime_ro),sum(prime_rno), sum(prime_assistauto), 
            sum(prime_ro)+sum(prime_rno)+ sum(prime_assistauto),
            sum(prime_rs),sum(prime_ri), sum(prime_agricole), sum(prime_transport) ,
            sum(prime_ri)+ sum(prime_agricole)+ sum(prime_transport),
            sum(prime_ro)+sum(prime_rno)+ sum(prime_assistauto)+ sum(prime_rs) +sum(prime_ri)+ sum(prime_agricole)+ sum(prime_transport) 
            from premieredecade_com  where mois= %s and annee =%s  """,(mois,annee,)) 


        elif (numd =='02'):
            etat1com = cur1.execute("""select agen.numagen,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_ro else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_rno else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_assistauto else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_ro else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_rno else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_assistauto else 0 end),

            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_rs else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_ri else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_agricole else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_transport else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_ri else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_agricole else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_transport else 0 end), 

            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_ro else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_rno else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_assistauto else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_rs else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_ri else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_agricole else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_transport else 0 end)
            from deuxiemedecade_com p, agence_saa agen where p.mois= %s and p.annee =%s GROUP BY 1 ORDER BY 1 """,(mois,annee,)) 
            etat2com = cur2.execute("""select sum(prime_ro),sum(prime_rno), sum(prime_assistauto), 
            sum(prime_ro)+sum(prime_rno)+ sum(prime_assistauto),
            sum(prime_rs),sum(prime_ri), sum(prime_agricole), sum(prime_transport) ,
            sum(prime_ri)+ sum(prime_agricole)+ sum(prime_transport) , 
            sum(prime_ro)+sum(prime_rno)+ sum(prime_assistauto)+ sum(prime_rs) +sum(prime_ri)+ sum(prime_agricole)+ sum(prime_transport)
            from deuxiemedecade_com  where mois= %s and annee =%s  """,(mois,annee,)) 


        elif (numd =='03'):
            etat1com = cur1.execute("""select agen.numagen,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_ro else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_rno else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_assistauto else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_ro else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_rno else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_assistauto else 0 end),

            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_rs else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_ri else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_agricole else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_transport else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_ri else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_agricole else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_transport else 0 end), 

            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_ro else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_rno else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_assistauto else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_rs else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_ri else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_agricole else 0 end) +
            sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_transport else 0 end)
            from troisiemedecade_com p, agence_saa agen where p.mois= %s and p.annee =%s GROUP BY 1 ORDER BY 1 """,(mois,annee,)) 
            etat2com = cur2.execute("""select sum(prime_ro),sum(prime_rno), sum(prime_assistauto), 
            sum(prime_ro)+sum(prime_rno)+ sum(prime_assistauto),
            sum(prime_rs),sum(prime_ri), sum(prime_agricole), sum(prime_transport) ,
            sum(prime_ri)+ sum(prime_agricole)+ sum(prime_transport) , 
            sum(prime_ro)+sum(prime_rno)+ sum(prime_assistauto)+ sum(prime_rs) +sum(prime_ri)+ sum(prime_agricole)+ sum(prime_transport)
            from troisiemedecade_com  where mois= %s and annee =%s  """,(mois,annee,)) 
        result1 = cur1.fetchall()
        result2 = cur2.fetchone()
        if result1 is None :
            error  = "l'etat demandé n'est pos disponible !!!"
        
        print(result1) 
       
        if error is None:

            return render_template('etatcomdecadegeneraleenprime.html',session=session['nom'] ,numerod=numd, mois =mois,annee =annee , resultat =result1 ,resultat2 =result2,session2= session['mail']  )
     return render_template('formecomdecadegeneraleenprime.html',error =error,session=session['nom'],session2= session['mail'] )        
          
@app.route("/etatcomcomparatifparagece",methods=('GET', 'POST'))
def etatcomcomparatifparagece():
     if request.method == 'POST':
        numd = request.form['numd']
        mois = request.form['mois']
        annee = request.form['annee']
        
        print (numd,mois, annee)
        db =db_connxion.get_cnn()
        error = None
        cur1 = db.cursor()
        cur2 = db.cursor()

        if (numd =='01'):
            etat1com = cur1.execute("""select agen.numagen,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.ro_encour else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.ro_passe else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.difference_ro else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.rno_encour else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.rno_passe else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.difference_rno else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.assistauto_encour else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.assistauto_passe else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.difference_assistauto else 0 end) , 

            sum(case when cast(p.numagen as integer)= agen.numagen then p.rs_encour else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.rs_passe else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.difference_rs else 0 end) ,
           
            sum(case when cast(p.numagen as integer)= agen.numagen then p.ri_encour else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.ri_passe else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.difference_ri else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.agricole_encour else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.agricole_passe else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.difference_agricole else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.transport_encour else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.transport_passe else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.difference_transport else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.totalenbre_encour else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.totalenbre_passe else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.totale_diff else 0 end)

            from premieredecate_diff p, agence_saa agen where p.mois= %s and p.annee =%s GROUP BY 1 ORDER BY 1 """,(mois,annee,)) 

            etat2com = cur2.execute("""select sum(ro_encour),sum(ro_passe),sum(difference_ro),sum(rno_encour),sum(rno_passe),sum(difference_rno) ,
            sum(assistauto_encour), sum(assistauto_passe), sum(difference_assistauto), sum(rs_encour), sum(rs_passe), 
            sum(difference_rs), sum(ri_encour),sum(ri_passe) ,sum(difference_ri ),sum(agricole_encour),sum(agricole_passe),sum(difference_agricole),
            sum(transport_encour), sum(transport_passe), sum(difference_transport ) , sum(totalenbre_encour),sum(totalenbre_passe) ,sum(totale_diff)
            from premieredecate_diff  where mois= %s and annee =%s """,(mois,annee,)) 
        elif (numd =='02'):
            etat1com = cur1.execute("""select agen.numagen,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.ro_encour else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.ro_passe else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.difference_ro else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.rno_encour else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.rno_passe else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.difference_rno else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.assistauto_encour else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.assistauto_passe else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.difference_assistauto else 0 end) , 

            sum(case when cast(p.numagen as integer)= agen.numagen then p.rs_encour else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.rs_passe else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.difference_rs else 0 end) ,
           
            sum(case when cast(p.numagen as integer)= agen.numagen then p.ri_encour else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.ri_passe else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.difference_ri else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.agricole_encour else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.agricole_passe else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.difference_agricole else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.transport_encour else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.transport_passe else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.difference_transport else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.totalenbre_encour else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.totalenbre_passe else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.totale_diff else 0 end)

            from deuxiemedecade_diff p, agence_saa agen where p.mois= %s and p.annee =%s GROUP BY 1 ORDER BY 1 """,(mois,annee,)) 
            etat2com = cur2.execute("""select sum(ro_encour),sum(ro_passe),sum(difference_ro),sum(rno_encour),sum(rno_passe),sum(difference_rno) ,
            sum(assistauto_encour), sum(assistauto_passe), sum(difference_assistauto), sum(rs_encour), sum(rs_passe), 
            sum(difference_rs), sum(ri_encour),sum(ri_passe) ,sum(difference_ri ),sum(agricole_encour),sum(agricole_passe),sum(difference_agricole),
            sum(transport_encour), sum(transport_passe), sum(difference_transport ) , sum(totalenbre_encour),sum(totalenbre_passe) ,sum(totale_diff)
            from deuxiemedecade_diff  where mois= %s and annee =%s """,(mois,annee,)) 
        elif (numd =='03'):
            etat1com = cur1.execute("""select agen.numagen,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.ro_encour else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.ro_passe else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.difference_ro else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.rno_encour else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.rno_passe else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.difference_rno else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.assistauto_encour else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.assistauto_passe else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.difference_assistauto else 0 end) , 

            sum(case when cast(p.numagen as integer)= agen.numagen then p.rs_encour else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.rs_passe else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.difference_rs else 0 end) ,
           
            sum(case when cast(p.numagen as integer)= agen.numagen then p.ri_encour else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.ri_passe else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.difference_ri else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.agricole_encour else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.agricole_passe else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.difference_agricole else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.transport_encour else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.transport_passe else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.difference_transport else 0 end) ,

            sum(case when cast(p.numagen as integer)= agen.numagen then p.totalenbre_encour else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.totalenbre_passe else 0 end) ,
            sum(case when cast(p.numagen as integer)= agen.numagen then p.totale_diff else 0 end)

            from troisiemedecade_diff p, agence_saa agen where p.mois= %s and p.annee =%s GROUP BY 1 ORDER BY 1 """,(mois,annee,)) 
            etat2com = cur2.execute("""select sum(ro_encour),sum(ro_passe),sum(difference_ro),sum(rno_encour),sum(rno_passe),sum(difference_rno) ,
            sum(assistauto_encour), sum(assistauto_passe), sum(difference_assistauto), sum(rs_encour), sum(rs_passe), 
            sum(difference_rs), sum(ri_encour),sum(ri_passe) ,sum(difference_ri ),sum(agricole_encour),sum(agricole_passe),sum(difference_agricole),
            sum(transport_encour), sum(transport_passe), sum(difference_transport ) , sum(totalenbre_encour),sum(totalenbre_passe) ,sum(totale_diff)
            from troisiemedecade_diff  where mois= %s and annee =%s """,(mois,annee,)) 
        result1 = cur1.fetchall()
        result2 = cur2.fetchone()
        if result1 == []: 
            error  = "l'etat demandé n'est pos disponible !!!"
        
        print(result1) 
       
        if error is None:

            return render_template('etatcomcomparatifparagece.html',session=session['nom'] ,numerod=numd, mois =mois,annee =annee , resultat =result1, resultat2 =result2,session2= session['mail'] )
     return render_template('formecomcomparatifderealisationparagence.html',error =error,session=session['nom'],session2= session['mail'] )        
          
@app.route("/etatcomcomparatifparbranche",methods=('GET', 'POST'))
def etatcomcomparatifparbranche():
     if request.method == 'POST':
        numd = request.form['numd']
        mois = request.form['mois']
        annee = request.form['annee']
        
        print (numd,mois, annee)
        db =db_connxion.get_cnn()
        error = None
        cur1 = db.cursor()
        cur2 = db.cursor()
        cur3 = db.cursor()
        cur4 = db.cursor()
        if (numd =='01'):
            etat1com = cur1.execute("""select
                nbrero_direct ,   
                primero_direct,  
                nbrerno_direct, 
                primerno_direct,   
                nbrers_direct , 
                primers_direct, 
                nbreri_direct ,  
                primeri_direct ,  
                nbreagricole_direct ,   
                primeagricole_direct, 
                nbretransport_direct,  
                primetransport_direct,    
                nbrero_prive,    
                primero_prive,   
                nbrerno_prive,  
                primerno_prive, 
                nbrers_prive,  
                primers_prive,     
                nbreri_prive,  
                primeri_prive, 
                nbreagricole_prive,   
                primeagricole_prive ,  
                nbretransport_prive,   
                primetransport_prive ,  
                nbrero_banque,    
                primero_banque,    
                nbrerno_banque ,
                primerno_banque,   
                nbrers_banque,    
                primers_banque,    
                nbreri_banque,  
                primeri_banque,   
                nbreagricole_banque,    
                primeagricole_banque,  
                nbretransport_banque,    
                primetransport_banque,     
                totalenbre_ro,  
                totalenbre_rno,    
                totalenbre_rs, 
                totalnbre_ri, 
                totalenbre_agricole,    
                totalenbre_transport, 
                totaleprime_ro, 
                totaleprime_rno, 
                totaleprime_rs ,
                totalenbre_ri,    
                totaleprime_agricole, 
                totaprime_transport
                 from premieredecate_comp  where mois= %s and annee =%s  """,(mois,annee,)) 

            etat3com = cur3.execute("""select
                 sum( nbrero_direct  +nbrerno_direct), sum(primero_direct+ primerno_direct),
                 sum( nbrero_prive  +nbrerno_prive), sum(primero_prive+ primerno_prive ),
                 sum( nbrero_banque  +nbrerno_banque), sum(primero_banque+ primerno_banque),
                 sum(totalenbre_ro +totalenbre_rno), sum(totaleprime_ro + totaleprime_rno),

                 sum(nbreri_direct + nbreagricole_direct+ nbretransport_direct),
                 sum(primeri_direct + primeagricole_direct+ primetransport_direct),
                 sum(nbreri_prive + nbreagricole_prive + nbretransport_prive ),
                 sum(primeri_prive  + primeagricole_prive + primetransport_prive ),
                 sum(nbreri_banque + nbreagricole_banque + nbretransport_banque ),
                 sum(primeri_banque  + primeagricole_banque + primetransport_banque ),
                 sum(totalnbre_ri +totalenbre_agricole +totalenbre_transport),
                 sum(totalenbre_ri + totaleprime_agricole + totaprime_transport),

                 sum(nbrero_direct  +nbrerno_direct + nbrers_direct +nbreri_direct + nbreagricole_direct + nbretransport_direct),
                 sum(primero_direct + nbrerno_direct +primers_direct +primeri_direct + primeagricole_direct+ primetransport_direct),

                 sum(nbrero_prive  +nbrerno_prive + nbrers_prive +nbreri_prive+ nbreagricole_prive + nbretransport_prive),
                 sum(primero_prive + primers_prive +primers_prive +primeri_prive  + primeagricole_prive + primetransport_prive),    


                 sum(nbrero_banque  +nbrerno_banque + nbrers_banque +nbreri_banque+ nbreagricole_banque + nbretransport_banque),
                 sum(primero_banque + primers_banque +primers_banque +primeri_banque  + primeagricole_banque + primetransport_banque),     
                 sum(totalenbre_ro +totalenbre_rno + totalnbre_ri +totalenbre_agricole +totalenbre_transport) ,
                 sum(totaleprime_ro + totaleprime_rno +totalenbre_ri + totaleprime_agricole + totaprime_transport)          
                 from premieredecate_comp  where mois= %s and annee = %s  """,(mois,annee,)) 


            etat2com = cur2.execute("""select
                 totalenbre_ro,totalenbre_rno,totalenbre_rs,totalnbre_ri,
                 totalenbre_agricole,totalenbre_transport,totaleprime_ro,totaleprime_rno,
                 totaleprime_rs,totalenbre_ri, totaleprime_agricole, totaprime_transport
                 from premieredecate_comp  where mois= %s and annee =cast(%s as integer)-1  """,(mois,annee,)) 

            etat4com = cur4.execute("""select
                sum(totalenbre_ro +totalenbre_rno),sum(totaleprime_ro + totaleprime_rno ),
                sum(totalnbre_ri + totalenbre_agricole + totalenbre_transport),
                sum(totalenbre_ri+ totaleprime_agricole+ totaprime_transport),
                sum(totalenbre_ro +totalenbre_rno +totalenbre_rs + totalnbre_ri + totalenbre_agricole + totalenbre_transport ),
                sum(totaleprime_ro + totaleprime_rno +totaleprime_rs +totalenbre_ri+ totaleprime_agricole+ totaprime_transport )
                 from premieredecate_comp  where mois= %s and annee =cast(%s as integer)-1  """,(mois,annee,)) 
        elif (numd =='02'):
            etat1com = cur1.execute("""select
                nbrero_direct ,   
                primero_direct,  
                nbrerno_direct, 
                primerno_direct,   
                nbrers_direct , 
                primers_direct, 
                nbreri_direct ,  
                primeri_direct ,  
                nbreagricole_direct ,   
                primeagricole_direct, 
                nbretransport_direct,  
                primetransport_direct,    
                nbrero_prive,    
                primero_prive,   
                nbrerno_prive,  
                primerno_prive, 
                nbrers_prive,  
                primers_prive,     
                nbreri_prive,  
                primeri_prive, 
                nbreagricole_prive,   
                primeagricole_prive ,  
                nbretransport_prive,   
                primetransport_prive ,  
                nbrero_banque,    
                primero_banque,    
                nbrerno_banque ,
                primerno_banque,   
                nbrers_banque,    
                primers_banque,    
                nbreri_banque,  
                primeri_banque,   
                nbreagricole_banque,    
                primeagricole_banque,  
                nbretransport_banque,    
                primetransport_banque,     
                totalenbre_ro,  
                totalenbre_rno,    
                totalenbre_rs, 
                totalnbre_ri, 
                totalenbre_agricole,    
                totalenbre_transport, 
                totaleprime_ro, 
                totaleprime_rno, 
                totaleprime_rs ,
                totalenbre_ri,    
                totaleprime_agricole, 
                totaprime_transport
                 from deuxiemedecade_comp  where mois= %s and annee =%s  """,(mois,annee,)) 

            etat3com = cur3.execute("""select
                 sum( nbrero_direct  +nbrerno_direct), sum(primero_direct+ primerno_direct),
                 sum( nbrero_prive  +nbrerno_prive), sum(primero_prive+ primerno_prive ),
                 sum( nbrero_banque  +nbrerno_banque), sum(primero_banque+ primerno_banque),
                 sum(totalenbre_ro +totalenbre_rno), sum(totaleprime_ro + totaleprime_rno),

                 sum(nbreri_direct + nbreagricole_direct+ nbretransport_direct),
                 sum(primeri_direct + primeagricole_direct+ primetransport_direct),
                 sum(nbreri_prive + nbreagricole_prive + nbretransport_prive ),
                 sum(primeri_prive  + primeagricole_prive + primetransport_prive ),
                 sum(nbreri_banque + nbreagricole_banque + nbretransport_banque ),
                 sum(primeri_banque  + primeagricole_banque + primetransport_banque ),
                 sum(totalnbre_ri +totalenbre_agricole +totalenbre_transport),
                 sum(totalenbre_ri + totaleprime_agricole + totaprime_transport),

                 sum(nbrero_direct  +nbrerno_direct + nbrers_direct +nbreri_direct + nbreagricole_direct + nbretransport_direct),
                 sum(primero_direct + nbrerno_direct +primers_direct +primeri_direct + primeagricole_direct+ primetransport_direct),

                 sum(nbrero_prive  +nbrerno_prive + nbrers_prive +nbreri_prive+ nbreagricole_prive + nbretransport_prive),
                 sum(primero_prive + primers_prive +primers_prive +primeri_prive  + primeagricole_prive + primetransport_prive),    


                 sum(nbrero_banque  +nbrerno_banque + nbrers_banque +nbreri_banque+ nbreagricole_banque + nbretransport_banque),
                 sum(primero_banque + primers_banque +primers_banque +primeri_banque  + primeagricole_banque + primetransport_banque),     
                 sum(totalenbre_ro +totalenbre_rno + totalnbre_ri +totalenbre_agricole +totalenbre_transport) ,
                 sum(totaleprime_ro + totaleprime_rno +totalenbre_ri + totaleprime_agricole + totaprime_transport)          
                 from deuxiemedecade_comp  where mois= %s and annee = %s  """,(mois,annee,)) 


            etat2com = cur2.execute("""select
                 totalenbre_ro,totalenbre_rno,totalenbre_rs,totalnbre_ri,
                 totalenbre_agricole,totalenbre_transport,totaleprime_ro,totaleprime_rno,
                 totaleprime_rs,totalenbre_ri, totaleprime_agricole, totaprime_transport
                 from deuxiemedecade_comp  where mois= %s and annee =cast(%s as integer)-1  """,(mois,annee,)) 

            etat4com = cur4.execute("""select
                sum(totalenbre_ro +totalenbre_rno),sum(totaleprime_ro + totaleprime_rno ),
                sum(totalnbre_ri + totalenbre_agricole + totalenbre_transport),
                sum(totalenbre_ri+ totaleprime_agricole+ totaprime_transport),
                sum(totalenbre_ro +totalenbre_rno +totalenbre_rs + totalnbre_ri + totalenbre_agricole + totalenbre_transport ),
                sum(totaleprime_ro + totaleprime_rno +totaleprime_rs +totalenbre_ri+ totaleprime_agricole+ totaprime_transport )
                 from deuxiemedecade_comp  where mois= %s and annee =cast(%s as integer)-1  """,(mois,annee,)) 
        elif (numd =='03'):
            etat1com = cur1.execute("""select
                nbrero_direct ,   
                primero_direct,  
                nbrerno_direct, 
                primerno_direct,   
                nbrers_direct , 
                primers_direct, 
                nbreri_direct ,  
                primeri_direct ,  
                nbreagricole_direct ,   
                primeagricole_direct, 
                nbretransport_direct,  
                primetransport_direct,    
                nbrero_prive,    
                primero_prive,   
                nbrerno_prive,  
                primerno_prive, 
                nbrers_prive,  
                primers_prive,     
                nbreri_prive,  
                primeri_prive, 
                nbreagricole_prive,   
                primeagricole_prive ,  
                nbretransport_prive,   
                primetransport_prive ,  
                nbrero_banque,    
                primero_banque,    
                nbrerno_banque ,
                primerno_banque,   
                nbrers_banque,    
                primers_banque,    
                nbreri_banque,  
                primeri_banque,   
                nbreagricole_banque,    
                primeagricole_banque,  
                nbretransport_banque,    
                primetransport_banque,     
                totalenbre_ro,  
                totalenbre_rno,    
                totalenbre_rs, 
                totalnbre_ri, 
                totalenbre_agricole,    
                totalenbre_transport, 
                totaleprime_ro, 
                totaleprime_rno, 
                totaleprime_rs ,
                totalenbre_ri,    
                totaleprime_agricole, 
                totaprime_transport
                 from troisiemedecade_comp  where mois= %s and annee =%s  """,(mois,annee,)) 

            etat3com = cur3.execute("""select
                 sum( nbrero_direct  +nbrerno_direct), sum(primero_direct+ primerno_direct),
                 sum( nbrero_prive  +nbrerno_prive), sum(primero_prive+ primerno_prive ),
                 sum( nbrero_banque  +nbrerno_banque), sum(primero_banque+ primerno_banque),
                 sum(totalenbre_ro +totalenbre_rno), sum(totaleprime_ro + totaleprime_rno),

                 sum(nbreri_direct + nbreagricole_direct+ nbretransport_direct),
                 sum(primeri_direct + primeagricole_direct+ primetransport_direct),
                 sum(nbreri_prive + nbreagricole_prive + nbretransport_prive ),
                 sum(primeri_prive  + primeagricole_prive + primetransport_prive ),
                 sum(nbreri_banque + nbreagricole_banque + nbretransport_banque ),
                 sum(primeri_banque  + primeagricole_banque + primetransport_banque ),
                 sum(totalnbre_ri +totalenbre_agricole +totalenbre_transport),
                 sum(totalenbre_ri + totaleprime_agricole + totaprime_transport),

                 sum(nbrero_direct  +nbrerno_direct + nbrers_direct +nbreri_direct + nbreagricole_direct + nbretransport_direct),
                 sum(primero_direct + nbrerno_direct +primers_direct +primeri_direct + primeagricole_direct+ primetransport_direct),

                 sum(nbrero_prive  +nbrerno_prive + nbrers_prive +nbreri_prive+ nbreagricole_prive + nbretransport_prive),
                 sum(primero_prive + primers_prive +primers_prive +primeri_prive  + primeagricole_prive + primetransport_prive),    


                 sum(nbrero_banque  +nbrerno_banque + nbrers_banque +nbreri_banque+ nbreagricole_banque + nbretransport_banque),
                 sum(primero_banque + primers_banque +primers_banque +primeri_banque  + primeagricole_banque + primetransport_banque),     
                 sum(totalenbre_ro +totalenbre_rno + totalnbre_ri +totalenbre_agricole +totalenbre_transport) ,
                 sum(totaleprime_ro + totaleprime_rno +totalenbre_ri + totaleprime_agricole + totaprime_transport)          
                 from troisiemedecade_comp  where mois= %s and annee = %s  """,(mois,annee,)) 


            etat2com = cur2.execute("""select
                 totalenbre_ro,totalenbre_rno,totalenbre_rs,totalnbre_ri,
                 totalenbre_agricole,totalenbre_transport,totaleprime_ro,totaleprime_rno,
                 totaleprime_rs,totalenbre_ri, totaleprime_agricole, totaprime_transport
                 from troisiemedecade_comp  where mois= %s and annee =cast(%s as integer)-1  """,(mois,annee,)) 

            etat4com = cur4.execute("""select
                sum(totalenbre_ro +totalenbre_rno),sum(totaleprime_ro + totaleprime_rno ),
                sum(totalnbre_ri + totalenbre_agricole + totalenbre_transport),
                sum(totalenbre_ri+ totaleprime_agricole+ totaprime_transport),
                sum(totalenbre_ro +totalenbre_rno +totalenbre_rs + totalnbre_ri + totalenbre_agricole + totalenbre_transport ),
                sum(totaleprime_ro + totaleprime_rno +totaleprime_rs +totalenbre_ri+ totaleprime_agricole+ totaprime_transport )
                 from troisiemedecade_comp  where mois= %s and annee =cast(%s as integer)-1  """,(mois,annee,)) 

        result1 = cur1.fetchone()
        result2 = cur2.fetchone()
        result3 = cur3.fetchone()
        result4 = cur4.fetchone()
        if result1 == []: 
            error  = "l'etat demandé n'est pos disponible !!!"
        if result2 is None : 
            error =" Nous nous pouvont pas effectuer l'valuation car des  données passée ne sont plus disponible"
        print(result1) 
        print(result2) 
        if error is None:

            return render_template('etatcomcomparatifparbranche.html',session=session['nom'] ,numerod=numd, mois =mois,annee =annee , resultat =result1, resultat2 =result2, resultat3 =result3,resultat4 =result4,session2= session['mail'] )
     return render_template('formecomcomparatifderealisationparabranche.html',error =error,session=session['nom'],session2= session['mail'] )  

@app.route("/etatrdcomparatifrppparagence",methods=('GET', 'POST'))
def etatrdcomparatifrppparagence():
     if request.method == 'POST':
        annee = request.form['annee']
        
        print ( annee)
        db =db_connxion.get_cnn()
        error = None
        cur1 = db.cursor()
        cur2 = db.cursor()
        cur3 = db.cursor()
        cur4 = db.cursor()
        etat1rd = cur1.execute("""select agen.numagen, agen.nomagen,
        sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_contrat else 0 end) ,
        sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_nette else 0 end) ,
        sum(case when cast(p.numagen as integer)= agen.numagen then p.acc else 0 end) ,
        sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_totale else 0 end) ,
        sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_totale else 0 end) 
        from comprpp_paragence p,agence_saa agen where p.annee = %s  GROUP BY 1,2 ORDER BY 1""",(annee,)) 
        totale1 = cur3.execute("""select sum(nombre_contrat), sum(prime_nette), sum(acc),sum(prime_totale), sum(rec_totale)
        from comprpp_paragence where annee = %s """,(annee,)) 
        etat2rd = cur2.execute("""select agen.numagen, agen.nomagen,
        sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_contrat else 0 end) ,
        sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_nette else 0 end) ,
        sum(case when cast(p.numagen as integer)= agen.numagen then p.acc else 0 end) ,
        sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_totale else 0 end) ,
        sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_totale else 0 end) 
        from comprpp_paragence p,agence_saa agen where p.annee =cast(%s as integer)-1   GROUP BY 1,2 ORDER BY 1""",(annee,)) 
        totale1 = cur4.execute("""select sum(nombre_contrat), sum(prime_nette), sum(acc),sum(prime_totale), sum(rec_totale)
        from comprpp_paragence where annee =cast(%s as integer)-1  """,(annee,)) 

        result1 = cur1.fetchall()
        result2 = cur2.fetchall()
        result3 = cur3.fetchone()
        result4 = cur4.fetchone()
        
      
        if result1 == []: 
            error  = "l'etat demandé n'est pos disponible !!!"
        if result2 == [] : 
            flash(" Nous n'avons pas pu effectuer l'valuation car des  données passée ne sont plus disponible")        
        print(result1)    
        print(result1) 
        print(result2) 
        if error is None:

            return render_template('etatrdcomparatifrppparagence.html',session=session['nom'] ,annee =annee , resultat =result1,resultat2 =result2,resultat3 = result3,resultat4 = result4,session2= session['mail'] )
     return render_template('formerdcomparatifrppparagence.html',error =error,session=session['nom'],session2= session['mail'] )       

@app.route("/etatrdcomparatifrppparproduit",methods=('GET', 'POST'))
def etatrdcomparatifrppparproduit():
     if request.method == 'POST':
        annee = request.form['annee']
        
        print ( annee)
        db =db_connxion.get_cnn()
        error = None
        cur1 = db.cursor()
        cur2 = db.cursor()
        cur3 = db.cursor()
        cur4 = db.cursor()
        etat1rd = cur1.execute("""select prod.numprod, prod.libprod,
        sum(case when cast(p.numprod as integer)= prod.numprod then p.nombre_contrat else 0 end) ,
        sum(case when cast(p.numprod as integer)= prod.numprod then p.cout_depolice else 0 end) ,
        sum(case when cast(p.numprod as integer)= prod.numprod then p.prime_emises else 0 end) ,
        sum(case when cast(p.numprod as integer)= prod.numprod then p.prime_nette else 0 end) ,
        sum(case when cast(p.numprod as integer)= prod.numprod then p.reserves_rec else 0 end) 
        from comprpp_parprod p,produit prod where prod.numbran >=12 and prod.numbran <=16 and  p.annee = %s  GROUP BY 1,2 ORDER BY 1""",(annee,)) 
       
        totale1 = cur3.execute("""select sum(nombre_contrat), sum(cout_depolice), sum(prime_emises),sum(prime_nette), sum(reserves_rec)
        from comprpp_parprod where annee = %s """,(annee,)) 
        etat2rd = cur2.execute("""select prod.numprod, prod.libprod,
        sum(case when cast(p.numprod as integer)= prod.numprod then p.nombre_contrat else 0 end) ,
        sum(case when cast(p.numprod as integer)= prod.numprod then p.cout_depolice else 0 end) ,
        sum(case when cast(p.numprod as integer)= prod.numprod then p.prime_emises else 0 end) ,
        sum(case when cast(p.numprod as integer)= prod.numprod then p.prime_nette else 0 end) ,
        sum(case when cast(p.numprod as integer)= prod.numprod then p.reserves_rec else 0 end) 
        from comprpp_parprod p,produit prod where prod.numbran >=12 and prod.numbran <=16 and  p.annee =cast(%s as integer)-1  GROUP BY 1,2 ORDER BY 1""",(annee,)) 

        totale1 = cur4.execute("""select sum(nombre_contrat), sum(cout_depolice), sum(prime_emises),sum(prime_nette), sum(reserves_rec)
        from comprpp_parprod where annee =cast(%s as integer)-1 """,(annee,))       
        result1 = cur1.fetchall()
        result2 = cur2.fetchall()
        result3 = cur3.fetchone()
        result4 = cur4.fetchone()
        if result1 == []: 
            error  = "l'etat demandé n'est pos disponible !!!"
        if result2 == [] : 
            flash(" Nous n'avons pas pu effectuer l'valuation car des  données passée ne sont plus disponible")                
        print(result1) 
        print(result2)   
       
        if error is None:

            return render_template('etatrdcomparatifrppparproduit.html',session=session['nom'] ,annee =annee , resultat =result1,  resultat2 =result2 , resultat3 =result3, resultat4 =result4,session2= session['mail'] )
     return render_template('formerdcomparatifrppparproduit.html',error =error,session=session['nom'],session2= session['mail'] )       


@app.route("/etatagericoleparprodparagence",methods=('GET', 'POST'))
def etatagericoleparprodparagence():
     if request.method == 'POST':
        mois = request.form['mois']
        annee = request.form['annee']
        prod = request.form['prod']
        print ( mois,annee, prod)
        db =db_connxion.get_cnn()
        error = None
        cur1 = db.cursor()
        cur2 = db.cursor()
        cur3 = db.cursor()
        cur4 = db.cursor()
        cur5 = db.cursor()
        if (prod =='1711'):
            etat1agri = cur1.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbrecont_1711 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_nette_1711 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.cout_police_1711 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_1711 else 0 end) 
              from productionagri_agenprod p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,))  
            etat2agri = cur2.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1711_83 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1711_84 else 0 end) ,
               sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1711_83 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1711_84 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1711_83 else 0 end),
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1711_84 else 0 end)
              from productionagri_garantie p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,)) 

            etat3agri = cur3.execute("""select libprod from produit where numprod = %s""",(prod,)) 

            etat4agri = cur4.execute("""select sum(p.prime1711_83),sum(p.prime1711_84), sum(p.rec1711_83), sum(p.rec1711_84),sum(p.nbre1711_83),
            sum(p.nbre1711_84)from  productionagri_garantie p where p.mois = %s and p.annee = %s """,(mois,annee,)) 

            etat5agri = cur5.execute("""select sum(cout_police_1711) from productionagri_agenprod where 
            mois = %s and annee = %s """,(mois,annee,)) 

        elif (prod =='1717'):
            etat1agri = cur1.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbrecont_1717 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_nette_1717 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.cout_police_1717 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_1717 else 0 end) 
              from productionagri_agenprod p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,))  
            etat2agri = cur2.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1717_85 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1717_86 else 0 end) ,
               sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1717_85 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1717_86 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1717_85 else 0 end),
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1717_86 else 0 end)
              from productionagri_garantie p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,)) 
           
            etat3agri = cur3.execute("""select libprod from produit where numprod = %s""",(prod,)) 
           
            etat4agri = cur4.execute("""select sum(p.prime1717_85),sum(p.prime1717_86), sum(p.rec1717_85), sum(p.rec1717_86),sum(p.nbre1717_85),
            sum(p.nbre1717_86)from  productionagri_garantie p where p.mois = %s and p.annee = %s """,(mois,annee,)) 
            etat5agri = cur5.execute("""select sum(cout_police_1717) from productionagri_agenprod where 
            mois = %s and annee = %s """,(mois,annee,))

        elif (prod =='1719'):
            etat1agri = cur1.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbrecont_1719 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_nette_1719 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.cout_police_1719 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_1719 else 0 end) 
              from productionagri_agenprod p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,))  
            etat2agri = cur2.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1719_87 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1719_88 else 0 end) ,
               sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1719_87 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1719_88 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1719_87 else 0 end),
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1719_88 else 0 end)
              from productionagri_garantie p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,)) 
            etat3agri = cur3.execute("""select libprod from produit where numprod = %s""",(prod,)) 
           
            etat4agri = cur4.execute("""select sum(p.prime1719_87),sum(p.prime1719_88), sum(p.rec1719_87), sum(p.rec1719_88),sum(p.nbre1719_87),
            sum(p.nbre1719_88)from  productionagri_garantie p where p.mois = %s and p.annee = %s """,(mois,annee,)) 
            etat5agri = cur5.execute("""select sum(cout_police_1719) from productionagri_agenprod where 
            mois = %s and annee = %s """,(mois,annee,))

        elif (prod =='1913'):
            etat1agri = cur1.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbrecont_1913 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_nette_1913 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.cout_police_1913 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_1913 else 0 end) 
              from productionagri_agenprod p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,))  
            etat2agri = cur2.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1913_82 else 0 end) ,
               sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1913_82 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1913_82 else 0 end)
              from productionagri_garantie p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,)) 

            etat3agri = cur3.execute("""select libprod from produit where numprod = %s""",(prod,)) 
           
            etat4agri = cur4.execute("""select sum(p.prime1913_82), sum(p.rec1913_82), sum(p.nbre1913_82)
            from  productionagri_garantie p where p.mois = %s and p.annee = %s """,(mois,annee,)) 
            etat5agri = cur5.execute("""select sum(cout_police_1913) from productionagri_agenprod where 
            mois = %s and annee = %s """,(mois,annee,))

        elif (prod =='1811'):
            etat1agri = cur1.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbrecont_1811 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_nette_1811 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.cout_police_1811 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_1811 else 0 end) 
              from productionagri_agenprod p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,))  
            etat2agri = cur2.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1811_91 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1811_92 else 0 end) ,
               sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1811_91 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1811_92 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1811_91 else 0 end),
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1811_92 else 0 end)
              from productionagri_garantie p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,)) 
            etat3agri = cur3.execute("""select libprod from produit where numprod = %s""",(prod,)) 
           
            etat4agri = cur4.execute("""select sum(p.prime1811_91),sum(p.prime1811_92), sum(p.rec1811_91), sum(p.rec1811_92),sum(p.nbre1811_91),
            sum(p.nbre1811_92)from  productionagri_garantie p where p.mois = %s and p.annee = %s """,(mois,annee,)) 
            etat5agri = cur5.execute("""select sum(cout_police_1811) from productionagri_agenprod where 
            mois = %s and annee = %s """,(mois,annee,))

        elif (prod =='1812'):
            etat1agri = cur1.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbrecont_1812 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_nette_1812 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.cout_police_1812 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_1812 else 0 end) 
              from productionagri_agenprod p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,))  
            etat2agri = cur2.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1812_93 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1812_94 else 0 end) ,
               sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1812_93 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1812_94 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1812_93 else 0 end),
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1812_94 else 0 end)
              from productionagri_garantie p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,)) 
            etat3agri = cur3.execute("""select libprod from produit where numprod = %s""",(prod,)) 
           
            etat4agri = cur4.execute("""select sum(p.prime1812_93),sum(p.prime1812_94), sum(p.rec1812_93), sum(p.rec1812_94),sum(p.nbre1812_93),
            sum(p.nbre1812_94)from  productionagri_garantie p where p.mois = %s and p.annee = %s """,(mois,annee,)) 
            etat5agri = cur5.execute("""select sum(cout_police_1812) from productionagri_agenprod where 
            mois = %s and annee = %s """,(mois,annee,))

        elif (prod =='1914'):
            etat1agri = cur1.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbrecont_1914 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_nette_1914 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.cout_police_1914 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_1914 else 0 end) 
              from productionagri_agenprod p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,))  
            etat2agri = cur2.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1914_89 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1914_90 else 0 end) ,
               sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1914_89 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1914_90 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1914_89 else 0 end),
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1914_90 else 0 end)
              from productionagri_garantie p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,)) 
            etat3agri = cur3.execute("""select libprod from produit where numprod = %s""",(prod,)) 
           
            etat4agri = cur4.execute("""select sum(p.prime1914_89),sum(p.prime1914_90), sum(p.rec1914_89), sum(p.rec1914_90),sum(p.nbre1914_89),
            sum(p.nbre1914_90)from  productionagri_garantie p where p.mois = %s and p.annee = %s """,(mois,annee,)) 
            etat5agri = cur5.execute("""select sum(cout_police_1914) from productionagri_agenprod where 
            mois = %s and annee = %s """,(mois,annee,))

        elif (prod =='1712'):
            etat1agri = cur1.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbrecont_1712 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_nette_1712 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.cout_police_1712 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_1712 else 0 end) 
              from productionagri_agenprod p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,))  
            etat2agri = cur2.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1914_89 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1914_90 else 0 end) ,
               sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1914_89 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1914_90 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1914_89 else 0 end),
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1914_90 else 0 end)
              from productionagri_garantie p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,)) 
            etat3agri = cur3.execute("""select libprod from produit where numprod = %s""",(prod,)) 
           
            etat4agri = cur4.execute("""select sum(p.nbrecont_1712),sum(p.prime_nette_1712), sum(p.cout_police_1712), sum(p.rec_1712)
            from  productionagri_agenprod p where p.mois = %s and p.annee = %s """,(mois,annee,)) 
            etat5agri = cur5.execute("""select sum(cout_police_1812) from productionagri_agenprod where 
            mois = %s and annee = %s """,(mois,annee,))

        elif (prod =='1713'):
            etat1agri = cur1.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbrecont_1713 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_nette_1713 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.cout_police_1713 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_1713 else 0 end) 
              from productionagri_agenprod p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,))  
            etat2agri = cur2.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1914_89 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1914_90 else 0 end) ,
               sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1914_89 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1914_90 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1914_89 else 0 end),
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1914_90 else 0 end)
              from productionagri_garantie p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,)) 
            etat3agri = cur3.execute("""select libprod from produit where numprod = %s""",(prod,)) 
           
            etat4agri = cur4.execute("""select sum(p.nbrecont_1713),sum(p.prime_nette_1713), sum(p.cout_police_1713), sum(p.rec_1713)
            from  productionagri_agenprod p where p.mois = %s and p.annee = %s """,(mois,annee,)) 
            etat5agri = cur5.execute("""select sum(cout_police_1812) from productionagri_agenprod where 
            mois = %s and annee = %s """,(mois,annee,))

        elif (prod =='1714'):
            etat1agri = cur1.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbrecont_1714 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_nette_1714 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.cout_police_1714 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_1714 else 0 end) 
              from productionagri_agenprod p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,))  
            etat2agri = cur2.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1914_89 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1914_90 else 0 end) ,
               sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1914_89 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1914_90 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1914_89 else 0 end),
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1914_90 else 0 end)
              from productionagri_garantie p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,)) 
            etat3agri = cur3.execute("""select libprod from produit where numprod = %s""",(prod,)) 
           
            etat4agri = cur4.execute("""select sum(p.nbrecont_1714),sum(p.prime_nette_1714), sum(p.cout_police_1714), sum(p.rec_1714)
            from  productionagri_agenprod p where p.mois = %s and p.annee = %s """,(mois,annee,)) 
            etat5agri = cur5.execute("""select sum(cout_police_1812) from productionagri_agenprod where 
            mois = %s and annee = %s """,(mois,annee,))

        elif (prod =='1715'):
            etat1agri = cur1.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbrecont_1715 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_nette_1715 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.cout_police_1715 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_1715 else 0 end) 
              from productionagri_agenprod p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,))  
            etat2agri = cur2.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1914_89 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1914_90 else 0 end) ,
               sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1914_89 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1914_90 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1914_89 else 0 end),
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1914_90 else 0 end)
              from productionagri_garantie p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,)) 
            etat3agri = cur3.execute("""select libprod from produit where numprod = %s""",(prod,)) 
           
            etat4agri = cur4.execute("""select sum(p.nbrecont_1715),sum(p.prime_nette_1715), sum(p.cout_police_1715), sum(p.rec_1715)
            from  productionagri_agenprod p where p.mois = %s and p.annee = %s """,(mois,annee,)) 
            etat5agri = cur5.execute("""select sum(cout_police_1812) from productionagri_agenprod where 
            mois = %s and annee = %s """,(mois,annee,))

        elif (prod =='1716'):
            etat1agri = cur1.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbrecont_1716 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_nette_1716 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.cout_police_1716 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_1716 else 0 end) 
              from productionagri_agenprod p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,))  
            etat2agri = cur2.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1914_89 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1914_90 else 0 end) ,
               sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1914_89 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1914_90 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1914_89 else 0 end),
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1914_90 else 0 end)
              from productionagri_garantie p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,)) 
            etat3agri = cur3.execute("""select libprod from produit where numprod = %s""",(prod,)) 
           
            etat4agri = cur4.execute("""select sum(p.nbrecont_1716),sum(p.prime_nette_1716), sum(p.cout_police_1716), sum(p.rec_1716)
            from  productionagri_agenprod p where p.mois = %s and p.annee = %s """,(mois,annee,)) 
            etat5agri = cur5.execute("""select sum(cout_police_1812) from productionagri_agenprod where 
            mois = %s and annee = %s """,(mois,annee,))
        elif (prod =='1718'):
            etat1agri = cur1.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbrecont_1718 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_nette_1718 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.cout_police_1718 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_1718 else 0 end) 
              from productionagri_agenprod p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,))  
            etat2agri = cur2.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1914_89 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1914_90 else 0 end) ,
               sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1914_89 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1914_90 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1914_89 else 0 end),
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1914_90 else 0 end)
              from productionagri_garantie p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,)) 
            etat3agri = cur3.execute("""select libprod from produit where numprod = %s""",(prod,)) 
           
            etat4agri = cur4.execute("""select sum(p.nbrecont_1718),sum(p.prime_nette_1718), sum(p.cout_police_1718), sum(p.rec_1718)
            from  productionagri_agenprod p where p.mois = %s and p.annee = %s """,(mois,annee,)) 
            etat5agri = cur5.execute("""select sum(cout_police_1812) from productionagri_agenprod where 
            mois = %s and annee = %s """,(mois,annee,))

        elif (prod =='1813'):
            etat1agri = cur1.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbrecont_1813 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_nette_1813 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.cout_police_1813 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_1813 else 0 end) 
              from productionagri_agenprod p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,))  
            etat2agri = cur2.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1914_89 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1914_90 else 0 end) ,
               sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1914_89 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1914_90 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1914_89 else 0 end),
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1914_90 else 0 end)
              from productionagri_garantie p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,)) 
            etat3agri = cur3.execute("""select libprod from produit where numprod = %s""",(prod,)) 
           
            etat4agri = cur4.execute("""select sum(p.nbrecont_1813),sum(p.prime_nette_1813), sum(p.cout_police_1813), sum(p.rec_1813)
            from  productionagri_agenprod p where p.mois = %s and p.annee = %s """,(mois,annee,)) 
            etat5agri = cur5.execute("""select sum(cout_police_1812) from productionagri_agenprod where 
            mois = %s and annee = %s """,(mois,annee,))

        elif (prod =='1814'):
            etat1agri = cur1.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbrecont_1814 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_nette_1814 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.cout_police_1814 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_1814 else 0 end) 
              from productionagri_agenprod p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,))  
            etat2agri = cur2.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1914_89 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1914_90 else 0 end) ,
               sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1914_89 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1914_90 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1914_89 else 0 end),
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1914_90 else 0 end)
              from productionagri_garantie p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,)) 
            etat3agri = cur3.execute("""select libprod from produit where numprod = %s""",(prod,)) 
           
            etat4agri = cur4.execute("""select sum(p.nbrecont_1814),sum(p.prime_nette_1814), sum(p.cout_police_1814), sum(p.rec_1814)
            from  productionagri_agenprod p where p.mois = %s and p.annee = %s """,(mois,annee,)) 
            etat5agri = cur5.execute("""select sum(cout_police_1812) from productionagri_agenprod where 
            mois = %s and annee = %s """,(mois,annee,))

        elif (prod =='1815'):
            etat1agri = cur1.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbrecont_1815 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_nette_1815 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.cout_police_1815 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_1815 else 0 end) 
              from productionagri_agenprod p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,))  
            etat2agri = cur2.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1914_89 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1914_90 else 0 end) ,
               sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1914_89 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1914_90 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1914_89 else 0 end),
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1914_90 else 0 end)
              from productionagri_garantie p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,)) 
            etat3agri = cur3.execute("""select libprod from produit where numprod = %s""",(prod,)) 
           
            etat4agri = cur4.execute("""select sum(p.nbrecont_1815),sum(p.prime_nette_1815), sum(p.cout_police_1815), sum(p.rec_1815)
            from  productionagri_agenprod p where p.mois = %s and p.annee = %s """,(mois,annee,)) 
            etat5agri = cur5.execute("""select sum(cout_police_1812) from productionagri_agenprod where 
            mois = %s and annee = %s """,(mois,annee,))

        elif (prod =='1816'):
            etat1agri = cur1.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbrecont_1816 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_nette_1816 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.cout_police_1816 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_1816 else 0 end) 
              from productionagri_agenprod p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,))  
            etat2agri = cur2.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1914_89 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1914_90 else 0 end) ,
               sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1914_89 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1914_90 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1914_89 else 0 end),
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1914_90 else 0 end)
              from productionagri_garantie p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,)) 
            etat3agri = cur3.execute("""select libprod from produit where numprod = %s""",(prod,)) 
           
            etat4agri = cur4.execute("""select sum(p.nbrecont_1816),sum(p.prime_nette_1816), sum(p.cout_police_1816), sum(p.rec_1816)
            from  productionagri_agenprod p where p.mois = %s and p.annee = %s """,(mois,annee,)) 
            etat5agri = cur5.execute("""select sum(cout_police_1812) from productionagri_agenprod where 
            mois = %s and annee = %s """,(mois,annee,))

        elif (prod =='1915'):
            etat1agri = cur1.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbrecont_1915 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_nette_1915 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.cout_police_1915 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_1915 else 0 end) 
              from productionagri_agenprod p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,))  
            etat2agri = cur2.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1914_89 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1914_90 else 0 end) ,
               sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1914_89 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1914_90 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1914_89 else 0 end),
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1914_90 else 0 end)
              from productionagri_garantie p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,)) 
            etat3agri = cur3.execute("""select libprod from produit where numprod = %s""",(prod,)) 
           
            etat4agri = cur4.execute("""select sum(p.nbrecont_1915),sum(p.prime_nette_1915), sum(p.cout_police_1915), sum(p.rec_1915)
            from  productionagri_agenprod p where p.mois = %s and p.annee = %s """,(mois,annee,)) 
            etat5agri = cur5.execute("""select sum(cout_police_1812) from productionagri_agenprod where 
            mois = %s and annee = %s """,(mois,annee,))
        elif (prod =='1916'):
            etat1agri = cur1.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbrecont_1916 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_nette_1916 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.cout_police_1916 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_1916 else 0 end) 
              from productionagri_agenprod p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,))  
            etat2agri = cur2.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1914_89 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1914_90 else 0 end) ,
               sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1914_89 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1914_90 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1914_89 else 0 end),
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1914_90 else 0 end)
              from productionagri_garantie p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,)) 
            etat3agri = cur3.execute("""select libprod from produit where numprod = %s""",(prod,)) 
           
            etat4agri = cur4.execute("""select sum(p.nbrecont_1916),sum(p.prime_nette_1916), sum(p.cout_police_1916), sum(p.rec_1916)
            from  productionagri_agenprod p where p.mois = %s and p.annee = %s """,(mois,annee,)) 
            etat5agri = cur5.execute("""select sum(cout_police_1812) from productionagri_agenprod where 
            mois = %s and annee = %s """,(mois,annee,))

        elif (prod =='1917'):
            etat1agri = cur1.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbrecont_1917 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_nette_1917 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.cout_police_1917 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_1917 else 0 end) 
              from productionagri_agenprod p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,))  
            etat2agri = cur2.execute("""select agen.numagen,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1914_89 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.prime1914_90 else 0 end) ,
               sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1914_89 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.rec1914_90 else 0 end) ,
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1914_89 else 0 end),
              sum(case when cast(p.numagen as integer)= agen.numagen then p.nbre1914_90 else 0 end)
              from productionagri_garantie p, agence_saa agen where p.mois = %s and p.annee = %s GROUP BY 1 ORDER BY 1""",(mois,annee,)) 
            etat3agri = cur3.execute("""select libprod from produit where numprod = %s""",(prod,)) 
           
            etat4agri = cur4.execute("""select sum(p.nbrecont_1917),sum(p.prime_nette_1917), sum(p.cout_police_1917), sum(p.rec_1917)
            from  productionagri_agenprod p where p.mois = %s and p.annee = %s """,(mois,annee,)) 
            etat5agri = cur5.execute("""select sum(cout_police_1812) from productionagri_agenprod where 
            mois = %s and annee = %s """,(mois,annee,))
        result1 = cur1.fetchall()
        result2 = cur2.fetchall()
        result3 = cur3.fetchone()
        result4 = cur4.fetchone()
        result5 = cur5.fetchone()
        if result1 == []: 
            error  = "l'etat demandé n'est pos disponible !!!"
               
        print(result1) 
        print(result2)   
       
        if error is None:

            return render_template('etatagericoleparprodparagence.html',session=session['nom'] ,prod= prod,mois=mois,annee =annee , resultat =result1,resultat2 =result2,resultat3 =result3, resultat4 =result4,resultat5 =result5,session2= session['mail'] )
     return render_template('formeagricoleagenceproduit.html',error =error,session=session['nom'],session2= session['mail'] )       

@app.route("/etatagricoleproductionmensuelle",methods=('GET', 'POST'))
def etatagricoleproductionmensuelle():
     if request.method == 'POST':
        mois = request.form['mois']
        annee = request.form['annee']
        print ( mois,annee)
        db =db_connxion.get_cnn()
        error = None
        cur1 = db.cursor()
        cur2 = db.cursor()
        cur3 = db.cursor()
        cur4 = db.cursor()
        etat1agri = cur1.execute("""select
        nbrecont_1711,
        cout_police_1711 ,
        nbrecont_1712,
        prime_nette_1712,
        cout_police_1712,
        rec_1712,
        nbrecont_1713,
        prime_nette_1713,
        cout_police_1713,
        rec_1713,
        nbrecont_1714,
        prime_nette_1714,
        cout_police_1714,
        rec_1714,
        nbrecont_1715,
        prime_nette_1715,
        cout_police_1715,
        rec_1715,
        nbrecont_1716,
        prime_nette_1716,
        cout_police_1716,
        rec_1716,
        nbrecont_1717,
        cout_police_1717,
        nbrecont_1718,
        prime_nette_1718,
        cout_police_1718,
        rec_1718,
        nbrecont_1719,     
        cout_police_1719,
        nbrecont_1811,    
        cout_police_1811, 
        nbrecont_1812,     
        cout_police_1812,
        nbrecont_1813,
        prime_nette_1813, 
        cout_police_1813,
        rec_1813,
        nbrecont_1814, 
        prime_nette_1814,
        cout_police_1814,
        rec_1814,
        nbrecont_1815, 
        prime_nette_1815,
        cout_police_1815,
        rec_1815,
        nbrecont_1816, 
        prime_nette_1816,
        cout_police_1816,
        rec_1816,          
        nbrecont_1913,
        cout_police_1913, 
        nbrecont_1914,
        cout_police_1914,
        nbrecont_1915,   
        prime_nette_1915,
        cout_police_1915,
        rec_1915,
        nbrecont_1916,
        prime_nette_1916,
        cout_police_1916,
        rec_1916,
        nbrecont_1917,
        prime_nette_1917,
        cout_police_1917,
        rec_1917
         from productionagri_agenprod where mois = %s and annee = %s""",(mois,annee,)) 
        etat2agri = cur3.execute("""select (nbrecont_1711 +nbrecont_1712+
        nbrecont_1713+nbrecont_1714 +nbrecont_1715 +nbrecont_1716 +
        nbrecont_1717+nbrecont_1718 +nbrecont_1719 +nbrecont_1811 +
        nbrecont_1812 + nbrecont_1813 +nbrecont_1814 +nbrecont_1815 +
        nbrecont_1816 +nbrecont_1913 +nbrecont_1914 +nbrecont_1915
        ),
        (cout_police_1711 +cout_police_1712+cout_police_1713 +
         cout_police_1714 +cout_police_1715 + cout_police_1716 +
        cout_police_1717+cout_police_1718 + cout_police_1719 +
        cout_police_1811 +cout_police_1812 +cout_police_1813 +
        cout_police_1814 +cout_police_1815 +cout_police_1816 +
        cout_police_1913 + cout_police_1914 +cout_police_1915 + 
        cout_police_1916 +cout_police_1917 ), 
        (prime_nette_1712 +prime_nette_1713 +prime_nette_1714 +prime_nette_1715 + 
        prime_nette_1716  +prime_nette_1718  +prime_nette_1813 +
        prime_nette_1814 +prime_nette_1815 +prime_nette_1816 +
        prime_nette_1915 +prime_nette_1916 +prime_nette_1917 ),
        (rec_1712 +rec_1713 +rec_1714 +rec_1715 + rec_1716 +
        rec_1717 +rec_1718 +rec_1719 +rec_1813 +rec_1814 +
        rec_1815 +rec_1816 +rec_1915 +rec_1916 +rec_1917)
         from productionagri_agenprod where mois = %s and annee = %s""",(mois,annee,))  
        etat2agri = cur2.execute("""select  
        prime1711_83,
        rec1711_83,
        nbre1711_83,
        prime1711_84,
        rec1711_84,
        nbre1711_84,
        prime1717_85,
        rec1717_85,
        nbre1717_85,
        prime1717_86,
        rec1717_86,
        nbre1717_86,
        prime1719_87, 
        rec1719_87,
        nbre1719_87,
        prime1719_88,
        rec1719_88,
        nbre1719_88,
        prime1811_91,
        rec1811_91,
        nbre1811_91,
        prime1811_92,    
        rec1811_92,
        nbre1811_92,
        prime1812_93,  
        rec1812_93,
        nbre1812_93,
        prime1812_94,
        rec1812_94,
        nbre1812_94,
        prime1913_82,  
        rec1913_82,
        nbre1913_82,
        prime1914_89, 
        rec1914_89,
        nbre1914_89,
        prime1914_90,
        rec1914_90,
        nbre1914_90
        
         from productionagri_garantie where mois = %s and annee = %s""",(mois,annee,)) 
        etat2agri = cur4.execute("""select (prime1711_83+prime1711_84 
        +prime1717_85 +prime1717_86 +prime1719_87 +prime1719_88 +
        prime1914_89 +prime1914_90 +prime1811_91 +prime1811_92 +
        prime1812_93 +prime1812_94 +prime1913_82 ),
        (rec1711_83+ rec1711_84 +rec1717_85 + rec1717_86 +
        rec1719_87 +rec1719_88 +rec1914_89 +rec1914_90 +
        rec1811_91 +rec1811_92 + rec1812_93 +rec1812_94 +
        rec1913_82 )
    
        from productionagri_garantie where mois = %s and annee = %s""",(mois,annee,)) 
        result1 = cur1.fetchone()
        result2 = cur2.fetchone()
        result3 = cur3.fetchone()
        result4 = cur4.fetchone()
        if result1 is None  : 
            error  = "l'etat demandé n'est pos disponible !!!"
               
        print(result1)
        print(result2) 
       
       
        if error is None:

            return render_template('etatagricoleproductionmensuelle.html',session=session['nom'] ,mois=mois,annee =annee , resultat =result1 , resultat2 =result2, resultat3 =result3, resultat4 =result4,session2= session['mail'] )
     return render_template('formeetatagricoleproductionmensuelle.html',error =error,session=session['nom'],session2= session['mail'] )       

@app.route("/etattransportaassurancemensuellenvxrenvx",methods=('GET', 'POST'))
def etattransportaassurancemensuellenvxrenvx():
     if request.method == 'POST':
        mois = request.form['mois']
        annee = request.form['annee']
        prod = request.form['prod']
        print ( mois,annee ,prod)
        db =db_connxion.get_cnn()
        error = None
        cur1 = db.cursor()
        cur2 = db.cursor()
        cur3 = db.cursor()
        etat1trans = cur1.execute("""select agen.numagen, p.libprod ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_nvx else 0 end),
         sum(case when cast(p.numagen as integer)= agen.numagen then p.primenette_nvx else 0 end),
         sum(case when cast(p.numagen as integer)= agen.numagen then p.cp_nvx else 0 end),
         sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_nvx else 0 end),

         sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_renvx else 0 end),
         sum(case when cast(p.numagen as integer)= agen.numagen then p.primenette_renvx else 0 end),
         sum(case when cast(p.numagen as integer)= agen.numagen then p.cp_renvx else 0 end),
         sum(case when cast(p.numagen as integer)= agen.numagen then p.rec_renvx else 0 end)
         from prodtransport_nvxrenvx p, agence_saa agen  where p.mois = %s and p.annee = %s and p.numprod = %s GROUP BY 1,2 ORDER BY 1""",(mois,annee,prod,))

        etat2trans = cur2.execute("""select libprod from produit where numprod = %s  """,(prod,))
        etat3trans = cur3.execute("""select sum(nombre_nvx), sum(primenette_nvx) , sum(cp_nvx), sum(rec_nvx), 
        sum(nombre_renvx), sum(primenette_renvx) , sum(cp_renvx), sum(rec_renvx)
        from prodtransport_nvxrenvx   where mois = %s and annee = %s and numprod = %s """,(mois,annee,prod,))
        result1 = cur1.fetchall()
        result2 = cur2.fetchone()
        result3 = cur3.fetchone()
        if result1 ==[]  : 
            error  = "l'etat demandé n'est pos disponible !!!"
               
        print(result1)
        
       
       
        if error is None:

            return render_template('etattransportaassurancemensuellenvxrenvx.html',session=session['nom'] ,mois=mois,annee =annee , resultat =result1 ,resultat2 =result2, resultat3 =result3 ,session2= session['mail'] )
     return render_template('formetransportetatassurance.html',error =error,session=session['nom'],session2= session['mail'] )       

@app.route("/etattransportproductionmensuelle",methods=('GET', 'POST'))
def etattransportproductionmensuelle():
     if request.method == 'POST':
        mois = request.form['mois']
        annee = request.form['annee']
        prod = request.form['prod']
        print ( mois,annee ,prod)
        db =db_connxion.get_cnn()
        error = None
        cur1 = db.cursor()
        cur2 = db.cursor()
        cur3 = db.cursor()
        etat1trans = cur1.execute("""select agen.numagen, p.libprod ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_contrat else 0 end),
         sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_nette else 0 end),
         sum(case when cast(p.numagen as integer)= agen.numagen then p.acc else 0 end),
         sum(case when cast(p.numagen as integer)= agen.numagen then p.rec else 0 end)
         from prodtransport_prodmenth p, agence_saa agen  where p.mois = %s and p.annee = %s and p.numprod = %s GROUP BY 1,2 ORDER BY 1""",(mois,annee,prod,))

        etat2trans = cur2.execute("""select libprod from produit where numprod = %s  """,(prod,))
        etat3trans = cur3.execute("""select sum(nombre_contrat), sum(prime_nette) , sum(acc), sum(rec)
        from prodtransport_prodmenth   where mois = %s and annee = %s and numprod = %s """,(mois,annee,prod,))
        result1 = cur1.fetchall()
        result2 = cur2.fetchone()
        result3 = cur3.fetchone()
        if result1 ==[]  : 
            error  = "l'etat demandé n'est pos disponible !!!"
               
        print(result1)
        
       
       
        if error is None:

            return render_template('etattransportproductionmensuelle.html',session=session['nom'] ,mois=mois,annee =annee , resultat =result1 ,resultat2 =result2, resultat3 =result3,session2= session['mail']  )
     return render_template('formetransportetatprodmensuelle.html',error =error,session=session['nom'],session2= session['mail'] )       

@app.route("/etatagricolerecapannuelle",methods=('GET', 'POST'))
def etatagricolerecapannuelle():
     if request.method == 'POST':
        annee = request.form['annee']
        prod = request.form['prod']
        print ( annee ,prod)
        db =db_connxion.get_cnn()
        error = None
        cur1 = db.cursor()
        cur2 = db.cursor()
        cur3 = db.cursor()
        etat1trans = cur1.execute("""select agen.numagen, p.libprod ,
         sum(case when cast(p.numagen as integer)= agen.numagen then p.nombre_contrat else 0 end),
         sum(case when cast(p.numagen as integer)= agen.numagen then p.prime_nette else 0 end),
         sum(case when cast(p.numagen as integer)= agen.numagen then p.acc else 0 end),
         sum(case when cast(p.numagen as integer)= agen.numagen then p.rec else 0 end)
         from prodtransport_prodmenth p, agence_saa agen  where  p.annee = %s and p.numprod = %s GROUP BY 1,2 ORDER BY 1""",(annee,prod,))

        etat2trans = cur2.execute("""select libprod from produit where numprod = %s  """,(prod,))
        etat3trans = cur3.execute("""select sum(nombre_contrat), sum(prime_nette) , sum(acc), sum(rec)
        from prodtransport_prodmenth   where  annee = %s and numprod = %s """,(annee,prod,))
        result1 = cur1.fetchall()
        result2 = cur2.fetchone()
        result3 = cur3.fetchone()
        if result1 ==[]  : 
            error  = "l'etat demandé n'est pos disponible !!!"
               
        print(result1)
        
       
       
        if error is None:

            return render_template('etatagricolerecapannuelle.html',session=session['nom'] ,annee =annee , resultat =result1 ,resultat2 =result2, resultat3 =result3,session2= session['mail']  )
     return render_template('formeagricolereacapeannuelle.html',error =error,session=session['nom'],session2= session['mail'] )       

@app.route("/etattransportreacpeparproduit",methods=('GET', 'POST'))
def etattransportreacpeparproduit():
     if request.method == 'POST':
        mois = request.form['mois']
        annee = request.form['annee']
        
        print ( mois,annee)
        db =db_connxion.get_cnn()
        error = None
        cur1 = db.cursor()
        cur3 = db.cursor()
        etat1trans = cur1.execute("""select prod.numprod,prod.libprod,
         sum(case when cast(p.numprod as integer)= prod.numprod then p.nombre_contrat else 0 end),
         sum(case when cast(p.numprod as integer)= prod.numprod then p.prime_nette else 0 end),
         sum(case when cast(p.numprod as integer)= prod.numprod then p.acc else 0 end),
         sum(case when cast(p.numprod as integer)= prod.numprod then p.rec else 0 end)
         from prodtransport_prodmenth p, produit prod  where prod.numbran >=20 and prod.numbran <=22 and p.mois = %s and p.annee = %s GROUP BY 1,2 ORDER BY 1""",(mois,annee,))

        etat3trans = cur3.execute("""select sum(nombre_contrat), sum(prime_nette) , sum(acc), sum(rec)
        from prodtransport_prodmenth   where  mois = %s and annee = %s """,(mois,annee,))
        result1 = cur1.fetchall()
        result3 = cur3.fetchone()
        if result1 ==[]  : 
            error  = "l'etat demandé n'est pos disponible !!!"
               
        print(result1)
        
       
       
        if error is None:

            return render_template('etattransportreacpeparproduit.html',session=session['nom'] ,mois = mois,annee =annee , resultat =result1 , resultat3 =result3,session2= session['mail']  )
     return render_template('formetransportrecapeparproduit.html',error =error,session=session['nom'],session2= session['mail'] )       

@app.route("/etatautosinistrematavechono" ,methods=('GET', 'POST'))
def etatautosinistrematavechono():
     if request.method == 'POST':
        mois = request.form['mois']
        annee = request.form['annee']
        print (mois, annee)
        months = dict(jan=1, feb=2, mar=3,apr=4,may=5, jun=6,jul=7, aug=8, Sep=9,oct=10,nov=11,dec=12 )
        print(months[mois])
        sut = months[mois] -1
        print(sut)
        db =db_connxion.get_cnn()
        error = None
        cur1 = db.cursor()
        cur2 = db.cursor()
        cur3 = db.cursor()
        cur4 = db.cursor()
        etatsini1 = cur1.execute("""select agen.numagen , 
         sum( case when (stk.numagen = agen.numagen) then  stk.nombre_ancienstk else 0 end) ,
         sum(case when stk.numagen = agen.numagen then stk.nombre_declarer else 0 end) ,
         sum(case when stk.numagen = agen.numagen then stk.nombre_regle else 0 end) ,

         (sum( case when (stk.numagen = agen.numagen) then  stk.nombre_ancienstk else 0 end)  +
         sum(case when stk.numagen = agen.numagen then stk.nombre_declarer else 0 end)- 
         sum(case when stk.numagen = agen.numagen then stk.nombre_regle else 0 end)),
         sum (((case when stk.numagen = agen.numagen then stk.nombre_regle else 0 end) * 100) / (case when stk.numagen = agen.numagen then stk.nombre_declarer else 1 end))::integer,
         sum(case when stk.numagen = agen.numagen then stk.reglement else 0 end) ,
         sum(case when stk.numagen = agen.numagen then stk.honoraire else 0 end) 
         from agence_saa agen,sinistremat_nvxstok stk  where  stk.mois = %s and stk.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

        etatsini2 = cur2.execute("""select sum (stk.nombre_ancienstk),sum (stk.nombre_declarer),  sum (  stk.nombre_regle),
        sum ( stk.nombre_ancienstk)+sum (stk.nombre_declarer)- sum (  stk.nombre_regle),
        (sum(stk.nombre_regle) * 100 / sum(stk.nombre_declarer))::integer, sum(stk.reglement )
        from  sinistremat_nvxstok stk  where   mois = %s and annee =%s  """,(mois,annee,)) 
        if sut == 0 :
            etatsini1 = cur3.execute("""select agen.numagen ,
            sum( case when (stk.numagen = agen.numagen) then  stk.nvx_stk else 0 end) 
            from agence_saa agen,sinistremat_nvxstok stk  where  stk.mois =to_char(to_timestamp(to_char(date_part('MON', to_timestamp('dec', ' mon')::date) -1,'999'),'MM'), 'mon')  and cast(stk.annee as integer) =%s-1   GROUP BY 1 ORDER BY 1""",(annee,))
            etatsini1 = cur4.execute("""select  sum( stk.nvx_stk)  
            from sinistremat_nvxstok stk  where  stk.mois =to_char(to_timestamp(to_char(date_part('MON', to_timestamp('dec', ' mon')::date) -1,'999'),'MM'), 'mon')  and cast(stk.annee as integer) =%s-1  """,(annee,))
            
        else:

            etatsini1 = cur3.execute("""select agen.numagen ,
            sum( case when (stk.numagen = agen.numagen) then  stk.nvx_stk else 0 end) 
            from agence_saa agen,sinistremat_nvxstok stk  where  stk.mois =to_char(to_timestamp(to_char(date_part('MON', to_timestamp(%s, ' mon')::date) -1,'999'),'MM'), 'mon')  and stk.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))
            etatsini1 = cur4.execute("""select  sum( stk.nvx_stk)  
            from sinistremat_nvxstok stk  where  stk.mois =to_char(to_timestamp(to_char(date_part('MON', to_timestamp(%s, ' mon')::date) -1,'999'),'MM'), 'mon')  and stk.annee =%s  """,(mois,annee,))

        result1 = cur1.fetchall()
        result2 = cur2.fetchone()
        result3 = cur3.fetchall()
        result4 = cur4.fetchone()
       
        print(result1 )
        print(result2 )
        print(result3 )
         
        datenow = datetime.now()
        date_finmois = datetime(datenow.year, datenow.month, 1) + relativedelta(months=1, days=-1) 
       
        print(datenow)
        anneeact = datenow.year
        moisact = datenow.month
        print(type(months[mois]))
        print(type(moisact))
        print(date_finmois )                        
        print( anneeact)
        print( moisact)
        if date_finmois > datenow and months[mois]== moisact and int(annee)== anneeact: 
            error = "l'etat que vous_avez demandée n'est pas encore prét"
        if result1 == []: 
            error ="l'etat n'est pas disponible  "
        if error is None:
            return render_template('etatautosinistrematavechono.html',session=session['nom'],resultats1 =result1,resultats2 =result2,resultats3 =result3,mois =mois,annee =annee, resultats4 =result4,session2= session['mail']  )
     return render_template('formeetatautosinistrematahmoi.html',error =error,session=session['nom'],session2= session['mail'] )  
    
@app.route("/etatsinistrecorporel" ,methods=('GET', 'POST'))
def etatsinistrecorporel():
     if request.method == 'POST':
        mois = request.form['mois']
        annee = request.form['annee']
        print (mois, annee)
        months = dict(jan=1, feb=2, mar=3,apr=4,may=5, jun=6,jul=7, aug=8, Sep=9,oct=10,nov=11,dec=12 )
        print(months[mois])
        sut = months[mois] -1
        print(sut)
        db =db_connxion.get_cnn()
        error = None
        cur1 = db.cursor()
        cur2 = db.cursor()
        cur3 = db.cursor()
        cur4 = db.cursor()
        etatsini1 = cur1.execute("""select agen.numagen , 
         sum( case when (stk.numagen = agen.numagen) then  stk.nombre_ancienstk else 0 end) ,
         sum(case when stk.numagen = agen.numagen then stk.nombre_declarer else 0 end) ,
         sum(case when stk.numagen = agen.numagen then stk.nombre_regle else 0 end) ,

         (sum( case when (stk.numagen = agen.numagen) then  stk.nombre_ancienstk else 0 end)  +
         sum(case when stk.numagen = agen.numagen then stk.nombre_declarer else 0 end)- 
         sum(case when stk.numagen = agen.numagen then stk.nombre_regle else 0 end)),
         sum (((case when stk.numagen = agen.numagen then stk.nombre_regle else 0 end) * 100) / (case when stk.numagen = agen.numagen then stk.nombre_declarer else 1 end))::integer,
         sum(case when stk.numagen = agen.numagen then stk.reglement else 0 end) 
         from agence_saa agen,sinistrecorp_nvxstok stk  where  stk.mois = %s and stk.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))

        etatsini2 = cur2.execute("""select sum (stk.nombre_ancienstk),sum (stk.nombre_declarer),  sum (  stk.nombre_regle),
        sum ( stk.nombre_ancienstk)+sum (stk.nombre_declarer)- sum (  stk.nombre_regle),
        (sum(stk.nombre_regle) * 100 / sum(stk.nombre_declarer))::integer, sum(stk.reglement )
        from  sinistrecorp_nvxstok stk  where   mois = %s and annee =%s  """,(mois,annee,)) 
        if sut == 0 :
            etatsini1 = cur3.execute("""select agen.numagen ,
            sum( case when (stk.numagen = agen.numagen) then  stk.nvx_stk else 0 end) 
            from agence_saa agen,sinistrecorp_nvxstok stk  where  stk.mois =to_char(to_timestamp(to_char(date_part('MON', to_timestamp('dec', ' mon')::date) -1,'999'),'MM'), 'mon')  and cast(stk.annee as integer) =%s-1   GROUP BY 1 ORDER BY 1""",(annee,))
            etatsini1 = cur4.execute("""select  sum( stk.nvx_stk)  
            from sinistrecorp_nvxstok stk  where  stk.mois =to_char(to_timestamp(to_char(date_part('MON', to_timestamp('dec', ' mon')::date) -1,'999'),'MM'), 'mon')  and cast(stk.annee as integer) =%s-1  """,(annee,))
            
        else:

            etatsini1 = cur3.execute("""select agen.numagen ,
            sum( case when (stk.numagen = agen.numagen) then  stk.nvx_stk else 0 end) 
            from agence_saa agen,sinistrecorp_nvxstok stk  where  stk.mois =to_char(to_timestamp(to_char(date_part('MON', to_timestamp(%s, ' mon')::date) -1,'999'),'MM'), 'mon')  and stk.annee =%s  GROUP BY 1 ORDER BY 1""",(mois,annee,))
            etatsini1 = cur4.execute("""select  sum( stk.nvx_stk)  
            from sinistrecorp_nvxstok stk  where  stk.mois =to_char(to_timestamp(to_char(date_part('MON', to_timestamp(%s, ' mon')::date) -1,'999'),'MM'), 'mon')  and stk.annee =%s  """,(mois,annee,))

        result1 = cur1.fetchall()
        result2 = cur2.fetchone()
        result3 = cur3.fetchall()
        result4 = cur4.fetchone()
       
        print(result1 )
        print(result2 )
        print(result3 )
         
        datenow = datetime.now()
        date_finmois = datetime(datenow.year, datenow.month, 1) + relativedelta(months=1, days=-1) 
       
        print(datenow)
        anneeact = datenow.year
        moisact = datenow.month
        print(type(months[mois]))
        print(type(moisact))
        print(date_finmois )                        
        print( anneeact)
        print( moisact)
        if date_finmois > datenow and months[mois]== moisact and int(annee)== anneeact: 
            error = "l'etat que vous_avez demandée n'est pas encore prét"
        if result1 == []: 
            error ="l'etat n'est pas disponible  "
        if error is None:
            return render_template('etatsinistrecorporel.html',session=session['nom'],resultats1 =result1,resultats2 =result2,resultats3 =result3,mois =mois,annee =annee ,resultats4 =result4,session2= session['mail'] )
     return render_template('formeetatautosinstrecorp.html',error =error,session=session['nom'],session2= session['mail'] )  

@app.route("/sendmail",methods=('GET', 'POST'))
def sendmail():
  if request.method == 'POST':
    mail1 = request.form['mail']
    objet = request.form['objet']
    contenu = request.form['contenu']
    print (mail1, objet,contenu)
    db =db_connxion.get_cnn()
    error = None
    cur1 = db.cursor()
    cur1.execute("""select emailagen from agence_saa where emailagen = %s  """,(mail1,))
    resul = cur1.fetchone()
    if resul is not None :
        msg = Message(objet,sender="kds781228@gmail.com", recipients = [mail1])
        msg.body = contenu
        mail.send(msg)
        flash ("votre message a été envoyer avec succé")
        if error is None:
            return render_template('formulaire_send_auto.html',session=session['nom'],session2= session['mail'] )
    else : 
        error ="l'email que vous avez saisie ne correspond a aucune agence"
        return render_template('formulaire_send_auto.html',session=session['nom'], error = error,session2= session['mail'] )


@app.route("/sendmailcom",methods=('GET', 'POST'))
def sendmailcom():
  if request.method == 'POST':
    mail1 = request.form['mail']
    objet = request.form['objet']
    contenu = request.form['contenu']
    print (mail1, objet,contenu)
    db =db_connxion.get_cnn()
    error = None
    cur1 = db.cursor()
    cur1.execute("""select emailagen from agence_saa where emailagen = %s  """,(mail1,))
    resul = cur1.fetchone()
    if resul is not None :
        msg = Message(objet,sender="kds781228@gmail.com", recipients = [mail1])
        msg.body = contenu
        mail.send(msg)
        flash ("votre message a été envoyer avec succé")
        if error is None:
            return render_template('formulaire_send_com.html',session=session['nom'],session2= session['mail'] )
    else : 
        error ="l'email que vous avez saisie ne correspond a aucune agence"
        return render_template('formulaire_send_com.html',session=session['nom'], error = error,session2= session['mail'] )


@app.route("/sendmailirdt",methods=('GET', 'POST'))
def sendmailirdt():
  if request.method == 'POST':
    mail1 = request.form['mail']
    objet = request.form['objet']
    contenu = request.form['contenu']
    print (mail1, objet,contenu)
    db =db_connxion.get_cnn()
    error = None
    cur1 = db.cursor()
    cur1.execute("""select emailagen from agence_saa where emailagen = %s  """,(mail1,))
    resul = cur1.fetchone()
    if resul is not None :
        msg = Message(objet,sender="kds781228@gmail.com", recipients = [mail1])
        msg.body = contenu
        mail.send(msg)
        flash ("votre message a été envoyer avec succé")
        if error is None:
            return render_template('formulaire_send_irdt.html',session=session['nom'],session2= session['mail'] )
    else : 
        error ="l'email que vous avez saisie ne correspond a aucune agence"
        return render_template('formulaire_send_irdt.html',session=session['nom'], error = error,session2= session['mail'] )
app.secret_key = 'the random string'
Bootstrap(app)
#run the app
if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 8080, app, use_debugger=True, use_reloader=True)
