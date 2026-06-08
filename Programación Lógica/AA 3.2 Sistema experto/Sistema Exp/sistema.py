"""
============================================================
SISTEMA EXPERTO DE RECOMENDACIÓN DE CARRERAS
Tecnológico Nacional de México

Paradigma lógico : Prolog (motor de inferencia) -> carreras.pl
Paradigma funcional: Python  (controlador)      -> map, filter, namedtuple
============================================================
"""

from pyswip import Prolog
from collections import namedtuple
import re

# ==========================
# CONEXIÓN CON PROLOG
# ==========================

prolog = Prolog()
prolog.consult("carreras.pl")

# ==========================
# ESTRUCTURAS INMUTABLES
# ==========================

Pregunta  = namedtuple("Pregunta",  ["id", "texto", "opciones", "categoria"])
Opcion    = namedtuple("Opcion",    ["clave", "texto", "valor_prolog"])
Resultado = namedtuple("Resultado", ["carrera", "puntaje", "descripcion"])

# ==========================
# BASE DE PREGUNTAS (INMUTABLE)
# ==========================

PREGUNTAS = (
    Pregunta(
        id=1,
        texto="¿Cuál es tu habilidad más destacada?",
        categoria="habilidad",
        opciones=(
            Opcion("a", "Razonamiento lógico y matemático",   "logica_matematica"),
            Opcion("b", "Comunicación y relaciones sociales",  "comunicacion"),
            Opcion("c", "Liderazgo y toma de decisiones",      "liderazgo"),
            Opcion("d", "Trabajo en laboratorio / ciencias",   "laboratorio"),
        ),
    ),
    Pregunta(
        id=2,
        texto="¿Qué habilidad describes mejor en ti?",
        categoria="habilidad",
        opciones=(
            Opcion("a", "Programar o usar herramientas digitales", "programacion"),
            Opcion("b", "Organizar tareas y proyectos",            "organizacion"),
            Opcion("c", "Empatía y trabajo social",                "empatia"),
            Opcion("d", "Resolver problemas técnicos o de diseño", "resolucion_problemas"),
        ),
    ),
    Pregunta(
        id=3,
        texto="¿Cómo prefieres trabajar?",
        categoria="habilidad",
        opciones=(
            Opcion("a", "En equipo colaborativo",             "trabajo_en_equipo"),
            Opcion("b", "Analizando datos o estadísticas",    "estadistica"),
            Opcion("c", "Con pensamiento crítico",            "pensamiento_critico"),
            Opcion("d", "En contacto con ciencias naturales", "ciencias_naturales"),
        ),
    ),
    Pregunta(
        id=4,
        texto="¿Qué área te apasiona más?",
        categoria="interes",
        opciones=(
            Opcion("a", "Tecnología e inteligencia artificial", "tecnologia"),
            Opcion("b", "Negocios y emprendimiento",            "negocios"),
            Opcion("c", "Manufactura, logística o calidad",     "manufactura"),
            Opcion("d", "Voluntariado y desarrollo social",     "voluntariado"),
        ),
    ),
    Pregunta(
        id=5,
        texto="¿Qué actividad disfrutas más en tu tiempo libre?",
        categoria="interes",
        opciones=(
            Opcion("a", "Cocinar o estudiar nutrición/salud",      "cocina"),
            Opcion("b", "Investigar o leer sobre ciencias",        "investigacion"),
            Opcion("c", "Administrar o planificar eventos",        "organizacion_eventos"),
            Opcion("d", "Explorar el medio ambiente o la cultura", "medio_ambiente"),
        ),
    ),
    Pregunta(
        id=6,
        texto="¿Cuál es tu meta profesional?",
        categoria="interes",
        opciones=(
            Opcion("a", "Crear software o videojuegos",     "software"),
            Opcion("b", "Gestionar finanzas o empresas",    "finanzas"),
            Opcion("c", "Innovar en procesos industriales", "automatizacion"),
            Opcion("d", "Emprender mi propio negocio",      "emprendimiento"),
        ),
    ),
)

NOMBRES_CARRERAS = {
    "sistemas_computacionales": "Ingeniería en Sistemas Computacionales",
    "ciencia_de_datos"        : "Ingeniería en Ciencia de Datos",
    "administracion"          : "Licenciatura en Administración",
    "industrial"              : "Ingeniería Industrial",
    "alimentarias"            : "Ingeniería en Industrias Alimentarias",
    "desarrollo_comunitario"  : "Licenciatura en Desarrollo Comunitario",
    "gestion_empresarial"     : "Licenciatura en Gestión Empresarial",
}

# ==========================
# FUNCIONES PURAS (FUNCIONAL)
# ==========================

def mostrar_bienvenida() -> None:
    print("\n" + "=" * 60)
    print("  SISTEMA EXPERTO — RECOMENDACIÓN DE CARRERA")
    print("  Tecnológico Nacional de México")
    print("=" * 60)
    print("  Responde el cuestionario para descubrir qué carrera")
    print("  se ajusta mejor a tu perfil.\n")


def mostrar_pregunta(pregunta: Pregunta) -> None:
    print(f"\n[{pregunta.id}/6] {pregunta.texto}")
    list(map(lambda op: print(f"  {op.clave}) {op.texto}"), pregunta.opciones))


def obtener_respuesta(opciones: tuple) -> Opcion:
    claves_validas = list(map(lambda o: o.clave, opciones))
    while True:
        entrada = input("  Tu respuesta: ").strip().lower()
        coincidencia = list(filter(lambda o: o.clave == entrada, opciones))
        if coincidencia:
            return coincidencia[0]
        print(f"    Opción inválida. Elige entre: {', '.join(claves_validas)}")


def preguntar_una(pregunta: Pregunta) -> tuple:
    mostrar_pregunta(pregunta)
    respuesta = obtener_respuesta(pregunta.opciones)
    return (pregunta.categoria, respuesta.valor_prolog)


def aplicar_cuestionario(preguntas: tuple) -> dict:
    respuestas = tuple(preguntar_una(p) for p in preguntas)

    habilidades = tuple(map(
        lambda r: r[1],
        filter(lambda r: r[0] == "habilidad", respuestas)
    ))
    intereses = tuple(map(
        lambda r: r[1],
        filter(lambda r: r[0] == "interes", respuestas)
    ))
    return {"habilidades": habilidades, "intereses": intereses}


# ==========================
# PUENTE PYTHON ↔ PROLOG
# ==========================

def construir_lista_prolog(elementos: tuple) -> str:
    return "[" + ", ".join(elementos) + "]"


def extraer_par(par) -> tuple:
    """
    pyswip puede devolver el functor -(Puntaje,Carrera) de varias formas
    según la versión. Esta función lo maneja todas robustamente.
    """
    s = str(par).strip()

    # --- Forma A: string tipo  "-(7,sistemas_computacionales)" ---
    m = re.match(r"^-\((\d+),\s*([a-z_]+)\)$", s)
    if m:
        return (int(m.group(1)), m.group(2))

    # --- Forma B: string tipo  "7-sistemas_computacionales" ---
    m = re.match(r"^(\d+)-([a-z_]+)$", s)
    if m:
        return (int(m.group(1)), m.group(2))

    # --- Forma C: objeto pyswip con .args  (Functor) ---
    if hasattr(par, "args"):
        try:
            return (int(par.args[0]), str(par.args[1]))
        except Exception:
            pass

    # --- Forma D: objeto con .functor y .args ---
    if hasattr(par, "functor") and hasattr(par, "args"):
        try:
            return (int(par.args[0]), str(par.args[1]))
        except Exception:
            pass

    raise ValueError(
        f"No se pudo parsear el par Prolog.\n"
        f"  Tipo  : {type(par)}\n"
        f"  Valor : {par!r}\n"
        f"  String: {s}"
    )


def par_a_resultado(par) -> Resultado:
    puntaje, carrera = extraer_par(par)
    nombre = NOMBRES_CARRERAS.get(carrera, carrera)
    desc_q = list(prolog.query(f"perfil_carrera({carrera}, Desc)"))
    desc   = desc_q[0]["Desc"] if desc_q else "Sin descripción."
    return Resultado(carrera=nombre, puntaje=puntaje, descripcion=desc)


def consultar_top_carreras(habilidades: tuple, intereses: tuple) -> list:
    lista_h = construir_lista_prolog(habilidades)
    lista_i = construir_lista_prolog(intereses)
    query   = f"top_carreras({lista_h}, {lista_i}, Lista)"

    resultados_prolog = list(prolog.query(query))
    if not resultados_prolog:
        return []

    pares = resultados_prolog[0]["Lista"]
    return list(map(par_a_resultado, pares))


# ==========================
# PRESENTACIÓN DE RESULTADOS
# ==========================

def mostrar_resultados(resultados: list) -> None:
    print("\n" + "=" * 60)
    print("  RESULTADOS DE LA INFERENCIA PROLOG")
    print("=" * 60)

    if not resultados:
        print("  No se encontraron carreras que coincidan con tu perfil.")
        return

    recomendada = resultados[0]
    print(f"\n    CARRERA RECOMENDADA:")
    print(f"      {recomendada.carrera}  (puntaje: {recomendada.puntaje})")
    print(f"      {recomendada.descripcion}")

    print("\n    RANKING COMPLETO:")
    lineas = list(map(
        lambda item: f"  {item[0]+1}. {item[1].carrera:45s}  puntaje: {item[1].puntaje}",
        enumerate(resultados)
    ))
    for linea in lineas:
        print(linea)

    print("\n" + "=" * 60)
    print("  Consulta con un orientador vocacional para más detalles.")
    print("=" * 60 + "\n")


# ==========================
# PUNTO DE ENTRADA
# ==========================

def main() -> None:
    mostrar_bienvenida()
    try:
        perfil = aplicar_cuestionario(PREGUNTAS)

        print(f"\n  Perfil capturado:")
        print(f"     Habilidades : {', '.join(perfil['habilidades'])}")
        print(f"     Intereses   : {', '.join(perfil['intereses'])}")
        print("\n    Consultando motor de inferencia Prolog...")

        resultados = consultar_top_carreras(perfil["habilidades"], perfil["intereses"])
        mostrar_resultados(resultados)

    except KeyboardInterrupt:
        print("\n\n  Sesión cancelada por el usuario.\n")


if __name__ == "__main__":
    main()



