import unicodedata

LOCAL_CULTURE_DATA = {
    "cusco": {
        "dishes": [
            "Cuy chactado (cuy frito y aplastado)",
            "Chiri uchu (plato frío de la fiesta del Corpus Christi)",
            "Lechón al horno",
            "Chicha morada (bebida de maíz morado, sin alcohol)",
        ],
        "customs": [
            "El mate de coca y los caramelos de coca son comunes para la altura.",
            "Se respeta a la Pachamama (Madre Tierra); verás ofrendas en lugares sagrados.",
            "Pide permiso antes de fotografiar a personas con vestimenta tradicional.",
            "En mercados artesanales se puede regatear con cortesía.",
        ],
        "phrases": [
            {"phrase": "Allin p'unchay", "meaning": "Buenos días (quechua)"},
            {"phrase": "Allillanchu?", "meaning": "¿Cómo estás? (quechua)"},
            {"phrase": "Sulpayki", "meaning": "Gracias (quechua)"},
            {"phrase": "¿Cuánto cuesta?", "meaning": "Para preguntar precios en español"},
        ],
    },
    "lima": {
        "dishes": [
            "Ceviche",
            "Lomo saltado",
            "Ají de gallina",
            "Anticuchos",
            "Suspiro a la limeña (postre)",
        ],
        "customs": [
            "Es habitual dejar una propina de alrededor del 10% en restaurantes.",
            "Entre conocidos, el saludo común es un beso en la mejilla.",
            "El ceviche se come típicamente al mediodía, no de noche.",
        ],
        "phrases": [
            {"phrase": "Buenos días", "meaning": "Saludo de la mañana"},
            {"phrase": "La cuenta, por favor", "meaning": "Para pedir la cuenta"},
            {"phrase": "¿Dónde queda...?", "meaning": "Para preguntar por un lugar"},
        ],
    },
    "arequipa": {
        "dishes": [
            "Rocoto relleno",
            "Adobo arequipeño",
            "Chupe de camarones",
            "Ocopa arequipeña",
        ],
        "customs": [
            "Los arequipeños tienen un fuerte orgullo regional; "
            "hablar bien de la ciudad es bien recibido.",
            "Las picanterías son restaurantes tradicionales; los platos suelen ser contundentes.",
        ],
        "phrases": [
            {"phrase": "Buenas tardes", "meaning": "Saludo de la tarde"},
            {"phrase": "¿Qué me recomienda?", "meaning": "Para pedir sugerencias de un plato"},
            {"phrase": "Muchas gracias", "meaning": "Agradecimiento"},
        ],
    },
    "buenos aires": {
        "dishes": [
            "Asado argentino",
            "Empanadas",
            "Milanesa",
            "Alfajores y dulce de leche",
        ],
        "customs": [
            "La cena suele ser tarde, entre las 9 y las 11 de la noche.",
            "El saludo habitual es un beso en la mejilla.",
            "Compartir mate es un gesto de amistad; se recibe y se devuelve al terminar.",
            "Es común dejar un 10% de propina en restaurantes.",
        ],
        "phrases": [
            {"phrase": "Che", "meaning": "Interjección coloquial para llamar la atención"},
            {"phrase": "¿Cómo andás?", "meaning": "¿Cómo estás? (voseo argentino)"},
            {"phrase": "La cuenta, por favor", "meaning": "Para pedir la cuenta"},
        ],
    },
    "paris": {
        "dishes": [
            "Croissant y baguette",
            "Croque-monsieur",
            "Crêpes",
            "Ratatouille",
            "Variedad de quesos franceses",
        ],
        "customs": [
            "Saluda con 'Bonjour' al entrar a una tienda o restaurante antes de pedir algo.",
            "Conviene reservar mesa en restaurantes, sobre todo para la cena.",
            "En el transporte público se mantiene un tono de voz bajo.",
            "El servicio suele estar incluido en la cuenta; la propina extra es opcional.",
        ],
        "phrases": [
            {"phrase": "Bonjour", "meaning": "Buenos días"},
            {"phrase": "Merci", "meaning": "Gracias"},
            {"phrase": "S'il vous plaît", "meaning": "Por favor"},
            {"phrase": "L'addition, s'il vous plaît", "meaning": "La cuenta, por favor"},
            {"phrase": "Parlez-vous anglais ?", "meaning": "¿Habla inglés?"},
        ],
    },
}


def _normalize(text: str) -> str:
    """Lowercase, trim and remove accents so 'París' and 'paris' match."""
    decomposed = unicodedata.normalize("NFD", text.lower().strip())
    return "".join(char for char in decomposed if unicodedata.category(char) != "Mn")


def get_local_culture_info(destination: str) -> dict:
    """Return typical dishes, local customs and useful phrases for a destination.

    Args:
        destination: Travel destination (for example "Cusco" or "París").

    Returns:
        Dictionary with status and the cultural information when the destination
        is in the laboratory database. For unknown destinations the status is
        "not_found" so the agent can answer carefully with general knowledge.
    """
    if not isinstance(destination, str) or not destination.strip():
        return {
            "status": "error",
            "message": "The destination must be a non-empty text.",
        }

    key = _normalize(destination)

    for known_destination, data in LOCAL_CULTURE_DATA.items():
        if known_destination in key:
            return {
                "status": "success",
                "destination": destination,
                "dishes": data["dishes"],
                "customs": data["customs"],
                "phrases": data["phrases"],
            }

    return {
        "status": "not_found",
        "destination": destination,
        "message": (
            "Destination not found in the laboratory database. "
            "Answer with general knowledge and recommend verifying local sources."
        ),
    }
