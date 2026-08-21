# Control Flow

In Seal, control flow is straightforward. It has [off-side rule](https://en.wikipedia.org/wiki/Off-side_rule) aka indentation rule for defining where blocks start and end like Python, CoffeeScript, ABC.

## If-Else

```seal
if a > 0
    print("a is positive")
else if a < 0
    print("a is negative")
else
    print("a is zero")
```

You just use indentation to define blocks. No `:` unlike Python.

```seal
a = integer(read())

if a == 0 then print("zero")
else if a == 1
    print("it is one")
else if a == 2 then print("two")
else print("unknown")
```

You can mix inline if-else statements with block ones.

## While

```seal
while true
    print("this will print forever")
```

While loop is straightforward as well.

```seal
while true do print("hello")
```

You can write inline while loop with `do` keyword.

## Seal-style loop

```seal
i = -1
max = 10
while ++i < max
    print(i) 
```

Instead of putting `++i` at the end of the loop body, you can put the increment into the condition check itself, and compensate by assigning `-1` to `i` before the loop begins. So it becomes kind of a "C-style for loop". If you'll let me, I want to call this "Seal-style loop".

## For

```seal
for i in 10
    print(i) // from 0 to 10 (10 is excluded)

for c in "my string"
    print(c)

for x in [1, 2, 3, 4, 5]
    print(x)
```

Currently, for loop supports 3 types of iterables: integer, string and list.

```seal
sum = 0
for i in 10 do sum += i
print(sum)
```

Here is inline for loop as well.

## Skip and Stop

```seal
for c in "Hello, World!"
    if c == "l" then skip
    if c == "r"
        stop

    print(c)
```

Output:

```
H
e
o
,
 
W
o
```

As you can tell, `skip` is for the traditional `continue` keyword, and `stop` is for `break`. I have used these keywords since the first version of Seal, and decided to keep them. Because why not?

## Function

```
define is_odd(n)
    return n % 2 == 1
```

This code defines a local function called "is_odd" in current scope.

```seal
is_odd = define(n)
    return n % 2 == 1
```

Since functions are first-class citizens in Seal, you can create an anonymous function and assign that directly to a variable. For convention, first option is more recommended.

```seal
define optimized_is_odd(n) (n & 1) == 1
```

If closing parenthesis is followed by a single expression right away, it is called "lambda".

```seal
add = define(a, b) a + b
```

Again, first-class.

```seal
define $add(a, b) a + b
$add = define(a, b) a + b

define $add(a, b)
    return a + b

$add = define(a, b)
    return a + b
```

By putting `$`, you define that function as global.

## Include

```seal
include "io"
```

Include statement requires string after it. Here are standard library names:

- "math"

- "io"

- "system"

When you include a file, you get capital case named global variable as a convention.

```seal
include "math"
Math // global hashmap holding mathematical functions
include "io"
IO  // again, global hashmap holding IO-related functions
include "io"  //  does not load again
```

When include statement is executed, first, it looks for standard libraries. Then, local files. It can include both `so`, `dll` files or Seal scripts. It starts with shared object files, and then Seal files. It loads the file only once.
