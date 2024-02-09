import networkx as nx
import heapq


subway = nx.Graph()
subway.add_edges_from(
    [   ("Heroiv Dnipra", "Minska", {"weight": 2}),
        ("Minska", "Obolon", {"weight": 3}),
        ("Obolon", "Pochaina", {"weight": 2}),
        ("Pochaina", "Ploshcha Tarasa Shevchenka", {"weight": 3}),
        ("Ploshcha Tarasa Shevchenka", "Kontraktova Ploshcha", {"weight": 3}),
        ("Kontraktova Ploshcha", "Poshtova Ploshcha", {"weight": 2}),
        ("Poshtova Ploshcha", "Maidan Nezalezhnosti", {"weight": 3}),
        ("Maidan Nezalezhnosti", "Ploshcha Ukrainskykh Heroiv", {"weight": 3}),
        ("Ploshcha Ukrainskykh Heroiv", "Olimpiyska", {"weight": 3}),
        ("Olimpiyska", "Palats Ukraina", {"weight": 2}),
        ("Palats Ukraina", "Lybidska", {"weight": 3}),
        ("Lybidska", "Demiivska", {"weight": 3}),
        ("Demiivska", "Holosiivska", {"weight": 2}),
        ("Holosiivska", "Vasylkivska", {"weight": 3}),
        ("Vasylkivska", "Vystavkovyi Tsentr", {"weight": 3}),
        ("Vystavkovyi Tsentr", "Ipodrom", {"weight": 2}),
        ("Ipodrom", "Teremky", {"weight": 3}),

        ("Lisova", "Chernihivska", {"weight": 3}),
        ("Chernihivska", "Darnytsia", {"weight": 2}),
        ("Darnytsia", "Livoberezhna", {"weight": 3}),
        ("Livoberezhna", "Hydropark", {"weight": 3}),
        ("Hydropark", "Dnipro", {"weight": 2}),
        ("Dnipro", "Arsenalna", {"weight": 3}),
        ("Arsenalna", "Khreshchatyk", {"weight": 4}),
        ("Khreshchatyk", "Teatralna", {"weight": 3}),
        ("Teatralna", "Universytet", {"weight": 2}),
        ("Universytet", "Vokzalna", {"weight": 3}),
        ("Vokzalna", "Politekhnichnyi Instytut", {"weight": 3}),
        ("Politekhnichnyi Instytut", "Shuliavska", {"weight": 3}),
        ("Shuliavska", "Beresteiska", {"weight": 2}),
        ("Beresteiska", "Nyvky", {"weight": 3}),
        ("Nyvky", "Sviatoshyn", {"weight": 3}),
        ("Sviatoshyn", "Zhytomyrska", {"weight": 2}),
        ("Zhytomyrska", "Akademmistechko", {"weight": 3}),

        ("Syrets", "Dorohozhychi", {"weight": 2}),
        ("Dorohozhychi", "Lukianivska", {"weight": 3}),
        ("Lukianivska", "Zoloti Vorota", {"weight": 4}),
        ("Zoloti Vorota", "Palats Sportu", {"weight": 2}),
        ("Palats Sportu", "Klovska", {"weight": 3}),
        ("Klovska", "Pecherska", {"weight": 3}),
        ("Pecherska", "Zvirynetska", {"weight": 3}),
        ("Zvirynetska", "Vydubychi", {"weight": 3}),
        ("Vydubychi", "Slavutych", {"weight": 4}),
        ("Slavutych", "Osokorky", {"weight": 3}),
        ("Osokorky", "Pozniaky", {"weight": 3}),
        ("Pozniaky", "Kharkivska", {"weight": 3}),
        ("Kharkivska", "Vyrlytsia", {"weight": 2}),
        ("Vyrlytsia", "Boryspilska", {"weight": 3}),
        ("Boryspilska", "Chervonyi Khutir", {"weight": 3}),

        ("Maidan Nezalezhnosti", "Khreshchatyk", {"weight": 5}),
        ("Teatralna", "Zoloti Vorota", {"weight": 5}),
        ("Palats Sportu", "Ploshcha Ukrainskykh Heroiv", {"weight": 5}),
    ]
)


def dijkstra_with_heapq(graph, start):
    priority_queue = [(0, start)]
    visited = set()
    shortest_paths = {vertex: float('infinity') for vertex in graph.nodes}
    shortest_paths[start] = 0

    while priority_queue:
        # Вилучення вершини з найменшою відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо вершина вже відвідана, пропускаємо її
        if current_vertex in visited:
            continue

        # Помічаємо вершину як відвідану
        visited.add(current_vertex)

        # Оновлення відстаней для сусідніх вершин
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']

            # Якщо нова відстань коротша, оновлюємо її та додаємо вершину до черги
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths


def main():
    start_vertex = "Obolon"
    shortest_paths = dijkstra_with_heapq(subway, start_vertex)

    print(f"Найкоротші шляхи з {start_vertex}:")
    for vertex, distance in shortest_paths.items():
        print(f"{vertex}: {distance}")

if __name__ == "__main__":
    main()