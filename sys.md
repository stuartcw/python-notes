# sys 

This module provides access to some objects used or maintained by the interpreter and to functions that interact strongly with the interpreter.

## Function & Object Descriptions

### Dynamic objects:

 * [argv](sys/demo-sys.py) -- command line arguments; argv[0] is the script pathname if known
 * [path[(sys/demo-sys.py) -- module search path; path[0] is the script directory, else an empty string.
 * [modules](sys/demo-sys.py) -- dictionary of loaded modules
 
 * displayhook -- called to show results in an interactive session. Probably only usual when writing a debugger.
 * excepthook -- called to handle any uncaught exception other than SystemExit

To customize printing in an interactive session or to install a custom top-level exception handler, assign other functions to replace these.

* exitfunc -- if sys.exitfunc exists, this routine is called when Python exits
      Assigning to sys.exitfunc is deprecated; use the atexit module instead.

* stdin -- standard input file object; used by raw_input() and input()
* stdout -- standard output file object; used by the print statement
* stderr -- standard error object; used for error messages

By assigning other file objects (or objects that behave like files) to these, it is possible to redirect all of the interpreter's I/O.

 * last_type -- type of last uncaught exception
 * last_value -- value of last uncaught exception
 * last_traceback -- traceback of last uncaught exception

These three are only available in an interactive session after a traceback has been printed.

 * exc_type -- type of exception currently being handled
 * exc_value -- value of exception currently being handled
 * exc_traceback -- traceback of exception currently being handled

The function exc_info() should be used instead of these three, because it is thread-safe.
