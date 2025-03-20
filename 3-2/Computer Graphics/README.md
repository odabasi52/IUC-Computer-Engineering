- WEEK 1 compile
```bash
g++ screen.cpp -o screen -lglfw -lGL
```

- WEEK 2 compile
```bash
# one of 2
make 
g++ -I glad/include main.cpp glad/src/glad.c -lglfw -ldl -o main
```


- WEEK 3 compile
```bash
# one of 3
make 

g++ -I glad/include uygulama.cpp glad/src/glad.c -lglfw -ldl -o main
g++ -I glad/include main.cpp glad/src/glad.c -lglfw -ldl -o main
```