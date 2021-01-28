 if(ele.puntosA<ele.puntosB):
                if listaPartidosA:
                   for i in data:
                        if i['equipo'].lower()==ele.equipoB:
                           i['jugados']=+1
                           i['ganados']=+1
                        if i['equipo'].lower()==ele.equipoA:
                           i['jugados']=+1
                           i['perdidos']=+1
                else:
                    print()
        elif(ele.puntosA>ele.puntosB):
            if listaPartidosA:
                print()
            else:
                print()

clasiA=({'equipo':,'jugados':,perdidos:,ganados})


for i in listaPartidosA:
        if i.puntosA>i.puntosB:
            for dataA in clasiA:
                if dataA['equipo']==i.equipoA:
                    clasiA.append({'equipo':i.equipoA,'jugados':1,'ganados':1,'perdidos':0})
                    #clasiA.append({'equipo':i.equipoB,'jugados':1,'ganados':0,'perdidos':1})
                elif dataA['equipo']==i.equipoB:
                    clasiA.append({'equipo':i.equipoA,'jugados':1,'ganados':1,'perdidos':0})
                    #clasiA.append({'equipo':i.equipoB,'jugados':1,'ganados':0,'perdidos':1})
            
        if i.puntosA<i.puntosB:
            clasiA.append({'equipo':i.equipoB,'jugados':1,'ganados':1,'perdidos':0})
            clasiA.append({'equipo':i.equipoA,'jugados':1,'ganados':0,'perdidos':1})


for j in clasiA:
    print(j)


for ele in listaEncuentros:
    if ele.grupo.lower()=="b":
       listaPartidosB.append(ele)


for i in listaPartidosB:
    print(len(clasiA))
    estaA=True
    estaB=True
    if len(clasiB)==0:
            clasiB.append({'equipo':i.equipoA,'jugados':0,'ganados':0,'perdidos':0})
            #clasiA.append({'equipo':i.equipoB,'jugados':0,'ganados':0,'perdidos':0})
    else:
        for dataB in clasiB:
            
            if dataB['equipo']!=i.equipoA:
                estaA=False
                break
                #clasiA.append({'equipo':i.equipoB,'jugados':0,'ganados':0,'perdidos':0})
            elif dataB['equipo']!=i.equipoB:
                estaB=False
                break
                #clasiA.append({'equipo':i.equipoB,'jugados':0,'ganados':0,'perdidos':0})
        if estaA==False:
            clasiB.append({'equipo':i.equipoA,'jugados':0,'ganados':0,'perdidos':0})
        elif estaB==False:
            clasiB.append({'equipo':i.equipoB,'jugados':0,'ganados':0,'perdidos':0})

for j in clasiB:
    print(j)