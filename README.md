# Custom Programming Language Simulator

This project is a Python-based interpreter that simulates a general-purpose programming language. It allows users to write and execute simple code while going through the fundamental phases of a programming language execution, including:

- **Lexical Analysis** (Tokenization)
- **Syntax Analysis** (Parsing and Abstract Syntax Tree generation)
- **Semantic Analysis** (Type checking and validation)
- **Code Execution** (Interpreting and running the user's code)

## Features

- Arithmetic and Boolean operations
- Variable declaration and assignment
- Arrays, tuples, and other data structures
- Conditional statements (`if`, `else`)
- Loops (`while`, `for`)
- Built-in functions(`sqrt`, `min`, `max`)

## Installation

To run the project, ensure you have Python installed. Clone this repository and navigate to the project directory:

```bash
git clone https://github.com/shilat2132/Viper.git
cd Viper
```

## Usage

To start the interpreter, run:

```bash
python tests.py
```

Then, you can enter code in the custom programming language and see the results.

## How to use

* Inside the project, enter the Viper folder and the tests.py file. 
* In there you can find tests of the code where the first part contains programs that work and the second part contains programs that would raise errors(errors of syntax/lexical/semantics). Each error is explained in a comment above the code

* In order to run one of the program, uncomment the line:
# Viper(code11).interperter()
and then run the python file. 
* Uncomment only one program each time or the code wouldn’t work correctly
* You can try adding your own program by adding a string variable, for example code13 containing the code string and sending it to the interpreter that way: Viper(code13).interperter()


## more info
for more info - see the rules in the rules.txt file
## License

This project is licensed under the MIT License - see the LICENSE file for details.


## Author
Shilat Dahan

