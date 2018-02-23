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

![](after the interpreter's realization, result of factorial in console here)



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



For each prefix, there are a series of manipulators to perform certain functions. They are listed as following:

#### [s] : Stack manipulation

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







## How to Use Whitespace Interpreter

[⬆ Top](#whitespace-interpreter)



