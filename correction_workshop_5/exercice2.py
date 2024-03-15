taches_maintenance = []

def ajouter_tache(id_tache, description):
    # tache_existante = False
    # for tache_id,_,_ in taches_maintenance:
    #     if  tache_id == id_tache:
    #         tache_existante = True
    #         break
    
    # if not tache_existante:
    #     taches_maintenance.append((id_tache, description, "En cours"))
    #     print(f"Tâche {id_tache} ajoutée.")
    # else:
    #     print("Une tâche avec cet ID existe déjà.")

    #if len([tache for tache in taches_maintenance if tache[0]== id_tache]) == 0:
    if not any(tache[0] == id_tache for tache in taches_maintenance):
        taches_maintenance.append((id_tache, description, "En cours"))
        print(f"Tâche {id_tache} ajoutée.")
    else:
        print("Une tâche avec cet ID existe déjà.")

def mettre_a_jour_tache(id_tache, statut):
    tache_trouvee = False
    for index, tache in enumerate(taches_maintenance):
        #index = taches_maintenance.index(tache)
        if  tache[0] == id_tache:
            taches_maintenance[index] = (tache[0], tache[1], statut)
            tache_trouvee = True
            print(f"Statut de la tâche {id_tache} mis à jour.")
            break
    
    if not tache_trouvee:
        print("Tâche non trouvée.")

ajouter_tache(1, "tache 1")
ajouter_tache(1, "tache 1")
mettre_a_jour_tache(1, "Términé")