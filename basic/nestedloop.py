"""
Logic: Demonstrates the nested loop concept with explanation
Shows how inner and outer loops work together
"""
def nested_loops_demo(n):
    print("Nested Loops Visualization:")
    
    for i in range(n):  # Outer loop - ROW control
        print(f"Row {i}: ", end="")
        
        for j in range(i + 1):  # Inner loop - COLUMN control
            print(f"({i},{j})", end=" ")
        print()  # New line after each row
nested_loops_demo(8)