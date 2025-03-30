games = {
    "Minecraft": "Песочница",
    "CS:GO": "Шутер",
    "The Witcher": "RPG"
}

games["Dota 2"] = "MOBA"  # Добавили игру
del games["CS:GO"]        # Удалили игру

for name, genre in games.items():
    print(f"{name} — это {genre}")
