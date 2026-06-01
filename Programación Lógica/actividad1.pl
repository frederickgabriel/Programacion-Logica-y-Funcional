% por frederick aguilar

% hechos que representan el arbol
mujer(reyna).
mujer(mayte).

hombre(gabriel).
hombre(rodrigo).
hombre(frederick).

madre(reyna, frederick).
madre(reyna, rodrigo).
madre(reyna, mayte).

padre(gabriel, frederick).
padre(gabriel, rodrigo).
padre(gabriel, mayte).




% datos sobre empleados

empleado(juan, 35, 'Ingeniero').
empleado(maria, 28, 'analista').
empleado(pedro, 40, 'gerente').



%Crear regla para consultar empleados menores a 30 años
joven(Persona):- empleado(Persona, Edad, _), Edad < 30.



%Pregunta y respuesta
saludo_respuesta(Saludo) :-
    member(Saludo, ["Hola", "Como estas", "Buenos dias", "Que tal?"]),
    responder_saludo(Saludo).

% Regla auxiliar para responder a saludos específicos
responder_saludo("Hola") :-
    write('Hola como puedo ayudarte?'), nl.
responder_saludo("Como estas") :-
    write('Estoy bien, gracias por preguntar.'), nl.
responder_saludo("Buenos dias") :-
    write('Buenos días como puedo ayudarte?'), nl.
responder_saludo("Que tal?") :-
    write('Todo bien, ¿y tú?'), nl.
responder_saludo(_) :-
    write('Lo siento, no entendí tu saludo.'), nl.

