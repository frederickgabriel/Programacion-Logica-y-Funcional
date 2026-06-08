% ============================================================
%  BASE DE CONOCIMIENTOS - SISTEMA EXPERTO DE CARRERAS
%  Tecnológico Nacional de México
% ============================================================

% -----------------------------------------------------------
%  PERFILES DE CARRERAS
%  perfil_carrera(Carrera, Descripcion)
% -----------------------------------------------------------

perfil_carrera(sistemas_computacionales,
    "Diseña, desarrolla y administra software y sistemas de información.").

perfil_carrera(ciencia_de_datos,
    "Analiza grandes volúmenes de datos para generar conocimiento y apoyar decisiones.").

perfil_carrera(administracion,
    "Planifica, organiza y dirige recursos humanos, financieros y materiales.").

perfil_carrera(industrial,
    "Optimiza procesos productivos, calidad y logística en entornos industriales.").

perfil_carrera(alimentarias,
    "Desarrolla y controla procesos de producción, conservación y calidad de alimentos.").

perfil_carrera(desarrollo_comunitario,
    "Promueve el bienestar social y el desarrollo sustentable de comunidades.").

perfil_carrera(gestion_empresarial,
    "Administra y lidera organizaciones con enfoque en innovación y competitividad.").


% -----------------------------------------------------------
%  HABILIDADES ASOCIADAS A CADA CARRERA
%  habilidad(Carrera, Habilidad)
% -----------------------------------------------------------

habilidad(sistemas_computacionales, logica_matematica).
habilidad(sistemas_computacionales, programacion).
habilidad(sistemas_computacionales, resolucion_problemas).
habilidad(sistemas_computacionales, trabajo_en_equipo).

habilidad(ciencia_de_datos, logica_matematica).
habilidad(ciencia_de_datos, estadistica).
habilidad(ciencia_de_datos, programacion).
habilidad(ciencia_de_datos, pensamiento_critico).

habilidad(administracion, liderazgo).
habilidad(administracion, comunicacion).
habilidad(administracion, organizacion).
habilidad(administracion, trabajo_en_equipo).

habilidad(industrial, logica_matematica).
habilidad(industrial, organizacion).
habilidad(industrial, resolucion_problemas).
habilidad(industrial, trabajo_en_equipo).

habilidad(alimentarias, ciencias_naturales).
habilidad(alimentarias, laboratorio).
habilidad(alimentarias, organizacion).
habilidad(alimentarias, resolucion_problemas).

habilidad(desarrollo_comunitario, comunicacion).
habilidad(desarrollo_comunitario, empatia).
habilidad(desarrollo_comunitario, liderazgo).
habilidad(desarrollo_comunitario, trabajo_en_equipo).

habilidad(gestion_empresarial, liderazgo).
habilidad(gestion_empresarial, comunicacion).
habilidad(gestion_empresarial, organizacion).
habilidad(gestion_empresarial, pensamiento_critico).


% -----------------------------------------------------------
%  INTERESES ASOCIADOS A CADA CARRERA
%  interes(Carrera, Interes)
% -----------------------------------------------------------

interes(sistemas_computacionales, tecnologia).
interes(sistemas_computacionales, videojuegos).
interes(sistemas_computacionales, robotica).
interes(sistemas_computacionales, software).

interes(ciencia_de_datos, tecnologia).
interes(ciencia_de_datos, matematicas).
interes(ciencia_de_datos, investigacion).
interes(ciencia_de_datos, inteligencia_artificial).

interes(administracion, negocios).
interes(administracion, finanzas).
interes(administracion, organizacion_eventos).
interes(administracion, recursos_humanos).

interes(industrial, manufactura).
interes(industrial, logistica).
interes(industrial, calidad).
interes(industrial, automatizacion).

interes(alimentarias, cocina).
interes(alimentarias, ciencias).
interes(alimentarias, salud).
interes(alimentarias, medio_ambiente).

interes(desarrollo_comunitario, voluntariado).
interes(desarrollo_comunitario, medio_ambiente).
interes(desarrollo_comunitario, cultura).
interes(desarrollo_comunitario, salud).

interes(gestion_empresarial, negocios).
interes(gestion_empresarial, emprendimiento).
interes(gestion_empresarial, finanzas).
interes(gestion_empresarial, innovacion).


% -----------------------------------------------------------
%  MOTOR DE INFERENCIA
%  contar_coincidencias(+Carrera, +Lista, -N)
%  Cuenta cuántos elementos de Lista tienen relación con Carrera
%  a través de habilidad/2 o interes/2
% -----------------------------------------------------------

contar_coincidencias_habilidades(Carrera, Habilidades, N) :-
    include(habilidad(Carrera), Habilidades, Matches),
    length(Matches, N).

contar_coincidencias_intereses(Carrera, Intereses, N) :-
    include(interes(Carrera), Intereses, Matches),
    length(Matches, N).

% Puntuacion total = habilidades coincidentes * 2 + intereses coincidentes
puntaje(Carrera, Habilidades, Intereses, Puntaje) :-
    contar_coincidencias_habilidades(Carrera, Habilidades, NH),
    contar_coincidencias_intereses(Carrera, Intereses, NI),
    Puntaje is NH * 2 + NI.


% -----------------------------------------------------------
%  REGLAS DE RECOMENDACION
%  recomendar(+Habilidades, +Intereses, -Carrera, -Puntaje)
% -----------------------------------------------------------

recomendar(Habilidades, Intereses, Carrera, Puntaje) :-
    perfil_carrera(Carrera, _),
    puntaje(Carrera, Habilidades, Intereses, Puntaje),
    Puntaje > 0.


% -----------------------------------------------------------
%  REGLA: MEJOR CARRERA
%  mejor_carrera(+Habilidades, +Intereses, -Carrera, -Puntaje)
%  Devuelve la carrera con mayor puntaje
% -----------------------------------------------------------

mejor_carrera(Habilidades, Intereses, MejorCarrera, MejorPuntaje) :-
    findall(P-C, recomendar(Habilidades, Intereses, C, P), Pares),
    Pares \= [],
    max_member(MejorPuntaje-MejorCarrera, Pares).


% -----------------------------------------------------------
%  REGLA: TOP N CARRERAS
%  top_carreras(+Habilidades, +Intereses, -Lista)
%  Devuelve lista ordenada de mayor a menor puntaje
% -----------------------------------------------------------

top_carreras(Habilidades, Intereses, ListaOrdenada) :-
    findall(P-C, recomendar(Habilidades, Intereses, C, P), Pares),
    msort(Pares, Sorted),
    reverse(Sorted, ListaOrdenada).