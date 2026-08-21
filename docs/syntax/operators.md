# Operators

## Precedence Table

Seal follows almost exactly C's precende order for operators. Here is precedence table of Seal operators in descending order:

| Operator(s)                                                                 | Description                                                                                                                                                                                               | Associativity |
|:---------------------------------------------------------------------------:| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |:-------------:|
| `++`, `--`<br>`()`<br>`[]`<br> `.`<br>`->`<br>`?`<br>`$`                    | Postfix increment and decrement<br>Function call<br>Indexing<br>Field access<br>Method call<br>Safe access<br>Global variable access                                                                      | Left-to-right |
| `++`, `--`<br>`+`, `-`<br> `!`,`not`, `~`                                   | Prefix increment and decrement<br>Unary plus and minus<br>Logical NOTs and bitwise NOT                                                                                                                    | Right-to-left |
| `*`, `/`, `%`                                                               | Multiplication, division, and remainder                                                                                                                                                                   | Left-to-right |
| `+`, `-`                                                                    | Addition and subtraction                                                                                                                                                                                  |               |
| `<<`, `>>`                                                                  | Bitwise left shift and right shift                                                                                                                                                                        |               |
| `<`, `<=`<br>`>`, `>=`                                                      | Less than and less than or equal to<br>Greater than and greater than or equal to                                                                                                                          |               |
| `==`, `!=`                                                                  | Equal to and not equal to                                                                                                                                                                                 |               |
| `&`                                                                         | Bitwise AND                                                                                                                                                                                               |               |
| `^`                                                                         | Bitwise XOR (exclusive OR)                                                                                                                                                                                |               |
| `\|`                                                                        | Bitwise OR                                                                                                                                                                                                |               |
| `and`                                                                       | Logical AND                                                                                                                                                                                               |               |
| `or`                                                                        | Logical OR                                                                                                                                                                                                |               |
| `if then else`                                                              | Ternary                                                                                                                                                                                                   | Right-to-left |
| `=`<br>`*=`, `/=`, `%=`<br>`+=`, `-=`<br>`<<=`, `>>=`,<br>`&=`, `^=`, `\|=` | Simple assignment<br>Assignment by product, quotient, and remainder<br>Assignment by sum and difference<br>Assignment by bitwise left shift and right shift<br>Assignment by bitwise AND, XOR, and OR<br> |               |
| `,`                                                                         | Comma                                                                                                                                                                                                     | Left-to-right |

## Some notes

- `++`, `--` are just like in C. If it is postfix, it mutates variable afterwards, otherwise, it mutates right before giving value.

  ```seal
  a = 32
  print(a++) //  32
  print(a)   //  33
  print(++a) //  34
  print(a)   //  34
  ```

- `$` lets you access to a global symbol explicitly. It is must be used if mutation or declaration of a global symbol is desired.

  ```seal
  $a = 20   //  global
  a  = 30   //  local, since on assignment, globals must be explicit
  print(a)  //  30, if no '$', locals are searched first
  print($a) //  20, since it is explicitly referred to a global
  ```

  Now, what if no locals shadow a global?

  ```seal
  $GLOBAL = 20
  GLOBAL + 2  // we can omit '$' since there is no GLOBAL
              // in this scope
  // this is just how global "print" function works without '$'
  print("Hello, Seal!")
  $print("Hello, Seal!")
  // they are just the same
  ```

  In Lua, everything you type without local is declared as a global. You have to type `local` to declare a local variable. But in Seal, it is kind of vice versa: unless you type `$` explicitly, anything is local.

- `?` shall be combined with either field access operator (`.`) or on a variable directly.

  ```seal
  WIDTH   //  if not defined, the program will crash
  WIDTH?  //  if not defined, return null, otherwise its value
  
  if not WIDTH?  //  one of its useful cases
      WIDTH = 1920
  ```

  In Lua, if you type an undefined variable name, it will silently return `nil`, unless you have attached some metatable to `_G` global table (it is dirty in my opinion). But in Seal, as you can see, you can use `?` operator to safely access to your global variable or just omit `?` to catch typos in your program.

  ```seal
  city = {
      name = "Vienna"
  }
  
  city.population   // crashes
  city.population?  // null
  
  // a useful case
  population = city.population? or 30000
  ```

  Another Lua vs Seal situtation here. In Lua, it doesn't crash when you access to undefined field of a map. But in Seal, you can define the access behavior.

- `->` is used as "method caller". Since Seal is a non-object-oriented language, this operator is used to imitate method-calling just like `:` operator in Lua.

  ```seal
  person = {
      name = "Huseyn",
      talk = define(self, msg) print(self.name, ":", msg)
  }
  
  person->talk("Hello")
  ```

  This is also useful on calling string, list functions as methods.

  ```seal
  "hello"->upper()  //  "HELLO"
  []->push(0, 1, 2)
  ```

  You can omit parentheses if you call with no arguments.

  ```seal
  "hello"->upper()  //  omit ()
  "hello"->upper
  "hello"->len
  ```

- Ternary operator in Seal is written in the following way:

  ```seal
  a = if 5 > 1 then "hi" else "bye"
  ```

- Seal uses `,` operator from C. It is not that widely known or talked about. It can be described as a "expression-separator". It evaluates expressions from left to right and returns the last expression value. So it is neither a tuple like in Python, nor multiple-returned value from a function in Lua.

  ```seal
  a = "hi", "hello"  //  returns "hello"
  ```

  Don't worry. Inside list and map declarators, function calls, and lambda, unless parentheses are explicitly put, comma is used as a separator, not operator.

  ```seal
  func(1, 2) // separator, two arguments
  func((1, 2)) // one argument, comma operator
  list = [1, 2] // two elements
  list = [(1, 2)] // one element, [2]
  lambda = define(x) x * x, 2  //  lambda = 2
  lambda = define(x) (x * x, 2)  //  lambda = a function that
                                 //  that returns only 2
  ```
