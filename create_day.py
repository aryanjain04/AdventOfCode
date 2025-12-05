#!/usr/bin/env python3
"""
Script to create a new day's directory structure for Advent of Code.

Usage: python create_day.py <year> <day>
Example: python create_day.py 2025 2
"""

import os
import sys

SOLUTION_TEMPLATE = '''#!/usr/bin/env python3
"""
Advent of Code {year} - Day {day}
"""

def parse_input(input_text):
    """Parse the input text into usable data structure."""
    lines = input_text.strip().split('\\n')
    return lines

def part1(data):
    """Solve part 1 of the puzzle."""
    # TODO: Implement solution for part 1
    return 0

def part2(data):
    """Solve part 2 of the puzzle."""
    # TODO: Implement solution for part 2
    return 0

def main():
    """Main function to read input and solve both parts."""
    with open('input.txt', 'r') as f:
        input_text = f.read()
    
    data = parse_input(input_text)
    
    print(f"Part 1: {{part1(data)}}")
    print(f"Part 2: {{part2(data)}}")

if __name__ == "__main__":
    main()
'''

README_TEMPLATE = '''# Day {day}

## Problem Description
<!-- Add the problem description from Advent of Code website -->

## Solution
Run the solution with:
```bash
python solution.py
```

## Notes
<!-- Add any notes about your approach -->
'''

def create_day(year, day):
    """Create directory structure for a new day."""
    day_str = str(day).zfill(2)
    dir_path = f"{year}/day{day_str}"
    
    # Create directory
    os.makedirs(dir_path, exist_ok=True)
    
    # Create solution.py
    solution_path = os.path.join(dir_path, "solution.py")
    with open(solution_path, 'w') as f:
        f.write(SOLUTION_TEMPLATE.format(year=year, day=day))
    
    # Make solution.py executable
    os.chmod(solution_path, 0o755)
    
    # Create input.txt
    input_path = os.path.join(dir_path, "input.txt")
    with open(input_path, 'w') as f:
        f.write("# Place your puzzle input here\n")
    
    # Create README.md
    readme_path = os.path.join(dir_path, "README.md")
    with open(readme_path, 'w') as f:
        f.write(README_TEMPLATE.format(day=day))
    
    print(f"✅ Created structure for Year {year}, Day {day} at {dir_path}/")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python create_day.py <year> <day>")
        print("Example: python create_day.py 2025 2")
        sys.exit(1)
    
    year = sys.argv[1]
    day = int(sys.argv[2])
    
    if day < 1 or day > 25:
        print("Error: Day must be between 1 and 25")
        sys.exit(1)
    
    create_day(year, day)
