# Compiler
CXX = g++

# Compiler flags
CXXFLAGS = -I glad/include

# Libraries to link
LDFLAGS = -lglfw -ldl

# Source files
SRC = uygulama.cpp glad/src/glad.c

# Output executable
OUT = main

# Default target
all: $(OUT)

# Build target
$(OUT): $(SRC)
	$(CXX) $(CXXFLAGS) $(SRC) $(LDFLAGS) -o $(OUT)

# Clean target
clean:
	rm -f $(OUT)
