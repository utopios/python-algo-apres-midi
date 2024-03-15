logs = [
    "ERROR: Echec de connexion",
    "INFO: maintenance 1",
    "WARNING: Utilisation du CPU élevée",
    "INFO: maintenance 2"
]

def filter_logs(niveau):
    # resultat = []
    # for log in logs:
    #     if log.startswith(niveau):
    #         resultat.append(log)
    # return resultat
    #return [log for log in logs if log.startswith(niveau)]
    return list(filter(lambda log: log.startswith(niveau), logs))

def compter_logs():
    niveaux = set(log.split(':')[0] for log in logs)
    # resultat = {}

    # for niveau in niveaux:
    #     #resultat[niveau] = len(filter_logs(niveau))
    #     resultat[niveau] = sum(log.startswith(niveau) for log in logs)  
    # return resultat
    return {niveau: sum(log.startswith(niveau) for log in logs) for niveau in niveaux}


print(filter_logs("ERROR"))
print(filter_logs("INFO"))


print(compter_logs())
