# kinopreiskategorie kinder bis 18 J 5euro Erwachsene 18J 10euro Senioren Ü65 7.50

kinder = 5
Erwachsene = 10
Senioren = 7.50

frage = int(input('Wie alt bist du ? '))

wieVieleTickets = int(input('Wie viele Tickets benötigst du ? '))

if frage < 18:
    print('Dein Kinder Ticket kostet pro Person', kinder, '€, zusammen macht das ', wieVieleTickets * kinder, '€')
elif 18 <= frage < 65:
    print('Dein Erwachsener Ticket kostet pro Person', Erwachsene, '€ zusammen macht das ', wieVieleTickets * Erwachsene,'€')
else:
    print('dein Senioren Ticket kostet pro Person', Senioren, '€ zusammen macht das ', wieVieleTickets * Senioren, '€')


