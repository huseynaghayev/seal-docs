# Variables

In Seal, there are two types of variables as you would expect: Locals and Globals.

This language uses different syntax than other ones. Let's go through cases.

## Naming

Variable naming must follow these rules:

- Starting with `[a-zA-Z]` or `_`

- Can include `[a-zA-Z]` or `[0-9]` or `_`

## Locals

Any identifier you type is local.

```seal
a = 0 // local
PI = 3.14159 // local
```

## Globals

If you put `$` symbol in front of any identifier, becomes global.

```seal
i_am_local = 0 // this can be accessed only in this scope

$i_am_global = 1 // this can be accessed anywhere

print("hello, world") // since print is not found in locals,
                      // it is searched in globals regardless
                      // same as $print("hello, world")
```

### Variable Search Fallback

If symbol name is found in current scope, it is used.

```seal
a = 0
print(a) // 'a' is found locally
```

If symbol is not found locally, it fallbacks to global map and searches that symbol there.

```seal
print(some_variable_name) // ERROR: 'some_variable_name is not defined'
```

If you put `$`, it does not search local names and jumps to global map immediately.

```seal
a = "local"
$a = "global"
print($a) // does not print local 'a', instead searches global 'a'
```

This is how Seal prevents you from typing `$print` everytime if you want to print something unless you define a local variable called `print` in that scope. Because `print` is just a global function. God, just imagine how annoying would it be...

### Preventing Error in Lookups

If you just want to know whether a variable is defined globally without crashing your entire program, there is a special syntax for that.

Let me introduce you `?` operator. Instead of crashing your program this returns `null` which means `no value`.

```seal
some_var? // is it defined?

name = $var? or "John" // if var doesn't exist or is null, use "John"
```

More about `?` operator can be found in [here](operators.md).
