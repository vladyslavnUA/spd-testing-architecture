# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

def make_alert_sound():
    print('made alert sound.')
def make_accept_sound():
    print('made acceptance sound')
def alert():
    print('!!!')
    print('there is a toxin in the food!')    
    print('!!!')
    make_alert_sound()

ingredients = ['sodium benzoate']
if 'sodium nitrate' in ingredients:
    alert()
if 'sodium benzoate' in ingredients:
    alert()
if 'sodium oxide' in ingredients:
    alert()
    
else:
    print('***')
    print('Toxin Free')
    print('***')
    make_accept_sound()
