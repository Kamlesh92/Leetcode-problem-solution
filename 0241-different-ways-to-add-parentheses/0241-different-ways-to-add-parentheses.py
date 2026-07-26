class Solution:
    def __init__(self):
        self.map = {}  # Memoization map to store already computed results
  #BY KAMLESH  
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Step 1: Check if the result for the current expression is already computed
        if expression in self.map:
            return self.map[expression]

        result = []

        # Step 2: Traverse the expression to find operators (+, -, *)
        for i in range(len(expression)):
            ch = expression[i]

            # Step 3: If the character is an operator, split the expression into left and right parts
            if ch in '*+-':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])

                # Step 4: Combine the results from left and right sub-expressions
                for l in left:
                    for r in right:
                        if ch == '+':
                            result.append(l + r)  # Add the results
                        elif ch == '-':
                            result.append(l - r)  # Subtract the results
                        elif ch == '*':
                            result.append(l * r)  # Multiply the results

        # Step 5: Base case - If there were no operators, it means the expression is a single number
        if not result:
            result.append(int(expression))  # Convert string to integer

        # Step 6: Store the result in the map to avoid redundant computation
        self.map[expression] = result

        # Step 7: Return the final computed result
        return result