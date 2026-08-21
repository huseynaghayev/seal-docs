# Data Types

There are **8** types of value in Seal:

- [Null](#null)

- [Boolean](#boolean)

- [Integer](#integer)

- [Float](#float)

- [String](#string)

- [List](#list)

- [Map](#map)

- [Function](#function)

## Null

This represents `no value`. `null` keyword is reserved. You can assign it to variables and other fields, but main usage of `null` data type is to represent non-existence of value. This is one of the only 'falsy' values in Seal.

```seal
a = null
if a
    print("this won't be printed")
```

## Boolean

This represents truth values: `true` and `false`. These both are reserved keywords. Only `false` and `null` values are *falsy* values. Besides them, everything is considered as truthful values. Also, `not` unary operator which is discussed more [right here](operators.md#not) creates boolean value.

## Integer

Integer values can be represented in following forms:

- 19 (decimal)

- 0xAF or 0xaf or 0xAf (hexadecimal)

- 0o777 (octal)

- 0b1010 (binary)

## Float

Floating points can be represented in following forms:

- 3.14159

- .23 (same as 0.23)

Different operand types (such as between `int` and `float`) of binary operators are discussed [here](operators.md).

## String

Strings are immutable and garbage-collected. That means you can't modify strings like you would in C. Instead, you have to create new string object everytime you want to change it.

```seal
a = "seal"
b = "string"->upper() // SEAL
```

Learn more about `->` [right here](operators.md/#Arrow).

Both `"` and `'` are the same thing. They both create string literals. Seal currently supports the following [escape sequences](https://en.wikipedia.org/wiki/Escape_sequence):

- `\n` (newline)

- `\t` (tab)

- `\\` (backslash)

- `\"` (double quote)

- `\'` (single quote)

- `\r` (carriage return)

- `\b` (backspace)

- `\f` (formfeed)

- `\v` (vertical tab)

## List

Lists are mutable and garbage-collected. They are basically variable-sized arrays. They support negative indices which get elements from end.

```seal
a = [] // create empty list
a->push(1, 2) // same as List.push(a, 1, 2)
print(a[-1]) // 2
```

Lists are compared by their addresses, not values.

```seal
print([] == []) // false, since they are two different objects

a = [1, 2]
b = a
print(a == b) // true
print(a != [1, 2]) // true
```

## Map

Maps are mutable and garbage-collected. They are also know as 'Hashmaps', 'Tables', 'Dictionaries', 'Objects' or even 'Associative Arrays' from other programming languages and concepts. This is such an essential data structure for writing highly optimized codes. Seal maps can be only indexed by string keys (unlike Lua).

```seal
a = {} // create empty map
a.name = "Seal" // create field
a["features"] = ["Beautiful", "Fast", "Easy"] // assign with [] syntax

print(a) // {name = 'Seal', features = ['Beautiful', 'Fast', 'Easy']}
```

Like lists, they are compared by address.

```seal
print({} == {}) // false

a = { key = "value" }
a = b
print(a == b) // true
print(a != { key == "value" }) // true
```

## Function

Functions are first-class values. Meaning, they are treated as the same as other values just like lists, integers, maps etc. That means they can be passed to functions too (higher-order functions). Let's take a look at a very simple example:

```seal
define apply(f, arg)
    return f(arg)

val = apply(define(x) x * x, 7)
print(val) // 49
```

Guess what? They are compared just like lists and maps.

More detailed information can be found [right here](function.md).
