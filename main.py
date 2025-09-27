import random
class Entrenador:
    def __init__(self, nombre: str):
        self.nombre = nombre

class Pokemon:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.ataque_max = random.randint(20, 100)
        self.vida_max = random.randint(150, 400)
        self.vida_actual = self.vida_max
    def __str__(self):
        return (f"{self.nombre} | ATAQUE MAX: {self.ataque_max} "
                f"| VIDA: {self.vida_actual}/{self.vida_max}")
    

entrenador1 = None
pokemon1 = None
entrenador2 = None
pokemon2 = None

ganadas = 0
perdidas = 0


def crearEntrenadorPokemon(jugador: int) -> None:
    global entrenador1, pokemon1, entrenador2, pokemon2

    print(" CREAR ENTRENADOR Y POKÉMON")
    if jugador == 1:
        nombre_ent = input("Tu nombre de entrenador: ").strip() or "Jugador"
        nombre_pok = input("Nombre de tu Pokémon: ").strip() or "Starter"

        entrenador1 = Entrenador(nombre_ent)
        pokemon1 = Pokemon(nombre_pok)

        print(f"¡Listo {entrenador1.nombre}!")
        print(f"Tu Pokémon: {pokemon1}")
    elif jugador == 2:
        nombre_ent = input("Nombre del entrenador rival: ").strip() or "Rival"
        nombre_pok = input("Nombre del Pokémon rival: ").strip() or "Rivalmon"

        entrenador2 = Entrenador(nombre_ent)
        pokemon2 = Pokemon(nombre_pok)

        print(f" Rival creado: {entrenador2.nombre}")
        print(f"Pokémon rival: {pokemon2}")
    else:
        print("Jugador inválido (usa 1 o 2).")


def valorDeAtaque (jugador:int)-> int:
    if jugador == 1:
        if pokemon1 is None:
            raise RuntimeError("Tu Pokémon no existe. Crea primero al jugador 1.")
        return random.randint(0, pokemon1.ataque_max)
    elif jugador == 2:
        if pokemon2 is None:
            raise RuntimeError("El Pokémon rival no existe. Crea primero al jugador 2.")
        return random.randint(0, pokemon2.ataque_max)
    else:
        raise ValueError("Jugador inválido (usa 1 o 2).")
def defender(receptor: int, valor_ataque: int) -> int:
    dado = random.randint(1, 6)
    ataque_final = 0 if dado == 6 else valor_ataque

    # Aplica al receptor
    if receptor == 1:
        if pokemon1 is None:
            raise RuntimeError("Tu Pokémon no existe.")
        pokemon1.vida_actual = max(0, pokemon1.vida_actual - ataque_final)
        vida_restante = pokemon1.vida_actual

        print(f"(DEFENSA) Dado: {dado} -> Daño aplicado a {pokemon1.nombre}: {ataque_final}. "
              f"Vida restante: {vida_restante}/{pokemon1.vida_max}")
        return vida_restante

    elif receptor == 2:
        if pokemon2 is None:
            raise RuntimeError("El Pokémon rival no existe.")
        pokemon2.vida_actual = max(0, pokemon2.vida_actual - ataque_final)
        vida_restante = pokemon2.vida_actual

        print(f"(DEFENSA) Dado: {dado} -> Daño aplicado a {pokemon2.nombre}: {ataque_final}. "
              f"Vida restante: {vida_restante}/{pokemon2.vida_max}")
        return vida_restante

    else:
        raise ValueError("Receptor inválido (usa 1 o 2).")


def recuperar() -> None:

    if pokemon1 is not None:
        pokemon1.vida_actual = pokemon1.vida_max
    if pokemon2 is not None:
        pokemon2.vida_actual = pokemon2.vida_max




def pelear():
    global ganadas, perdidas
    crearEntrenadorPokemon(2)

    recuperar()

    print(" INICIA LA PELEA ")
    print(f"Tú: {entrenador1.nombre} con {pokemon1}")
    print(f"Rival: {entrenador2.nombre} con {pokemon2}\n")

    turno = 1
    while True:
        print(f"=== Turno {turno} ===")
        atk1 = valorDeAtaque(1)
        print(f"Tu {pokemon1.nombre} ataca con fuerza {atk1}.")
        vida2 = defender(2, atk1) 
        if vida2 <= 0:
            print(f" ¡Ganaste! Entrenador: {entrenador1.nombre} | Pokémon: {pokemon1.nombre}")
            ganadas += 1
            break

        atk2 = valorDeAtaque(2)
        print(f"El {pokemon2.nombre} rival ataca con fuerza {atk2}.")
        vida1 = defender(1, atk2) 
        if vida1 <= 0:
            print(f" Perdiste. Ganador: {entrenador2.nombre} | Pokémon: {pokemon2.nombre}")
            perdidas += 1
            break

        turno += 1
        print("")

def main(): 
    random.seed()
    crearEntrenadorPokemon(1)

    while True:
        print("\nMenú: [P]elear  |  [F]inalizar")
        op = input("Opción: ").strip().upper()

        if op == "P":
            pelear()
        elif op == "F":
            print("RESUMEN FINAL")
            print(f"Entrenador: {entrenador1.nombre}")
            print(f"Tu Pokémon: {pokemon1}")
            print(f"Encuentros ganados: {ganadas}")
            print(f"Encuentros perdidos: {perdidas}")
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción inválida. Usa P o F.")


if __name__ == "__main__":
    main()

