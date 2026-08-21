## Lua

I love the fact that Lua is so simple but is so powerful at the same time. But I am not a big fan of its variable declaration syntax.

```lua
a = 0 -- global
local a = 1 -- now local
a = a + 1 -- assigns to local

-- if you ever want to access to global a,
-- you have to follow this syntax which seems a bit ugly

_G["a"] -- or
_G.a
```

## Python

Despite this language is so famous, I cannot like it. Not because I do not like its variable declaration syntax but there are other nuances too. Anyways, here is the code:

```python
# everything defined at top level (main scope)
# is considered as global symbol

a = 0 # this is global

def my_function():
    # anything defined inside this function is local

    b = 1 # this is local
    
    # to refer outside (global) a, you have to follow this syntax
    
    global a
    print(a) # 0
```
