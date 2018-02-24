# whitespace-interpreter
Python project of an interpreter for Whitespace (programming language)



[TOC]

## Introduction of Whitespace

### General

Following:

    [s] = Space (' ' or chr(32))
    [t] = Tab ('\t' or chr(9))
    [n] = Newline ('\n' or chr(10))

**Reference in:** http://compsoc.dur.ac.uk/whitespace/tutorial.php (*Which I could not get access to*)

**Reference from:** https://playsecurity.org/rawfile/grass_mud_horse_language_specification.md (*Which is GrassMudHorse Language, a language that changes \[s\] \[t\] \[n\] into Chinese characters '草' '泥' and '马'*)



Whitespace has only three valid character to program, which are **[s]**, **[t]**, and **[n]**, though it is Turing complete. Each of these is one of the *invisible* white-space characters and thus from print you can not actually see them. All other characters are treated as comments.



No need for explanation, Whitespace is able to hide the real purpose of the code. For example, you have a TOP SECRET script file, before any encryption, you can write the script in Whitespace language, and comment it with unrelated words, like:

```Whitespace
****TOP SECRET****  		
  		
    
	
		    
			 
 
	 					 		
 
 
							 	 

  								
 
    	
	  	 
 
	 							 

 
								

  							 
 


  						 	
	  
 
 
								  

 
						 	

  						  
	  
	
 	



  					 		
   	
	
 	

UR cheated :P
```

The script above is actually a function that calculate [*factorial*](https://en.wikipedia.org/wiki/Factorial). The program requires an input of number, and than calculate and output the factorial.

![after the interpreter's realization, result of factorial in console here]()



### Whitespace's Grammatical Norm

---

[⬆ Top](#whitespace-interpreter)

Whitespace programs are sets of instructions. It is more like the assembly than a high-level programming language (like C++ or Python). Data structures that Whitespace instructions operates on are **one stack** and **several heaps**, just like RAM. There are no arrays, lists or trees.



Each of Whitespace instructions has certain **prefixes**, which specify the function of the instruction listed as following:

| Prefix     | Function           |
| ---------- | ------------------ |
| \[s\]      | Stack manipulation |
| \[t\]\[s\] | Arithmetic         |
| \[t\]\[t\] | Heap access        |
| \[n\]      | Flow control       |
| \[t\]\[n\] | I/O                |

As you can see, any of the prefixes is not a prefix to the others, which means the interpreter won't misunderstand your instructions.



For each prefix, there are a series of **manipulators** to perform certain functions. Some manipulators require an operand while others don't. An **operand** is an integer (either signed or unsigned). It is given along with the instruction. The method to write an operand is introduced as following:

1. Integers are represented in binary. \[s] represent 0, \[t] represent 1.
2. Sign. Only operands of flow control instructions are unsigned integers. The others are signed. The sign is represented by the first binary digit, for which \[s] represent positive (+), \[t] represent negative (-).
3. An operand must end with a \[n].

For example, signed integer $+5 = (+101)_2$ is represented as `[s][t][s][t][n]`. Signed integer $-12=(-1100)_2$ is represented as `[t][t][t][s][s]`. Unsigned integer $255=(11111111)_2$ is represented as `[t][t][t][t][t][t][t][t]`.

The manipulators are listed as following:

#### \[s] : Stack manipulation

Whitespace stack stores parameters and results. Data is merely **integral**. The size of stack is unlimited.

| Manipulator | Operand | Function                                                   |
| ----------- | ------- | ---------------------------------------------------------- |
| \[s]        | Number  | Push a number onto stack                                   |
| \[n]\[s]    | -       | Duplicate the top of stack                                 |
| \[t]\[s]    | Number  | Duplicate the Nth (given by the operand) data onto the top |
| \[n]\[t]    | -       | Swap the top two data on stack                             |
| \[n]\[n]    | -       | Pop the number on the top of stack                         |
| \[t]\[n]    | Number  | Slide N (given by the operand) data off the stack          |

#### \[t]\[s] : Arithmetic

Whitespace does not have floating calculations, but *the digit of integral numbers is unlimited*.

An arithmetic instruction pop stack to give the right operand, and then pop stack to give the left operand. This is to make the order of operand the same as the order of pushes. The result will be pushed onto stack.

| Manipulator | Operand | Function |
| ----------- | ------- | -------- |
| \[s]\[s]    | -       | Add      |
| \[s]\[t]    | -       | Subtract |
| \[s]\[n]    | -       | Multiply |
| \[t]\[s]    | -       | Divide   |
| \[t]\[t]    | -       | Modulo   |

#### \[t]\[t] : Heap access

Same as stack, heaps only store integers. The maximum number of heaps is determined by the interpreter (///////////////////// After it finishes /////////////////), but the maximum value of heap number is unlimited.

Rules: Before storing, push a heap address (start with 0x0) first. Then push the number you need to store. When storing, top two data on stack will be popped. Top number will be stored to the heap at second top address.

Before retrieving, push the heap address. When retrieving, stack will be popped and the number stored in the heap at the address will be pushed onto stack.

| Manipulator | Operand | Function |
| ----------- | ------- | -------- |
| \[s]        | -       | Store    |
| \[t]        | -       | Retrieve |

#### \[n] : Flow control

Whitespace's flow control use **labels** (iow. tags), to mark locations for jumping (like `goto` in C/C++). The label is an **unsigned** integer with no limitation of value. Labels should not conflict with (i. e. repeat) each other, as there is only a global namespace.

| Manipulator | Operand | Function                                                     |
| ----------- | ------- | ------------------------------------------------------------ |
| \[s]\[s]    | Label   | Mark a location in the program                               |
| \[s]\[t]    | Label   | Call the subroutine at the marked location                   |
| \[s]\[n]    | Label   | Jump to the label unconditionally                            |
| \[t]\[s]    | Label   | Jump to the label if stack top is 0 (0x0)                    |
| \[t]\[t]    | Label   | Jump to the label if stack top is negative                   |
| \[t]\[n]    | -       | End the subroutine and return to where the subroutine was called |
| \[n]\[n]    | -       | End the program                                              |

***Attention: When using instructions \[n]\[t]\[s] (jump if 0) and \[n]\[t]\[t] (jump if <0), stack will pop the top to compare with 0. In order to keep the original stack top, you should first duplicate it (\[s]\[n]\[s]).***

#### \[t]\[n] : I/O control

| Manipulator | Operand | Function                                                     |
| ----------- | ------- | ------------------------------------------------------------ |
| \[s]\[s]    | -       | Pop the stack top and output it as a character               |
| \[s]\[t]    | -       | Pop the stack top and output it as a number                  |
| \[t]\[s]    | -       | Read a character (end with '\n') from input and store it to the heap addressed by stack top *(which will be popped)* |
| \[t]\[t]    | -       | Read a number from input and store it to the heap addressed by stack top *(which will be popped)* |



The program in the beginning, as said before, calculates factorial. The program starts with accepting an input of number, for example 6. Then it generates numbers that are less than the input, while not less than 0, which are 5, 4, 3, 2, 1, 0 in this case. At last, it calculate the multiplication of all those numbers, from 1 to the input, and the factorial is at the stack top, which then is outputted to the screen. 

The actual source code is provided in file "factorial.whitespace". For comments about how it works, check file "factorial.comment". For exact description of each instruction, you can copy the source code into Whitespace Interpreter, and use step option (`--step, -s`).





## How to Use Whitespace Interpreter

[⬆ Top](#whitespace-interpreter)



