# Compiler options
RUSTC = rustc
RUSTFLAGS = --edition=2021 -C opt-level=2

# Output directory
OUTPUT_DIR = ./build

# Target executable
TARGET = $(OUTPUT_DIR)/parity8

all: $(TARGET)

$(TARGET): parity8.rs
	$(RUSTC) $(RUSTFLAGS) -o $(TARGET) parity8.rs

clean:
	rm -rf $(OUTPUT_DIR)/*
