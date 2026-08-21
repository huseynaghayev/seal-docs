# Comments

In Seal, comments are like in C/C++. `/**/` and `//`.

## Multi-Line Comments

Since the syntax is white-space sensitive (indentation-based), there are some restrictions for using `/**/` comments.

You cannot use multi-line comments if a token comes right after comment for the first time. Example:

```seal
/* won't work */ if true
    print("something")

if /* will work */ true
    print("something else)
```

`/**/` is not nested for now, but hopefully will be implemented in the future.

```seal
/* /* */ */ // fail
```

## Single-Line Comments

`//` comment can be used anywhere in the code

```seal
if true // this is a single-line comment
    print("hello")
else
// this is else branch
    print("goodbye")
```
