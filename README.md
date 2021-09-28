
# Curso Udemy Python

### Operadores aritméticos

Operador de suma +

Operador de resta -

Operador de negativo -

Operador de multiplicación *

Operador de exponente **

Operador de división /

Operador de  división entera //

Operador de modulo o resto %

### Reglas de precedencia

En orden de precedencia

Parentesis

Exponente

Multiplicación

División

Suma

Resta

### Operadores de cadenas

Operador de concatenación +

Operador de repetición *

### Operadores de relación

Igual a ==

Distinto de != 

Mayor que >

Menor que <

Mayor o igual que >=

Menor o igual que <=

### Operadores de asignación

Asignación simple  =

Asignación suma +=

Asignación resta -=

Asignación multiplicación *=

Asignación exponente **=

Asignación división /=

Asignación división entera //=

Asignación división mod/resto %=

### Help

#### Palabras reservadas
```
>>> help("keywords")

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               break               for                 not
None                class               from                or
True                continue            global              pass
__peg_parser__      def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield

>>>
```
#### Palabras que no se recomiendan usar

```
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 
 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 
 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 
 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 
 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 
 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 
 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError',
 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 
 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError',
 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 
 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 
 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 
 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 
 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError',
 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning',
 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', 
 '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', 
 '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 
 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 
 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 
 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 
 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 
 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 
 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 
 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 
 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 
 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>>
```

#### Identificador de memoria

```
>>> var = 10
>>> var
10
>>> id(var)
2545891240528
```

#### Valores almacenados en memoria

```
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'var']
>>>
```

#### Fechas y horas en Python

```
>>> import datetime
>>> dir(datetime)
['MAXYEAR', 'MINYEAR', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', 
'__name__', '__package__',
'__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
>>>
>>> datetime.datetime.now()
datetime.datetime(2021, 9, 24, 9, 32, 0, 417811)
>>> now = datetime.datetime.now()
>>> now
datetime.datetime(2021, 9, 24, 9, 32, 19, 957049)
>>> now.day
24
>>> now.minute
32
>>> now.year
2021
```
#### links sobre el tema

- [https://strftime.org/](https://strftime.org/)

- [https://pyformat.info/](https://strftime.org/)


```
>>> now
datetime.datetime(2021, 9, 24, 11, 11, 54, 539680)
>>> now.strftime("%B %d, %Y")
'September 24, 2021'
>>>
```

### Expresiones Regulares
 
[regexr.com](https://regexr.com/3f4vo)
Es una web para probar en tiempo real expresiones regulares

[cheatography.com](https://cheatography.com/programming/)
Es una web donde hay Cheap Sheet de todo (se pueden descargar en PDF)

Character classes
```
.	any character except newline
\w\d\s	word, digit, whitespace
\W\D\S	not word, digit, whitespace
[abc]	any of a, b, or c
[^abc]	not a, b, or c
[a-g]	character between a & g
```
Anchors
```
^abc$	start / end of the string
\b\B	word, not-word boundary
```
Escaped characters
```
\.\*\\	escaped special characters
\t\n\r	tab, linefeed, carriage return
```
Groups & Lookaround
```
(abc)	capture group
\1	backreference to group #1
(?:abc)	non-capturing group
(?=abc)	positive lookahead
(?!abc)	negative lookahead
```
Quantifiers & Alternation
```
a*a+a?	0 or more, 1 or more, 0 or 1
a{5}a{2,}	exactly five, two or more
a{1,3}	between one & three
a+?a{2,}?	match as few as possible
ab|cd	match ab or cd
```

### Crear y escribir archivos
#### Ref
```
'r' open for reading (default)

'w' open for writing, truncating the file first

'x' open for exclusive creation, failing if the file already exists

'a' open for writing, appending to the end of the file if it exists

'b' binary mode

't' text mode (default)

'+' open for updating (reading and writing)
```

