class BuddySystem:
    def __init__(self, total_size):
        """Initialize the buddy system with the total memory size (must be a power of 2)."""
        self.total_size = total_size
        self.free_list = {i: [] for i in range(total_size.bit_length())}  # Free blocks by size
        self.free_list[total_size.bit_length() - 1].append(0)  # Add the full block initially

    def _get_block_size(self, size):
        """Find the smallest power of 2 greater than or equal to size."""
        power = 1
        while power < size:
            power *= 2
        return power

    def _find_free_block(self, size):
        """Find a free block of at least the given size."""
        for order, blocks in self.free_list.items():
            if blocks and (1 << order) >= size:
                return order
        return None

    def allocate(self, size):
        """Allocate memory of the given size."""
        size = self._get_block_size(size)
        order = size.bit_length() - 1

        # Find a free block
        block_order = self._find_free_block(size)
        if block_order is None:
            print(f"No available block for size {size}")
            return None

        # Split blocks until we get the desired size
        while block_order > order:
            block_address = self.free_list[block_order].pop(0)
            buddy_address = block_address + (1 << (block_order - 1))
            self.free_list[block_order - 1].extend([block_address, buddy_address])
            block_order -= 1

        # Allocate the block
        block_address = self.free_list[order].pop(0)
        print(f"Allocated block at address {block_address} with size {size}")
        return block_address

    def deallocate(self, address, size):
        """Deallocate memory at the given address and size."""
        size = self._get_block_size(size)
        order = size.bit_length() - 1
        buddy_address = address ^ (1 << order)

        # Add the block back to the free list
        self.free_list[order].append(address)
        self.free_list[order].sort()

        # Try to merge with its buddy
        while order < len(self.free_list) - 1:
            if buddy_address in self.free_list[order]:
                print(f"Merging blocks {address} and {buddy_address} of size {size}")
                self.free_list[order].remove(address)
                self.free_list[order].remove(buddy_address)
                address = min(address, buddy_address)
                buddy_address = address ^ (1 << (order + 1))
                size *= 2
                order += 1
                self.free_list[order].append(address)
                self.free_list[order].sort()
            else:
                break

        print(f"Deallocated block at address {address} with size {size}")


# Example Usage
if __name__ == "__main__":
    total_memory = 1024  # Total memory size in units (must be a power of 2)
    buddy = BuddySystem(total_memory)

    # Allocate memory
    block1 = buddy.allocate(200)
    block2 = buddy.allocate(300)

    # Deallocate memory
    buddy.deallocate(block1, 200)
    buddy.deallocate(block2, 300)
