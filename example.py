from pypeg2 import *
class Type(Keyword):
    grammar = Enum(K("string"), K("boolean"), K("integer"))

class Number(Symbol):
    regex = re.compile("\d+")

class EntityName(Symbol):
    regex = re.compile("([a-zA-Z0-9]+)")

class Instruction(Namespace):
    grammar = name(), attr("id", Number), ":", attr("typing", Type)

class Struct(List):
    pass

block = "{", maybe_some([Instruction, Struct]), "}"
Struct.grammar = ".", attr("name", EntityName), block

f = parse("""
        .Person { 
            name 0 : string
            id 1 : integer
            female 2 : boolean
            .Phone {
                type 0 : integer
                number 1 : string
            }
        }""", Struct)

print(f.name)
for fitem in f:
    print(fitem)
