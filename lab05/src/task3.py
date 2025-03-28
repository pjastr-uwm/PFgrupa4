from unittest.mock import Mock

m3 = Mock()
m3(4,5,6)
m3(x="ayx", y=677)
m3(False, "aaa", 8, p=5.6, r = -4.5)

print(m3.called)
print(m3.call_count)
print(m3.call_args)
print(m3.call_args[0])
print(m3.call_args[1])
print(m3.call_args_list)

print("loop")
for i,call in enumerate(m3.call_args_list):
    print("Number", i)
    print("Positional arguments", call[0])
    print("Keyword arguments", call[1])