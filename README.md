# Buddy System Memory Allocation Simulation

## Overview

This Python simulation implements the **Buddy System Memory Allocation** algorithm. Memory is divided into blocks of sizes that are powers of 2. It allocates the smallest suitable block for requests and merges "buddy" blocks when both are free, reducing fragmentation.

## Features

- Allocates the smallest suitable block for memory requests.
- Splits and merges buddy blocks to reduce fragmentation.

## Requirements

- Python 3.x

## How to Run

1. Clone or download the repository.
2. Run the simulation:

```bash
python buddy_system.py
```

## Example Usage

```python
memory = BuddySystem(1024)
block = memory.allocate(100)
memory.free(block)
```

## Author

Author: Gangula Sandaru

---
