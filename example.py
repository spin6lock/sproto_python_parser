from pypeg2 import *
class Type(Keyword):
    grammar = Enum(K("string"), K("boolean"), K("integer"))

class Array(Symbol):
    regex = re.compile("\*")

class Number(Symbol):
    regex = re.compile("\d+")

class EntityName(Symbol):
    regex = re.compile("([a-zA-Z0-9]+)")

class FIELD(Namespace):
    grammar = name(), attr("id", Number), ":", attr("is_array", optional(Array)), attr("typing", Type)

class block(Namespace):
    pass

class Struct(List):
    pass


block.grammar = "{", maybe_some([FIELD, Struct]), "}"
Struct.grammar = ".", attr("name", EntityName), block

with open("array_type.sproto") as fin:
    content = fin.read()
    f = parse(content, Struct)

print(f.name)
for fitem in f:
    for k, v in fitem.items():
        print(k, "is_array", bool(v.is_array))
