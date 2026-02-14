```python
class Calculator:
    def __init__(self):
        pass

    def run(self):
        while True:
            # Main program loop

class ConsoleCalculator(Calculator):
    def __init__(self):
        super().__init__()

def main():
    calculator = ConsoleCalculator()
    calculator.run()

if __name__ == "__main__":
    main()
```