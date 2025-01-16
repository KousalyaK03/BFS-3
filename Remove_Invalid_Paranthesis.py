# Explain your approach in brief:
# The goal is to remove the minimum number of invalid parentheses to make the string valid.
# This is solved using BFS to explore all possible strings by removing parentheses one at a time.
# We stop processing when we find the first level of valid strings.

# Time Complexity: O(2^N), where N is the length of the string. Each character can either be included or excluded.
# Space Complexity: O(N * 2^N), where N is the maximum string length and 2^N is the number of generated strings.
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(string: str) -> bool:
            # Helper function to check if a string has valid parentheses
            balance = 0
            for char in string:
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1
                if balance < 0:  # More closing parentheses than opening
                    return False
            return balance == 0

        # Initialize BFS queue and seen set
        queue = [s]
        seen = set([s])
        result = []
        found = False

        while queue:
            current = queue.pop(0)
            
            # Check if the current string is valid
            if is_valid(current):
                result.append(current)
                found = True
            
            # If a valid string is found, stop generating further strings
            if found:
                continue
            
            # Generate all possible strings by removing one character at a time
            for i in range(len(current)):
                if current[i] not in "()":
                    continue
                # Create a new string by skipping the i-th character
                new_string = current[:i] + current[i+1:]
                if new_string not in seen:
                    seen.add(new_string)
                    queue.append(new_string)

        return result
