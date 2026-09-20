import implementation_manual, math
print(implementation_manual.__file__)
import inspect
print(inspect.getsource(implementation_manual.get_read_duration))
print(implementation_manual.get_read_duration("word " * 401))
print(implementation_manual.get_read_duration("word " * 450))