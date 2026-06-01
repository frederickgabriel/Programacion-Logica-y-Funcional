%por frederick aguilar
%Hechos%
herramienta(khan_academy, [tipo(tutoria), plataforma(web), plataforma(app), nivel(primaria), nivel(secundaria), licencia(gratis)]).

herramienta(edmodo, [tipo(gestor), plataforma(web), plataforma(app), nivel(primaria), nivel(secundaria), licencia(gratis)]).

herramienta(quizlet, [tipo(repaso), plataforma(web), plataforma(app), nivel(secundaria), nivel(universidad), licencia(gratis)]).

herramienta(duolingo, [tipo(idiomas), plataforma(app), nivel(primaria), nivel(secundaria), nivel(universidad), licencia(gratis)]).

herramienta(coursera, [tipo(cursos), plataforma(web), nivel(universidad), licencia(pago)]).
herramienta(moodle, [tipo(gestor), plataforma(web), nivel(secundaria), nivel(universidad), licencia(gratis)]).

%Completar los 2 hechos que faltan%
herramienta(udemy, [tipo(cursos), plataforma(web), plataforma(app), nivel(universidad), nivel(profesionales), licencia(pago)]).

herramienta(google_classroom, [tipo(gestor), plataforma(web), plataforma(app), nivel(primaria), nivel(secundaria), nivel(universidad), licencia(gratis)]).

%Reglas para recomendaciones%

% Regla de recomendación por nivel educativo
recomendar_por_nivel(Nivel, Herramienta) :- herramienta(Herramienta, Caracteristicas), member(nivel(Nivel), Caracteristicas).

% Regla de recomendación por tipo de herramienta
recomendar_por_tipo(Tipo, Herramienta) :- herramienta(Herramienta, Caracteristicas), member(tipo(Tipo), Caracteristicas).

% Regla de recomendación por plataforma
recomendar_por_plataforma(Plataforma, Herramienta) :- herramienta(Herramienta, Caracteristicas), member(plataforma(Plataforma), Caracteristicas).

% Regla de recomendación por licencia
recomendar_por_licencia(Licencia, Herramienta) :- herramienta(Herramienta, Caracteristicas), member(licencia(Licencia), Caracteristicas).
