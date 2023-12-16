def can_move_on(s, n, dragons):
    dragons.sort(key=lambda x: x[0])  # Sort dragons by their strength
    for dragon in dragons:
        if s <= dragon[0]:
            return "NO"  # Kirito loses the duel
        s += dragon[1]  # Kirito defeats the dragon and gets a bonus strength increase
    return "YES"  # Kirito defeats all dragons without a single loss

# Example usage
s, n = map(int, input().split())
dragons = []
for _ in range(n):
    x, y = map(int, input().split())
    dragons.append((x, y))
result = can_move_on(s, n, dragons)
print(result)
