# alocacao-peca-drone
## Descrição do Problema
Sistema para alocar peças de reposição em drones de entrega com base no nível de bateria e distância percorrida.
## Requisitos
- Receber lista de drones com ID, bateria e distância.
- Alocar peça para o drone com menor bateria que já percorreu mais de 5km.
- Se não houver drone elegível, retornar mensagem de aviso.
## Exemplo de Uso
Entrada: Drones com baterias [20, 80, 10] e distâncias [4, 2, 6].
Saída: Drone 3 recebeu a peça de reposição.