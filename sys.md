# sys 

This module provides access to some objects used or maintained by the interpreter and to functions that interact strongly with the interpreter.

## Dynamic objects:

 * [argv](sys/demo-sys.py) -- command line arguments; argv[0] is the script pathname if known
 * [path](sys/demo-sys.py) -- module search path; path[0] is the script directory, else an empty string.
 * [modules](sys/demo-sys.py) -- dictionary of loaded modules
 
 
 ### System Hooks
 
 * displayhook -- called to show results in an interactive session. Probably only useful when writing a debugger.
 * excepthook -- called to handle any uncaught exception other than SystemExit

To customize printing in an interactive session or to install a custom top-level exception handler, assign other functions to replace these.

### Standard System File Objects

By assigning other file objects (or objects that behave like files) to these, it is possible to redirect all of the interpreter's I/O.

* stdin -- standard input file object; used by raw_input() and input()
* stdout -- standard output file object; used by the print statement
* stderr -- standard error object; used for error messages

#### Links

* [Redirect stdout and stderr to a logger in Python](https://www.electricmonk.nl/log/2011/08/14/redirect-stdout-and-stderr-to-a-logger-in-python/)

### Information about the last exception

 * last_type -- type of last uncaught exception
 * last_value -- value of last uncaught exception
 * last_traceback -- traceback of last uncaught exception

### Deprecated Functions & Objects

#### Interactive Session Exception Handlers

These three are only available in an interactive session after a traceback has been printed.

 * exc_type -- type of exception currently being handled
 * exc_value -- value of exception currently being handled
 * exc_traceback -- traceback of exception currently being handled

The function exc_info() should be used instead of these three, because it is thread-safe.

#### Hooking System Exit

* exitfunc -- if sys.exitfunc exists, this routine is called when Python exits. Assigning to sys.exitfunc is deprecated; use the [atexit](atexit.md) module instead.

## Static objects:

### Information about types
* float_info -- a dict with information about the float inplementation.
* long_info -- a struct sequence with information about the long implementation.
* maxint -- the largest supported integer (the smallest is -maxint-1)
* maxsize -- the largest supported length of containers.
* maxunicode -- the largest supported character
### Information about the interpreter
* builtin_module_names -- tuple of module names built into this interpreter
* version -- the version of this interpreter as a string
* version_info -- version information as a named tuple
* hexversion -- version information encoded as a single integer
* copyright -- copyright notice pertaining to this interpreter
* platform -- platform identifier
* executable -- absolute path of the executable binary of the Python interpreter
* prefix -- prefix used to find the Python library
* exec_prefix -- prefix used to find the machine-specific Python library
* float_repr_style -- string indicating the style of repr() output for floats
### Original system file objects
* \_\_stdin\_\_ -- the original stdin; don't touch!
* \_\_stdout\_\_ -- the original stdout; don't touch!
* \_\_stderr\_\_ -- the original stderr; don't touch!
* \_\_displayhook\_\_ -- the original displayhook; don't touch!
* \_\_excepthook\_\_ -- the original excepthook; don't touch!
