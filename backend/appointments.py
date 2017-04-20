from core.api import get_var, call

afspraken = get_var('appointments')
{
    id: {" title" :" some title" , " from" : 672348956726, ...},
    id2: {...}
}

(ID, {...})
call('functie_naam')

for key, item in dict().items():

def get_appointments(sort_by=0, include_trash=False):
    """
    return een lijst van de afspraken op een bepaalde volgorde.
    0 = date
    1 = date_reversed
    2 = date_moved_to_trash
    3 = data_moved_to_trash_reversed
    """
    afpraken = get_var('appointments')

    if include_trash == True:
        call(

"""
Als de include_trase true is moeten de bestanden van de prullenbak opgehaald worden.
er wordt gekeken naar de waard, die wordt gesorteerd en als include_trash false is worden de bestanden met een trash value
eruit gefilterd
"""
