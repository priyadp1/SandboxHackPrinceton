#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/resource.h>
#include <sys/wait.h>
#include <fcntl.h>

int main(int argc, char** argv){
if(argc < 3){
    perror("Not enough arguments");
    return 1;
}
char *exec = argv[1];
char *log = argv[2];
struct rlimit cpuLimit = {2, 2};
setrlimit(RLIMIT_CPU, &cpuLimit);
pid_t pid = fork();
if(pid < 0){
    perror("Failed to fork");
}
if(pid == 0){
    int fd = open(log, O_WRONLY | O_CREAT | O_TRUNC, 0644);
    dup2(fd, STDOUT_FILENO);
    dup2(fd, STDERR_FILENO);
    close(fd);
    char *args[] = {exec, NULL};
    execvp(exec, args);
    perror("Failed to exec");
    exit(1);
}
else{
    int status;
    waitpid(pid, &status, 0);
    if(WIFEXITED(status)){
        printf("Program exited with %d\n" , WEXITSTATUS(status));
    }
    else if(WIFSIGNALED(status)){
        printf("Program killed by %d\n" , WTERMSIG(status));
    }
}
return 0;
}