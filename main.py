# kinopreiskategorie kinder bis 18 J 5euro Erwachsene 18J 10euro Senioren Ü65 7.50

kinder = 5
Erwachsene = 10
Senioren = 7.50

frage = int(input('Wie alt bist du ? '))
if frage < 18:
    print('Dein Kinder Ticket kostet', kinder, '€')
elif 18 <= frage < 65:
    print('Dein Erwachsener Ticket kostet', Erwachsene, '€')
else:
    print('dein Senioren Ticket kostet', Senioren, '€')


