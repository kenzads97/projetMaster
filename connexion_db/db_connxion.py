import psycopg2
import click
from flask import current_app, g
from flask.cli import with_appcontext
from dateutil.relativedelta import relativedelta
from datetime import date

try:
    conn = psycopg2.connect(
        user = "postgres",
        password = "kenza",
        host = "localhost",
        port = "5432",
        database = "db_saa" )
    
    cur = conn.cursor()
 
    cur.execute("select * from dblink_connect('2001','host=localhost user=postgres password=kenza dbname=db_2001');")
    cur.execute("select * from dblink_connect('2002','host=localhost user=postgres password=kenza dbname=db_2002');")
    cur.execute("select * from dblink_connect('2003','host=localhost user=postgres password=kenza dbname=db_2003');")
    cur.execute("select * from dblink_connect('2004','host=localhost user=postgres password=kenza dbname=db_2004');")
    cur.execute("select * from dblink_connect('2005','host=localhost user=postgres password=kenza dbname=db_2005');")
    cur.execute("select * from dblink_connect('2052','host=localhost user=postgres password=kenza dbname=db_2052');")
    cur.execute("select * from dblink_connect('2054','host=localhost user=postgres password=kenza dbname=db_2054');")
    cur.execute("select * from dblink_connect('2056','host=localhost user=postgres password=kenza dbname=db_2056');")
    cur.execute("select * from dblink_connect('2059','host=localhost user=postgres password=kenza dbname=db_2059');")
    cur.execute("select * from dblink_connect('2060','host=localhost user=postgres password=kenza dbname=db_2060');")
    cur.execute("select * from dblink_connect('13401','host=localhost user=postgres password=kenza dbname=db_13401');")
    cur.execute("select * from dblink_connect('13402','host=localhost user=postgres password=kenza dbname=db_13402');")
    cur.execute("select * from dblink_connect('13403','host=localhost user=postgres password=kenza dbname=db_13403');")
    cur.execute("select * from dblink_connect('13404','host=localhost user=postgres password=kenza dbname=db_13404');")
    cur.execute("select * from dblink_connect('13405','host=localhost user=postgres password=kenza dbname=db_13405');")
    cur.execute("REFRESH MATERIALIZED VIEW contrat_police;")   
    conn.commit()
   

    def get_cnn():
        if 'conn' not in g:
            g.conn = psycopg2.connect(
                user = "postgres",
                password = "kenza",
                host = "localhost",
                port = "5432",
                database = "db_saa"
            )
               
        return g.conn
    def rafrech_monauto():
        db = get_cnn() 
        cur1 = get_cnn() .cursor()
        datenow = date.today()
        anneeact = datenow.year
        moisact = datenow.month
        date_finmois = date(datenow.year, datenow.month, 1) + relativedelta(months=1, days=-1)
        print(datenow)
        print(datenow)
        if  datenow == date_finmois :
            ref1 =cur1.execute(""" refresh materialized view statprodauto """)
            ref2 =cur1.execute(""" refresh materialized view prodpargaraparagen """)
            ref2 =cur1.execute(""" refresh materialized view sinistre_corporel """)
            ref2 =cur1.execute(""" refresh materialized view sinistre_materiel """)
            ref2 =cur1.execute(""" refresh materialized view sinistrecorp_declare """)
            ref2 =cur1.execute(""" refresh materialized view sinistrecorp_regle """)
            ref2 =cur1.execute(""" refresh materialized view sinistrecorp_ancienstok """)
            ref2 =cur1.execute(""" refresh materialized view sinistrecorp_nvxstok """)
            ref2 =cur1.execute(""" refresh materialized view sinistremat_declare """)
            ref2 =cur1.execute(""" refresh materialized view sinistremat_regle """)
            ref2 =cur1.execute(""" refresh materialized view sinistremat_ancienstok """)
            ref2 =cur1.execute(""" refresh materialized view sinistremat_nvxstok """)
            cur1.execute(""" insert into message_auto(id_msgauto , titre_msg, contenu1_msg,contenu2_msg, date) values ((SELECT MAX(id_msgauto)+1 from message_auto),
            'production' ,'les etats stat mensuelle du service production ',' pour le mois %s et l"année %s est disponible ',%s)""",(moisact,anneeact,datenow,))
            cur1.execute(""" insert into message_auto(id_msgauto , titre_msg, contenu1_msg,contenu2_msg, date) values ((SELECT MAX(id_msgauto)+1 from message_auto),
            'sinistre' ,'les etats stat mensuelle du service sinistre ',' pour le mois %s et l"année %s est disponible ',%s)""",(moisact,anneeact,datenow,))
            db.commit()
 

    def rafrech_decadecom():
        db = get_cnn() 
        cur1 = get_cnn() .cursor()
        datenow = date.today()
        anneeact = datenow.year
        moisact = datenow.month
        decade1 = date(datenow.year, datenow.month, 10)
        decade2 = date(datenow.year, datenow.month,20)
        decade3 = date(datenow.year, datenow.month, 1) + relativedelta(months=1, days=-1)
       
        if  (datenow == decade1) :
            ref1 =cur1.execute(""" refresh materialized view premieredecadersriagritrans_com """)
            ref2 =cur1.execute(""" refresh materialized view premieredecade_com """)
            ref2 =cur1.execute(""" refresh materialized view premieredecate_anc """)
            ref2 =cur1.execute(""" refresh materialized view premieredecate_nvx """)
            ref2 =cur1.execute(""" refresh materialized view premieredecate_diff """)
            ref2 =cur1.execute(""" refresh materialized view premieredecate_directe """)
            ref2 =cur1.execute(""" refresh materialized view premieredecate_banque """)
            ref2 =cur1.execute(""" refresh materialized view premieredecate_prive """)
            ref2 =cur1.execute(""" refresh materialized view premieredecate_comp """)
            cur1.execute(""" insert into message_com(id_msgcom , titre_msg, contenu1_msg,contenu2_msg, date) values ((SELECT MAX(id_msgcom)+1 from message_com),
            'Decade Numéro 1' ,'les etats stat de la decade 1 du departement commercial ',' pour le mois %s et l"année %s est disponible ',%s)""",(moisact,anneeact,datenow,))
            db.commit()
        elif (datenow == decade2) :
            ref1 =cur1.execute(""" refresh materialized view deuxiemedecadersriagritrans_com """)
            ref2 =cur1.execute(""" refresh materialized view deuxiemedecade_com """)
            ref2 =cur1.execute(""" refresh materialized view deuxiemedecade_anc """)
            ref2 =cur1.execute(""" refresh materialized view deuxiemedecade_nvx """)
            ref2 =cur1.execute(""" refresh materialized view deuxiemedecade_diff """)
            ref2 =cur1.execute(""" refresh materialized view deuxiemedecade_directe """)
            ref2 =cur1.execute(""" refresh materialized view deuxiemedecade_banque """)
            ref2 =cur1.execute(""" refresh materialized view deuxiemedecade_prive """)
            ref2 =cur1.execute(""" refresh materialized view deuxiemedecade_comp """)
            cur1.execute(""" insert into message_com(id_msgcom , titre_msg, contenu1_msg,contenu2_msg, date) values ((SELECT MAX(id_msgcom)+1 from message_com),
            'Decade Numéro 2','les etats stat de la decade 2 du departement commercial ',' pour le mois %s et l"année %s est disponible ',%s)""",(moisact,anneeact,datenow,))
            db.commit()
        elif (datenow == decade3) :
            ref1 =cur1.execute(""" refresh materialized view troisiemedecadersriagritrans_com """)
            ref2 =cur1.execute(""" refresh materialized view troisiemedecade_com """)
            ref2 =cur1.execute(""" refresh materialized view troisiemedecade_anc """)
            ref2 =cur1.execute(""" refresh materialized view troisiemedecade_nvx """)
            ref2 =cur1.execute(""" refresh materialized view troisiemedecade_diff """)
            ref2 =cur1.execute(""" refresh materialized view troisiemedecade_directe """)
            ref2 =cur1.execute(""" refresh materialized view troisiemedecade_banque """)
            ref2 =cur1.execute(""" refresh materialized view troisiemedecade_prive """)
            ref2 =cur1.execute(""" refresh materialized view troisiemedecade_comp """)
            cur1.execute(""" insert into message_com(id_msgcom , titre_msg, contenu1_msg,contenu2_msg, date) values ((SELECT MAX(id_msgcom)+1 from message_com),
            'Decade Numéro 3 ' ,'les etats stat de la decade 3 du departement commercial ',' pour le mois %s et l"année %s est disponible ',%s)""",(moisact,anneeact,datenow,))
            db.commit()

    def rafrech_irdtann():
            
        db = get_cnn() 
        cur1 = get_cnn() .cursor()
        datenow = date.today()
        anneeact = datenow.year
        fin_annee = date(datenow.year, 1, 1) + relativedelta(years=1,days=-1)
        if  ( fin_annee == datenow) :  
            ref1 =cur1.execute(""" refresh materialized view comprpp_paragence """)
            ref2 =cur1.execute(""" refresh materialized view comprpp_parprod """)
            ref2 =cur1.execute(""" refresh materialized view prodtransport_prodmenth """) 
            cur1.execute(""" insert into message_irdt(id_msgirdt , titre_msg, contenu1_msg,contenu2_msg, date) values ((SELECT MAX(id_msgirdt)+1 from message_irdt),
            'Risque simple' ,'les etats stat annuelle du service risque simple ',' pour l"année %s est disponible ',%s)""",(anneeact,datenow,))
            cur1.execute(""" insert into message_irdt(id_msgirdt , titre_msg, contenu1_msg,contenu2_msg, date) values ((SELECT MAX(id_msgirdt)+1 from message_irdt),
            'transport' ,'les etats stat annuelle du service transport ',' pour l"année %s est disponible ',%s)""",(anneeact,datenow,))
            db.commit()

    def rafrech_irdtmen():
        db = get_cnn() 
        cur1 = get_cnn() .cursor()
        datenow = date.today()
        anneeact = datenow.year
        moisact = datenow.month
        date_finmois = date(datenow.year, datenow.month, 1) + relativedelta(months=1, days=-1)
        
        if  (date_finmois == datenow) :
            ref1 =cur1.execute(""" refresh materialized view productionagri_agenprod """)
            ref2 =cur1.execute(""" refresh materialized view productionagri_garantie """)
            ref2 =cur1.execute(""" refresh materialized view prodtransport_nvxrenvx """)
            ref2 =cur1.execute(""" refresh materialized view prodtransport_prodmenth """)
           
            cur1.execute(""" insert into message_irdt(id_msgirdt , titre_msg, contenu1_msg,contenu2_msg, date) values ((SELECT MAX(id_msgirdt)+1 from message_irdt),
            'agricole' ,'les etats stat mensuelle du service agricole  ',' pour le mois %s et l"année %s est disponible ',%s)""",(moisact,anneeact,datenow,))
            cur1.execute(""" insert into message_irdt(id_msgirdt , titre_msg, contenu1_msg,contenu2_msg, date) values ((SELECT MAX(id_msgirdt)+1 from message_irdt),
            'transport' ,'les etats stat mensuelle du service transport ',' pour le mois %s et l"année %s est disponible ',%s)""",(moisact,anneeact,datenow,))
            db.commit()
except (Exception, psycopg2.Error) as error :
        print ("Erreur lors de la connexion à PostgreSQL", error)
