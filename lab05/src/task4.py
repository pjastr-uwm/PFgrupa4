from unittest.mock import Mock, MagicMock

m1 = Mock()
m2 = MagicMock()

print(hasattr(m1, "__str__"))
print(hasattr(m2, "__str__"))

print(hasattr(m1, "__len__"))
print(hasattr(m2, "__len__"))

m2.__len__.return_value = 5

print(len(m2))
m2.__add__.return_value = 200

print(m2 + 8)
m2.__radd__.return_value = 200
print(8 + m2)

m2.__getitem__.side_effect = lambda key: f"wartość dla {key}"

print(m2[9])
print(m2[False])
print(m2["klucz"])

mock_context = MagicMock()
mock_context.__enter__.return_value = "wartość wewnątrz kontekstu"
mock_context.__exit__.return_value = False

with mock_context as con:
    print(con)