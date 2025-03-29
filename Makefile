all:
	gcc -o hello hello.c
	gcc -o sandbox sandbox.c
clean:
	rm hello
	rm sandbox