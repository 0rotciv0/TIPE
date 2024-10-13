all : compiler executer

compiler : 
	gcc -o main.exe main.c -Wextra -Wall -ggdb3 -fsanitize=address -lm

executer : 
	./main.exe