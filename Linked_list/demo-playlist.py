from ll import LinkedList
from typing import List, Dict


def get_wos_discography() -> List[Dict[str, str]]:

    return [
        {"name": "Introducción al éxtasis", "artist": "WOS", "album": "Oscuro Éxtasis"},
        {"name": "Bizarrap Music Sessions #13", "artist": "WOS", "album": "Single"},
        {"name": "Canguro", "artist": "WOS", "album": "Caravana"},
        {"name": "Melón Vino", "artist": "WOS", "album": "Caravana"},
        {"name": "Fresko", "artist": "WOS", "album": "Caravana"},
        {"name": "Pantano", "artist": "WOS", "album": "Caravana"},
        {"name": "Escaleras", "artist": "WOS", "album": "Caravana"},
        {"name": "Luz Delito", "artist": "WOS", "album": "Caravana"},
        {"name": "Okupa", "artist": "WOS", "album": "Caravana"},
        {"name": "No Va a Bajar", "artist": "WOS", "album": "Caravana"},
        {"name": "Que se mejoren", "artist": "WOS", "album": "Oscuro Éxtasis"},
        {"name": "Niño Gordo Flaco", "artist": "WOS ft. Ca7riel", "album": "Oscuro Éxtasis"},
        {"name": "Culpa", "artist": "WOS ft. Ricardo Mollo", "album": "Oscuro Éxtasis"},
        {"name": "Andrómeda", "artist": "WOS", "album": "Single"},
        {"name": "Terraza", "artist": "WOS", "album": "Single"},
        {"name": "Animal", "artist": "WOS ft. Acru", "album": "Single"},
        {"name": "Mugre", "artist": "WOS", "album": "Oscuro Éxtasis"},
        {"name": "Convoy Jarana", "artist": "WOS", "album": "Oscuro Éxtasis"},
        {"name": "Alma Dinamita", "artist": "WOS", "album": "Oscuro Éxtasis"},
        {"name": "Buitres", "artist": "WOS", "album": "Oscuro Éxtasis"},
        {"name": "Pared de Cristal", "artist": "WOS", "album": "Oscuro Éxtasis"},
        {"name": "Mira Mamá", "artist": "WOS", "album": "Oscuro Éxtasis"},
        {"name": "Gato Negro", "artist": "WOS", "album": "Oscuro Éxtasis"},
        {"name": "Zafiro", "artist": "WOS", "album": "Oscuro Éxtasis"},
        {"name": "Contando Ovejas", "artist": "WOS", "album": "Oscuro Éxtasis"},
        {"name": "Misión", "artist": "WOS", "album": "Oscuro Éxtasis"},
        {"name": "Arrancarmelo", "artist": "WOS", "album": "Single"},
        {"name": "Descartable", "artist": "WOS", "album": "Descartable"},
        {"name": "Morfeo", "artist": "WOS", "album": "Descartable"},
        {"name": "Quemarás", "artist": "WOS ft. Indio Solari", "album": "Descartable"},
        {"name": "Cabezas Cromadas", "artist": "WOS ft. Dillom", "album": "Descartable"},
        {"name": "Melancolía", "artist": "WOS", "album": "Descartable"},
        {"name": "La Niebla", "artist": "WOS", "album": "Descartable"},
        {"name": "Sur", "artist": "WOS", "album": "Descartable"},
        {"name": "7 de Agosto", "artist": "WOS", "album": "Descartable"},
        {"name": "Estás", "artist": "WOS", "album": "Descartable"},
        {"name": "Caída Libre", "artist": "WOS", "album": "Descartable"},
        {"name": "Pausa", "artist": "WOS", "album": "Descartable"},
        {"name": "Ermitaño", "artist": "WOS", "album": "Descartable"},
        {"name": "La Coctelera", "artist": "WOS", "album": "Descartable"},
        {"name": "Nuevo Palacio", "artist": "WOS", "album": "Descartable"},
        {"name": "Live Set (Radio Nacional)", "artist": "WOS", "album": "En Vivo"},
        {"name": "Protocolo", "artist": "WOS", "album": "Single"},
        {"name": "Abrazame", "artist": "WOS", "album": "Single"},
        {"name": "Mirá Vos", "artist": "WOS", "album": "Single"},
        {"name": "Klapaucius", "artist": "WOS", "album": "Single"},
        {"name": "Sangre Fría", "artist": "WOS", "album": "Single"},
        {"name": "Bolivia", "artist": "WOS", "album": "Single"},
        {"name": "Puaj", "artist": "WOS", "album": "Single"},
        {"name": "Fresco (Remix)", "artist": "WOS", "album": "Caravana"}
    ]


def run_demo():
    playlist = LinkedList()
    songs = get_wos_discography()

    for song in songs:
        playlist.insert_at_end(
            name=song["name"],
            artist=song["artist"],
            album=song["album"]
        )

    print(f"--- PLAYLIST: WOS DISCOGRAPHY ---")
    print(f"Total tracks loaded: {len(playlist)}")
    
    if playlist.start and playlist.end:
        print(f"\nFirst Track: {playlist.start.data['name']}")
        print(f"Last Track: {playlist.end.data['name']}")

    target_song = "Quemarás"
    node = playlist.search(target_song)
    
    if node:
        print(f"\nReproduciendo: {node.data['name']} [{node.data['album']}]")
        if node.prev:
            print(f"  << Anterior: {node.prev.data['name']}")
        if node.next:
            print(f"  >> Siguiente: {node.next.data['name']}")

    print("\nVisualización de la Lista Doble:")
    print(playlist)


if __name__ == "__main__":
    run_demo()