
from datetime import datetime,timedelta

def ValidarFecha(Indate):
    if Indate!=None:
        dia=Indate.strftime('%A')
    fec_choose=str(Indate)
    actual=datetime.today()
    #actualmin=actual+timedelta(days=0.5)
    despues=actual+timedelta(days=22)
    if(len(str(fec_choose))!=0):
        fecact=actual.strftime("%Y-%m-%d")
        fecpost=despues.strftime("%Y-%m-%d")
        if(fec_choose>fecact and fec_choose<fecpost and dia!='Sunday'):
            return True
        else:
            return False
    else:
        return False