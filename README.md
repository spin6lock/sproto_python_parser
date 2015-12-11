Sproto Python Parser
--------------------

It can support this one:

```
    .Person {
        name 0 : string
        addr 1 : string
        sex  2 : integer
    }

```

But it can not handle nested structure like this:

```
    .Person {
        name 0 : string
        addr 1 : string
        sex  2 : integer
        .PhoneNum {
            type 0 : integer
            number 1 : integer
        }
        numbers 3 : *PhoneNum
    }

```

Any help would be approciated :)
