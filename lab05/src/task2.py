from unittest.mock import Mock

m2 = Mock(autospec=True)
m2.get_data.side_effect = [89, 4.5, True, "aaa"]

print(m2.get_data(x="ABC"))
print(m2.get_data())
print(m2.get_data(3433))
print(m2.get_data(False))


def modify(*args):
    return [2*elem for elem in args]


m2.get_data.side_effect = modify
print(m2.get_data(7))
print(m2.get_data(7, 9, 0))

m2.get_data.side_effect = ValueError("Wrong value")
try:
    print(m2.get_data())
except ValueError as err:
    print("Error", err)