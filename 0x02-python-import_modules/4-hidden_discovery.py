#!/usr/bin/python3
import dis
import marshal

def get_module_names(file_path):
    with open(file_path, 'rb') as f:
        magic = f.read(4)
        timestamp = f.read(4)
        code = marshal.load(f)

    if magic != b'\x03\xf3\r\n':
        print("Not a valid Python .pyc file.")
        return []

    names = []
    for instruction in code.co_code:
        if instruction.opname == 'LOAD_CONST':
            const_index = instruction.arg
            const_value = code.co_consts[const_index]
            if isinstance(const_value, str) and not const_value.startswith('__'):
                names.append(const_value)

    return sorted(set(names))

if __name__ == "__main__":
    file_path = 'hidden_4.pyc'
    names = get_module_names(file_path)

    for name in names:
        print(name)
