from DSAStack import DSAStack
from DSAQueue import CircularQueue

class EquationSolver(): 
    
    def __init__(self, equation):
        self.equation = equation

    def solve_equation(self):
        postfix_queue = self.parse_infix_to_postfix(self.equation)
        result = self.evaluate_postfix(postfix_queue)
        return result

    def parse_infix_to_postfix(self, equation):
        tokens = equation.split(" ")
        op_stack = DSAStack(len(tokens))
        postfix_queue = CircularQueue(len(tokens))
        for item in tokens:
            if item == "(":
                op_stack.push('(')
            elif item == ")":
                while op_stack.top() != '(':
                    postfix_queue.enqueue(op_stack.pop())
                op_stack.pop()
            
            elif (item == '+') or (item == '-') or (item == '*') or (item == '/'):
                while (
                    op_stack.is_empty() == False
                    and (op_stack.top() != '(' 
                    and self.precedence_of(op_stack.top()) >= self.precedence_of(item))
                ):
                    postfix_queue.enqueue(op_stack.pop())
                op_stack.push(item)
            else:
                postfix_queue.enqueue(float(item))
        while(op_stack.is_empty() == False):
            postfix_queue.enqueue(op_stack.pop())
        return postfix_queue


    def precedence_of(self, op):
        if op == "+" or op == "-":
            return 1
        elif op == "*" or op == "/":
            return 2
        else:
            raise RuntimeError("Not an operator")
            
    def evaluate_postfix(self, postfix_queue):
        evaluate_stack = DSAStack()
        while postfix_queue.is_empty() == False:
            item = postfix_queue.dequeue()
            if item == "+" or item == "-" or item == "*" or item == "/":
                op2 = evaluate_stack.pop()
                op1 = evaluate_stack.pop()
                result = self.execute_operation(item, op1, op2)
                evaluate_stack.push(result)
            else: 
                evaluate_stack.push(item)    
        return evaluate_stack.pop()


    def execute_operation(self, op, op1, op2):
        if op == '+':
            return op1 + op2
        elif op == '-':
            return op1 - op2
        elif op == '*':
            return op1 * op2
        elif op == '/':
            return op1 / op2
        else:
            raise RuntimeError("Not an operator")



answer = EquationSolver("( 10.3 * ( 14 + 3.2 ) ) / ( 5 + 2 - 4 * 3 )")
print(answer.solve_equation())