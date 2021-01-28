from string import ascii_letters
print(ascii_letters)



for ele in listaEncuentros:
    if ele.grupo.lower()=="a":
       listaPartidosA.append(ele)

for i in listaPartidosA:
    print(len(clasiA))
    estaA=True
    estaB=True
    if len(clasiA)==0:
            clasiA.append({'equipo':i.equipoA,'jugados':0,'ganados':0,'perdidos':0})
            #clasiA.append({'equipo':i.equipoB,'jugados':0,'ganados':0,'perdidos':0})
    else:
        for dataA in clasiA:
            if dataA['equipo']!=i.equipoA:
                estaA=False
                break
                #clasiA.append({'equipo':i.equipoB,'jugados':0,'ganados':0,'perdidos':0})
            elif dataA['equipo']!=i.equipoB:
                estaB=False
                break
                #clasiA.append({'equipo':i.equipoB,'jugados':0,'ganados':0,'perdidos':0})
        if estaA==False:
            clasiA.append({'equipo':i.equipoA,'jugados':0,'ganados':0,'perdidos':0})
        elif estaB==False:
            clasiA.append({'equipo':i.equipoB,'jugados':0,'ganados':0,'perdidos':0})
 

for iss in listaPartidosA:
    if iss.puntosA > iss.puntosB:
        for datA in clasiA:
            if datA['equipo']==iss.equipoA:
                datA['jugados']=datA['jugados']+1
                datA['ganados']=datA['ganados']+1
            if datA['equipo']==iss.equipoB:
                datA['jugados']=datA['jugados']+1
                datA['perdidos']=datA['perdidos']+1
    elif iss.puntosB > iss.puntosA:
        for datA in clasiA:
            if datA['equipo']==iss.equipoB:
                datA['jugados']=datA['jugados']+1
                datA['ganados']=datA['ganados']+1
            if datA['equipo']==iss.equipoA:
                datA['jugados']=datA['jugados']+1
                datA['perdidos']=datA['perdidos']+1

clasiA.sort(key=lambda p:p['perdidos'])

for j in clasiA:
    print(j)