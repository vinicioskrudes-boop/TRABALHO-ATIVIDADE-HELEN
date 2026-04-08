from datetime import datetime

agenda = []

def cadastrar_compromisso(data, hora, desc):
    try:
        datetime.strptime(data, "%d/%m/%Y")
    except:
        return "data_invalida"
    try:
        datetime.strptime(hora, "%H:%M")
    except:
        return "hora_invalida"
    if any(c["data"] == data and c["hora"] == hora for c in agenda):
        return "conflito"
    agenda.append({"data": data, "hora": hora, "desc": desc})
    return "ok"

def limpar_agenda():
    agenda.clear()