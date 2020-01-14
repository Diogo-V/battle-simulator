# n95555 Diogo Venancio

# --------------------------------------------- Misc. Functions ------------------------------------------------------ #


def eh_int_pos(univ):
    """
    Receives a value and returns True if it corresponds to a positive integer.

    eh_int_pos: universal -> boolean
    """
    return isinstance(univ, int) and univ >= 0


# ----------------------------------------------- TAD Posicao -------------------------------------------------------- #

# The representation for a position corresponds to a list with it's coordinates:
# Position = [x coordinate, y coordinate]

def cria_posicao(x, y):
    """
    Constructor:
    Receives 2 positives integers and returns a position.

    cria_posicao: integer x integer -> position
    """""

    # Verifies if x and y are positive integers
    if not (eh_int_pos(x) and eh_int_pos(y)):
        raise ValueError('cria_posicao: argumentos invalidos')

    return [x, y]  # The format for a position will be a list


def cria_copia_posicao(position):
    """
    Constructor:
    Receives a position and returns a copy of it.

    cria_copia_posicao: position -> position
    """
    return list(position)  # Creates a new list with the same properties


def obter_pos_x(position):
    """
    Selector:
    Receives a position and returns its x value.

    obter_pos_x: position -> integer
    """
    return position[0]


def obter_pos_y(position):
    """
    Selector:
    Receives a position and returns its y value.

    obter_pos_y: position -> integer
    """
    return position[1]


def eh_posicao(univ):
    """
    Recognizer:
    Receives a value and returns a boolean values according to if it represents a position.

    eh_posicao: universal -> boolean
    """
    return isinstance(univ, list) and len(univ) == 2 and eh_int_pos(obter_pos_x(univ)) and eh_int_pos(obter_pos_y(univ))


def posicoes_iguais(p1, p2):
    """
    Tester:
    Receives two positions and returns True if they represent the same position.

    posicoes_iguais: position x position -> boolean
    """
    return p1 == p2


def posicao_para_str(position):
    """
    Transformer:
    Receives a position and returns a string representing it's values.

    posicao_para_str: position -> string
    """
    return "(" + str(obter_pos_x(position)) + ", " + str(obter_pos_y(position)) + ")"


def obter_posicoes_adjacentes(position):
    """
    Returns a tuple containing the adjacent positions to a given position.

    obter_posicoes_adjacentes: position -> tuple
    """

    # Gets coordinates of vicinity respecting the maze's order
    res_adj_pos = ()
    x = obter_pos_x(position)
    y = obter_pos_y(position)
    if x >= 0 and y - 1 >= 0:
        res_adj_pos += (cria_posicao(x, y - 1),)
    if x - 1 >= 0 and y >= 0:
        res_adj_pos += (cria_posicao(x - 1, y),)
    if x + 1 >= 0 and y >= 0:
        res_adj_pos += (cria_posicao(x + 1, y),)
    if x >= 0 and y + 1 >= 0:
        res_adj_pos += (cria_posicao(x, y + 1),)

    return res_adj_pos  # Returns all valid coordinates of position's vicinity


# ----------------------------------------------- TAD Unidade -------------------------------------------------------- #

# The representation for a unit is a list with it's defining properties:
# Unit = [position, hit points, power, corresponding team]

def cria_unidade(position, hit_points, power, team):
    """
    Constructor:
    Receives a set with a position, hit points, power and corresponding team and returns a unit with such values.

    cria_unidade: position x integer x integer x string -> unit
    """

    # Verifies if inputs are valid
    if not (eh_posicao(position) and eh_int_pos(hit_points) and hit_points != 0 and
            eh_int_pos(power) and isinstance(team, str) and team != ""):
        raise ValueError("cria_unidade: argumentos invalidos")

    return [position, hit_points, power, team]  # The format for a unit will be a list


def cria_copia_unidade(unit):
    """
    Constructor:
    Receives a unit and returns a unit equivalent to it.

    cria_copia_unidade: unit -> unit
    """
    return list(unit)  # Creates a new list with the same properties


def obter_posicao(unit):
    """
    Selector:
    Receives a unit and returns its position.

    obter_posicao: unit -> position
    """
    return unit[0]


def obter_exercito(unit):
    """
    Selector:
    Receives a unit and returns its team.

    obter_exercito: unit -> string
    """
    return unit[3]


def obter_forca(unit):
    """
    Selector:
    Receives a unit and returns its power.

    obter_forca: unit -> integer
    """
    return unit[2]


def obter_vida(unit):
    """
    Selector:
    Receives a unit and returns its hit points.

    obter_vida: unit -> integer
    """
    return unit[1]


def muda_posicao(unit, new_pos):
    """
    Mutator:
    Receives a unit and a position and returns the same unit but with the new_pos as its position.

    muda_posicao: unit x position -> unit
    """
    unit[0] = new_pos
    return unit


def remove_vida(unit, damage):
    """
    Mutator:
    Receives a unit and the damage it took and returns the same unit but with its hp lowered.

    remove_vida: unit x integer -> unit
    """
    unit[1] -= damage
    return unit


def eh_unidade(univ):
    """
    Recognizer:
    Receives a value and returns a boolean value according to if it represents a unit.

    eh_unidade: universal -> boolean
    """
    return isinstance(univ, list) and len(univ) == 4 and eh_posicao(obter_posicao(univ)) \
           and eh_int_pos(obter_forca(univ)) and eh_int_pos(obter_vida(univ)) and obter_vida(univ) != 0 \
           and isinstance(obter_exercito(univ), str) and obter_exercito(univ) != ""


def unidades_iguais(u1, u2):
    """
    Tester:
    Receives a set of units and returns True if they are equivalent.

    unidades_iguais: unit x unit -> boolean
    """
    return u1 == u2


def unidade_para_char(unit):
    """
    Transformer:
    Receives a unit and returns the uppercase of first letter of its army.

    unidade_para_char: unit -> string
    """
    return obter_exercito(unit).upper()[0]


def unidade_para_str(unit):
    """
    Transformer:
    Receives a unit and returns a string that represents it.

    unidade_para_str: unit -> string
    """
    return unidade_para_char(unit) + "[" + str(obter_vida(unit)) + ", " + str(obter_forca(unit)) + \
           "]@" + posicao_para_str(obter_posicao(unit))


def unidade_ataca(u1, u2):
    """
    Receives two units and returns a boolean value according to if u2 has been destroyed after it has been damaged
    by the same amount of u1's power.

    unidade_ataca: unit x unit -> boolean
    """
    return obter_vida(remove_vida(u2, obter_forca(u1))) <= 0


def ordenar_unidades(tuple_units):
    """
    Receives a tuple of units and sorts them according to the map's rules.

    ordenar_unidades: tuple -> tuple
    """
    # Sorting by y coordinate and then by x coordinate
    return tuple(sorted(tuple_units, key=lambda x: (obter_pos_y(obter_posicao(x)), obter_pos_x(obter_posicao(x)))))


# ------------------------------------------------- TAD mapa --------------------------------------------------------- #

# The representation for a map is a list with it's defining features:
# Map = [size, inside walls, first army, second army]

def cria_mapa(size, walls, army1, army2):
    """
    Constructor:
    Receives four tuples: map's size (Nx, Ny), positions of in between walls, and two other tuples corresponding to
    units of the same army. Returns a map that represents the battle.

    cria_mapa: tuple x tuple x tuple x tuple -> map
    """

    # Verifying if size is a valid input
    if not (isinstance(size, tuple) and len(size) == 2 and eh_int_pos(size[0]) and eh_int_pos(size[1]) and size[0] >= 3
            and size[1] >= 3):
        raise ValueError("cria_mapa: argumentos invalidos")

    # Verifying is walls is a valid input
    if not (isinstance(walls, tuple)):
        raise ValueError("cria_mapa: argumentos invalidos")
    for wall in walls:
        if walls == ():
            break
        if not (eh_posicao(wall) and 0 < obter_pos_x(wall) < size[0] and 0 < obter_pos_y(wall) < size[1]):
            raise ValueError("cria_mapa: argumentos invalidos")

    # Verifying if armies are valid
    if not (isinstance(army1, tuple) and isinstance(army2, tuple) and army1 != () and army2 != ()):
        raise ValueError("cria_mapa: argumentos invalidos")
    for unit in army1:
        if not (eh_unidade(unit)):
            raise ValueError("cria_mapa: argumentos invalidos")
    for unit in army2:
        if not (eh_unidade(unit)):
            raise ValueError("cria_mapa: argumentos invalidos")

    return [size, walls, army1, army2]  # The format for a map will be a list


def cria_copia_mapa(battle_map):
    """
    Constructor:
    Receives a valid map and returns a copy of it.

    cria_copia_mapa: map -> map
    """
    return list(battle_map)


def obter_tamanho(battle_map):
    """
    Selector:
    Receives a map and returns a tuple containing its size.

    obter_tamanho: map -> tuple
    """
    return battle_map[0]


def obter_paredes(battle_map):
    """
    Selector:
    Receives a map and returns a tuple containing the inside walls.

    obter_paredes: map -> tuple
    """
    return battle_map[1]


def obter_exercito_1(battle_map):
    """
    Selector:
    Receives a map and returns a tuple containing the first army.

    obter_exercito_1: map -> tuple
    """
    return battle_map[2]


def obter_exercito_2(battle_map):
    """
    Selector:
    Receives a map and returns a tuple containing the second army.

    obter_exercito_2: map -> tuple
    """
    return battle_map[3]


def obter_nome_exercitos(battle_map):
    """
    Selector:
    Receives a map and returns a sorted tuple containing the name of the armies.

    obter_nome_exercitos: map -> tuple
    """
    # Since every unit in the same army has the same "tag" we can just get the first one and compare it with the input.
    if len(obter_exercito_1(battle_map)) == 0 or len(obter_exercito_2(battle_map)) == 0:
        return globals()["army1"], globals()["army2"]
    return tuple(sorted((obter_exercito(obter_exercito_1(battle_map)[0]),
                         obter_exercito(obter_exercito_2(battle_map)[0]))))


def nomes_exercitos_globais(battle_map):
    """
    Receives a battle map and creates 2 entries in the global dictionary, each one with the name of the armies.

    nomes_exercitos_globais: map -> global variables
    """
    # This was done to save the army's name before it was deleted during the simulation of the battle
    globals()["army1"] = obter_nome_exercitos(battle_map)[0]
    globals()["army2"] = obter_nome_exercitos(battle_map)[1]


def obter_unidades_exercito(battle_map, army):
    """
    Selector:
    Receives a map and the name of an army and returns a tuple with the units of such army in the map, sorted.

    obter_unidades_exercito: map x string -> tuple
    """
    # Since every unit in the same army has the same "tag" we can just get the first one and compare with the input
    # if the army does not have elements we return () to avoid conflict with other functions
    if len(obter_exercito_1(battle_map)) > 0 and obter_exercito(obter_exercito_1(battle_map)[0]) == army:
        return ordenar_unidades(obter_exercito_1(battle_map))
    elif len(obter_exercito_2(battle_map)) > 0 and obter_exercito(obter_exercito_2(battle_map)[0]) == army:
        return ordenar_unidades(obter_exercito_2(battle_map))
    return ()


def obter_todas_unidades(battle_map):
    """
    Selector:
    Receives a map and returns a tuple with all the units on it sorted according to map's rules.

    obter_todas_unidades: map -> tuple
    """
    return ordenar_unidades((obter_exercito_1(battle_map) + obter_exercito_2(battle_map)))


def obter_unidade(battle_map, position):
    """
    Selector:
    Receives a map and position and returns the unit at said position.

    obter_unidade: map x position -> unit
    """
    # Cycles through all units in the map in search of the unit
    for unit in obter_todas_unidades(battle_map):
        if obter_posicao(unit) == position:
            return unit


def obter_todas_posicoes_unidades(battle_map):
    """
    Selector:
    Receives a map and returns a tuple containing all the positions occupied by units.

    obter_todas_posicoes_adjacentes: map -> tuple
    """
    return tuple(obter_posicao(unit) for unit in obter_todas_unidades(battle_map))


def obter_exercito_atraves_unidade(battle_map, unit):
    """
    Selector:
    Receives a map and a unit and returns the army of such unit.

    obter_exercito_atraves_unidade: map x unit -> tuple
    """
    if unit in obter_exercito_1(battle_map):
        return obter_exercito_1(battle_map)
    else:
        return obter_exercito_2(battle_map)


def eliminar_unidade(battle_map, unit_del):
    """
    Mutator:
    Receives a map and a unit and returns the map without said unit.

    eliminar_unidade: map x unit -> map
    """

    # Gets all the units in the army of the unit to delete and replaces said army with a sorted one because, if not
    # done, it will create conflicts while searching for the index of the army
    army = obter_unidades_exercito(battle_map, obter_exercito(unit_del))
    battle_map[battle_map.index(obter_exercito_atraves_unidade(battle_map, unit_del))] = army

    # Verifies if there is only one unit left. Done to remove conflicts between functions
    if len(army) == 1:
        battle_map[battle_map.index(army)] = ()
    else:
        # Cycles through all units and erases the unit from input
        new_set_of_units = ()
        for unit in army:
            if unit != unit_del:
                new_set_of_units += (unit,)

        # Replaces the army of the unit_del with one without it
        battle_map[battle_map.index(army)] = new_set_of_units

    return battle_map


def mover_unidade(battle_map, unit, position):
    """
    Mutator:
    Receives a map, a unit and a position and returns the map with the unit at its new position.

    mover_unidade: map x unit x position -> map
    """
    unit[unit.index(obter_posicao(unit))] = position
    return battle_map


def eh_posicao_unidade(battle_map, position):
    """
    Recognizer:
    Receives a map and a position and returns True if position is occupied by a unit.

    eh_posicao_unidade: map x position -> boolean
    """
    return position in obter_todas_posicoes_unidades(battle_map)


def eh_posicao_parede(battle_map, position):
    """
    Recognizer:
    Receives a map and a position and returns True if position is a wall.

    eh_posicao_parede: map x position -> boolean
    """
    # Every position either has a 0 or the max coordinate in either the x or y, so we can just search for those values
    # in a set. We also need to check if it is not an inside wall
    return obter_pos_x(position) in (0, obter_tamanho(battle_map)[0] - 1) or obter_pos_y(position) in \
           (0, obter_tamanho(battle_map)[1] - 1) or position in obter_paredes(battle_map)


def eh_posicao_corredor(battle_map, position):
    """
    Recognizer:
    Receives a map and a position and returns True if position is not a wall.

    eh_posicao_corredor: map x position -> boolean
    """
    return not eh_posicao_parede(battle_map, position)


def mapas_iguais(map1, map2):
    """
    Tester:
    Receives two maps and returns True if they are equivalent to one another.

    mapas_iguais: map x map -> boolean
    """
    return map1 == map2


def mapa_para_str(battle_map):
    """
    Transformer:
    Receives a map and returns a string which, when printed, represents the battle.

    mapa_para_str: map -> string
    """

    # Initiates structures to be used in cycle
    map_str = ""
    all_units_pos = obter_todas_posicoes_unidades(battle_map)

    # In this cycle we check if each position is either a wall, a unit or is empty
    for y in range(obter_tamanho(battle_map)[1]):
        for x in range(obter_tamanho(battle_map)[0]):
            position = cria_posicao(x, y)

            # Checks if is a wall
            if eh_posicao_parede(battle_map, position):
                map_str += "#"

            # Checks if is a unit
            elif position in all_units_pos:
                map_str += unidade_para_char(obter_unidade(battle_map, position))

            # If it isn't any of the above, is empty
            else:
                map_str += "."

        map_str += "\n"

    return map_str[:-1]


def obter_inimigos_adjacentes(battle_map, unit):
    """
    Receives a map and a unit and returns a tuple containing its adjacent enemy units.

    obter_inimigos_adjacentes: map x unit -> tuple
    """

    # Initializes structures
    adj_units = ()
    adj_pos = obter_posicoes_adjacentes(obter_posicao(unit))

    # Cycles through all adjacent positions to the input unit
    for position in adj_pos:
        if eh_posicao_unidade(battle_map, position) and \
                obter_exercito(obter_unidade(battle_map, position)) != obter_exercito(unit):
            adj_units += (obter_unidade(battle_map, position),)

    return adj_units


def obter_movimento(mapa, unit):
    '''
    A funcao obter_movimento devolve a posicao seguinte da unidade argumento
    de acordo com as regras de movimento das unidades no labirinto.

    obter_movimento: mapa x unidade -> posicao
    '''

    ######################
    # Funcoes auxiliares #
    ######################
    def pos_to_tuple(pos):
        return obter_pos_x(pos), obter_pos_y(pos)

    def tuple_to_pos(tup):
        return cria_posicao(tup[0], tup[1])

    def tira_repetidos(tup_posicoes):
        conj_tuplos = set(tuple(map(pos_to_tuple, tup_posicoes)))
        return tuple(map(tuple_to_pos, conj_tuplos))

    def obter_objetivos(source):
        enemy_side = tuple(filter(lambda u: u != obter_exercito(source), obter_nome_exercitos(mapa)))[0]
        target_units = obter_unidades_exercito(mapa, enemy_side)
        tup_com_repetidos = \
            tuple(adj
                  for other_unit in target_units
                  for adj in obter_posicoes_adjacentes(obter_posicao(other_unit))
                  if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj))
        return tira_repetidos(tup_com_repetidos)

    def backtrack(target):
        result = ()
        while target is not None:
            result = (target,) + result
            target, _ = visited[target]
        return result

    ####################
    # Funcao principal #
    ####################
    # Nao mexer se ja esta' adjacente a inimigo
    if obter_inimigos_adjacentes(mapa, unit):
        return obter_posicao(unit)

    visited = {}

    # posicao a explorar, posicao anterior e distancia
    to_explore = [(pos_to_tuple(obter_posicao(unit)), None, 0)]

    # registro do numero de passos minimo ate primeira posicao objetivo
    min_dist = None

    # estrutura que guarda todas as posicoes objetivo a igual minima distancia
    min_dist_targets = []

    targets = tuple(pos_to_tuple(obj) for obj in obter_objetivos(unit))

    while to_explore:  # enquanto nao esteja vazio
        pos, previous, dist = to_explore.pop(0)

        if pos not in visited:  # posicao foi ja explorada?
            visited[pos] = (previous, dist)  # registro no conjunto de exploracao
            if pos in targets:  # se a posicao atual eh uma dos objetivos
                # se eh primeiro objetivo  ou se esta a  distancia minima
                if min_dist is None or dist == min_dist:
                    # acrescentor 'a lista de posicoes minimas
                    min_dist = dist
                    min_dist_targets.append(pos)
            else:  # nao 'e objetivo, acrescento adjacentes
                for adj in obter_posicoes_adjacentes(tuple_to_pos(pos)):
                    if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj):
                        to_explore.append((pos_to_tuple(adj), pos, dist + 1))

        # Parar se estou a visitar posicoes mais distantes que o minimo,
        # ou se ja encontrei todos os objetivos
        if (min_dist is not None and dist > min_dist) or len(min_dist_targets) == len(targets):
            break

    # se encontrei pelo menos uma posicao objetivo,
    # escolhe a de ordem de leitura menor e devolve o primeiro movimento
    if len(min_dist_targets) > 0:
        # primeiro dos objetivos em ordem de leitura
        tar = sorted(min_dist_targets, key=lambda x: (x[1], x[0]))[0]
        path = backtrack(tar)
        return tuple_to_pos(path[1])

    # Caso nenhuma posicao seja alcancavel
    return obter_posicao(unit)


# -------------------------------------------- Funcoes Adicionais ---------------------------------------------------- #


def calcula_pontos(battle_map, army):
    """
    Receives a map and an army and returns the score of such army.
    Score equals to the sum of the hp of each army's units.

    calcula_pontos: map x string -> integer
    """

    score = 0
    if obter_unidades_exercito(battle_map, army) == ():
        return score
    else:
        for unit in obter_unidades_exercito(battle_map, army):
            score += obter_vida(unit)
    return score


def simula_turno(battle_map):
    """
    Receives a battle map and simulates a round: each unit will, according to map's reading order, move one position
    and (eventually) attack an enemy unit.

    simula_turno: map -> map
    """

    # Gets all the units so that it doesn't have to be calculated in every iteration and transforms it into a list
    # to allow elements to be removed from it while iterating over the list
    all_units = list(obter_todas_unidades(battle_map))

    # Moves each unit and, if it is adjacent to an enemy, it will attack according to maps's reading order and if the
    # enemy is killed, it will remove it from the map. A While Loop was used to better control the index of the list
    # when we remove one element from it
    i = 0
    while i < len(all_units):
        mover_unidade(battle_map, all_units[i], obter_movimento(battle_map, all_units[i]))

        if obter_inimigos_adjacentes(battle_map, all_units[i]) != ():
            enemy_unit = obter_inimigos_adjacentes(battle_map, all_units[i])[0]
            remove_vida(enemy_unit, obter_forca(all_units[i]))

            if obter_vida(enemy_unit) <= 0:
                battle_map = eliminar_unidade(battle_map, enemy_unit)
                all_units.remove(enemy_unit)
                i -= 1
        i += 1

    return battle_map  # Returns the map with all the changes made


def simula_batalha(file_name, mode):
    """
    Receives a string corresponding the a simulation's config file name and a boolean value which will determine if
    the output will be in verbose or in quiet mode. Returns a string containing the name of the winning army.

    simula_batalha: string x boolean -> string
    """

    def gets_both_teams_score(map_battle):
        """Receives a map and returns a tuple with the score of both teams."""
        return calcula_pontos(map_battle, globals()["army1"]), \
               calcula_pontos(map_battle, globals()["army2"])

    def score_board(map_battle):
        """Receives a map and returns a string that represents the score board."""
        return "[ " + globals()["army1"] + ":" + \
               str(calcula_pontos(map_battle, globals()["army1"])) + " " + \
               globals()["army2"] + ":" + \
               str(calcula_pontos(map_battle, globals()["army2"])) + " ]"

    def verbose(map_battle):
        """Receives a battle map and returns a simulation in verbose mode, returning the map and
        score after each turn."""

        print(mapa_para_str(map_battle))
        print(score_board(map_battle))

        while 0 not in gets_both_teams_score(map_battle):
            print(mapa_para_str(simula_turno(map_battle)))
            print(score_board(map_battle))

    def quiet(map_battle):
        """Receives a battle map and returns a simulation in quiet mode, returning the map and score at
        the start and at the end of it."""

        print(mapa_para_str(map_battle))
        print(score_board(map_battle))

        while 0 not in gets_both_teams_score(map_battle):
            simula_turno(map_battle)

        print(mapa_para_str(map_battle))
        print(score_board(map_battle))

    # Opening the file and reading/putting the inputs from it in a list
    file = open(file_name, "r")
    list_of_lines = file.readlines()
    file.close()

    # Transforming all the items of the list from a string to something that can be used
    for line in list_of_lines:
        list_of_lines[list_of_lines.index(line)] = eval(line)

    # Getting all the structures from the list
    map_size = list_of_lines[0]
    inside_walls = tuple(cria_posicao(pos[0], pos[1]) for pos in list_of_lines[3])
    army1 = tuple(cria_unidade(cria_posicao(p[0], p[1]), list_of_lines[1][1], list_of_lines[1][2],
                               list_of_lines[1][0]) for p in list_of_lines[4])
    army2 = tuple(cria_unidade(cria_posicao(p[0], p[1]), list_of_lines[2][1], list_of_lines[2][2],
                               list_of_lines[2][0]) for p in list_of_lines[5])

    # Creates the map
    battle_map = cria_mapa(map_size, inside_walls, army1, army2)

    # Creating global variables
    nomes_exercitos_globais(battle_map)

    # Decides the mode in which it will simulate the battle
    verbose(battle_map) if mode else quiet(battle_map)

    # Seeing which army won the battle and returning their name
    if obter_exercito_1(battle_map) == () and obter_exercito_2(battle_map) == ():
        return "EMPATE"

    if obter_exercito_1(battle_map) == ():
        return globals()["army2"]
    else:
        return globals()["army1"]
