from pypeg2 import *
class Type(Keyword):
    grammar = Enum(K("string"), K("boolean"), K("integer"))

class Parameter:
    grammar = attr("typing", Type), name()

class Parameters(Namespace):
    grammar = optional(csl(Parameter))

class Instruction(str):
    grammar = name(), ":", Type

block = "{", maybe_some(Instruction), "}"
class Function(List):
    grammar = name(), block

f = parse("""
        person { 
            name : string
            id : integer
            female : boolean
        }
        """, Function)

print(f.name)
print(f[0])
print(f)
