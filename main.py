def alocar_peca(drones):
    melhor_index = -1
    menor_bateria = 100
    for i in range(len(drones)):
        if drones[i][1] < menor_bateria and drones[i][2] > 5:
            menor_bateria = drones[i][1]
            melhor_index = i
    if melhor_index == -1:
        return "Nenhum drone elegível para peça."
    return f"Drone {melhor_index + 1} recebeu a peça de reposição."

lista_drones = [
    ["D1", 20, 4.0],
    ["D2", 80, 2.0],
    ["D3", 10, 6.5]
]

resultado = alocar_peca(lista_drones)
print(resultado)