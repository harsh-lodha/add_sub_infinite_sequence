# add_sub_infinite_sequence
Help me solve this competitve programming question
The code has a logical error , the last and only 20th test case fails 
which unfortunately I dont know.
Problem statement:
Input file: standard input
Output file: standard output
Time limit: 2 seconds
Memory limit: 512 megabytes
Given two integers x and y, construct an infinite sequence of integers A = fa0; a1; a2; : : : g as
follows: a0 = 0 and for every i  1, a2i􀀀1 = a2i􀀀2 + x and a2i = a2i􀀀1 􀀀 y:
Given three integers x, y and z, find the index of the first occurrence of z in A or report that z
does not appear in A.
For example, if x = 2, y = 1 and z = 3, then A = (0; 2; 1; 3; 2; 4; 3; : : : ) and the answer is 3 (a3 = 3
and this is the first occurrence of 3 in A). If x = 2, y = 0 and z = 3, then A = (0; 2; 2; 4; 4; 6; 6; : : : )
and the answer is 􀀀1 (there is no occurrence of 3 in A).
Input
Three integers x, y and z (0  x; y; z  1000) separated by spaces.
Output
The first position of z in A or 􀀀1, if there is no occurrence of z in A.
Examples
standard input standard output
2 1 3 3
2 0 3 -1
Please discuss this problem at the following forum thread
