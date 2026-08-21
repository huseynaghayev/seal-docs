# Syntax

Seal has a beautiful syntax that is easy to read and write. This section demonstrates the syntax of Seal.

## Overview

Seal uses indentation for block definitions unlike [C-like languages](https://en.wikipedia.org/wiki/List_of_C-family_programming_languages) which use `{ }` (Curly Braces). With this approach, code looks cleaner and more natural. Unlike Python, it does not use `:` (Colons) at the end which I dislike a lot. Example Seal program:

```seal
define is_prime(n)
    if n < 2 then return false

    i = 2
    while i * i <= n
        if n % i == 0
            return false

        i += 1

    return true


print(is_prime(127))
```

## Sections

- [Comments](comment.md)

- [Variables](variables.md)

- [Data Types](types.md)

- [Operators](operators.md)

- [Control Flow](control.md)

- [Functions](function.md)

- [Strings](string.md)

- [Lists](list.md)

- [Maps](map.md) (Hashmaps / Tables / Objects)
