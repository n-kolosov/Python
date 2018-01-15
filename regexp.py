import re
p = re.compile(r"^[а-я]+", re.I | re.U)
print("Найдено" if p.search("АБВГДЕЁ") else "Нет")