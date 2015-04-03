from pypeg2 import *
class Type(Keyword):
    grammar = Enum(K("string"), K("boolean"), K("integer"))

class Number(Symbol):
    regex = re.compile("\d+")

class EntityName(Symbol):
    regex = re.compile("([a-zA-Z0-9]+)")

class Instruction(Namespace):
    grammar = name(), attr("id", Number), ":", attr("typing", Type)

block = "{", maybe_some(Instruction), "}"

class Function(List):
    grammar = ".", attr("name", EntityName), block

f = parse("""
        .Person { 
            name 0 : string
            id 1 : integer
            female 2 : boolean
        }
        """, Function)

print(f.name)
for fitem in f:
    print(fitem.name, fitem.typing, fitem.id)
