"""
Logic: Understanding nested loops foundation
- Outer loop: controls rows (vertical movement)
- Inner loop: controls columns (horizontal movement)
Key insight: Each row is independent
"""
def loop_basics(n):
    print("Basic Loop Understanding:")
    print("Row | Pattern")
    print("-" * 15)
    
    for i in range(n):  # i goes from 0 to n-1
        print(f"{i:2d}  | ", end="")
        for j in range(i + 1):  # j goes from 0 to i
            print("*", end="")
        print()  # Move to next line after each row
loop_basics(100)