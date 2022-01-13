import datetime
def ValidarHora(hora):
    hora_inicio=datetime.time(hour=8,minute=0,second=0,microsecond=0)
    hora_fin=datetime.time(hour=20,minute=0,second=0,microsecond=0)
    if(len(str(hora))!=0) and hora!=None:
        if(hora_inicio<=(hora)and hora<=(hora_fin)):
            return True
        else:
            return False
    else :
        return False
horasAtencion=(
        (datetime.time(hour=8,minute=0,second=0,microsecond=0),'8am-9am'),
        (datetime.time(hour=9,minute=0,second=0,microsecond=0),'9am-10am'),
        (datetime.time(hour=10,minute=0,second=0,microsecond=0),'10am-11am'),
        (datetime.time(hour=11,minute=0,second=0,microsecond=0),'11am-12pm'),
        (datetime.time(hour=12,minute=0,second=0,microsecond=0),'12pm-1pm'),
        (datetime.time(hour=15,minute=0,second=0,microsecond=0),'3pm-4pm'),
        (datetime.time(hour=16,minute=0,second=0,microsecond=0),'4pm-5pm'),
        (datetime.time(hour=17,minute=0,second=0,microsecond=0),'5pm-6pm'),
        (datetime.time(hour=18,minute=0,second=0,microsecond=0),'6pm-7pm'),
        (datetime.time(hour=19,minute=0,second=0,microsecond=0),'7pm-8pm'),
        (datetime.time(hour=20,minute=0,second=0,microsecond=0),'8pm-9pm'),
    )
