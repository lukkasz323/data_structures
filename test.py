# type: ignore

from linked_list import LinkedList

def test_linked_list():
    linked_list = LinkedList()
    linked_list.add(17)
    linked_list.add('abc')
    print(linked_list)

def main():
    print(test_linked_list())
        
if __name__ == '__main__':
    main()