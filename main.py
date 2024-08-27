from module import connect


## Use List Comprehensions:
## Creates lists concisely.
## Can be faster and more readable than traditional loops (in some cases).
names: list[str] = ['James', 'Charlotte', 'Stephany', 'Mario', 'Sandra']

# long_names: list[str] = []
# for name in names:
#     if len(name) > 7:
#         long_names.append(name)

## Better to write the code above
## using list comprehension
long_names: list[str] = [name for name in names if len(name) > 7]
print(f'Longa names: {long_names}')

## Use Type Annotations:
## Catches potential errors early (e.g., wrong data type).
## Improves code clarity and documentation (shows expected data types).
number: int = 10  # <- that is better use than number = 10 

# another example where type annotation can be useful
def upper_everything(elements):
    return [element.upper() for element in elements]
## The above code can be better defined 
def upper_everything(elements: list[str]) -> list[str]:
    # with the type annotation above, our code editer can infer 
    # the type of data we are dealing with
    # we get context actions 
    return [element for element in elements]

loud_list: list[str] = upper_everything(['Mario', 'James', 'Sandra'])


def greet() -> None:
    print('Hello, World!')

def bye() -> None:
    print('Bye, World!')


## We will re-write the following test case better 
## by using functions for each test case
# def enter_club(name: str, age: int, has_id: bool) -> None:
#     if name.lower() == 'bob':
#         print('Get out of here bob, we don\'t no trouble.')
#         return
#     if age >= 21 and has_id:
#         print('You may enter the club.')
#     else:
#         print('You may not enter the club.')



## Use smaller, reusable functions:
## Improves code readability and maintainability
## Easier to modify or reuse functionalities in different parts of the code
def is_an_adult(age: int, has_id: bool) -> bool:
    return age >= 21 and has_id

def is_bob(name: str) -> bool:
    return name.lower() == 'bob'

def enter_club(name: str, age: int, has_id: bool) -> None:
    if is_bob(name):
        print('Get out of here bob, we don\'t no trouble.')
        return
    
    if is_an_adult(age, has_id):
        print('You may enter the club.')
    else:
        print('You may not enter the club.')




## Define a main() function
## Organizes code by grouping functionalities
## Makes code structure similar to other languages (e.g. Java)
def main() -> None:
    # greet()
    # bye()
    enter_club('Bob', 29, has_id=True)
    enter_club('James', 29, has_id=True)
    enter_club('Sandra', 29, has_id=False)
    enter_club('Mario', 20, has_id=True)


# Check if __name__ == '__main__'
# Ensures the correct script runs when executed directly
# Helps identify the script's purpose (meant to be run or just imported)
if __name__== '__main__':
    main()