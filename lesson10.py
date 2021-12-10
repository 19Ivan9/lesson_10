if __name__ == '__main__':
    print('tack1:')
    file = open('myfile.txt', 'w')
    file.write(input('enter txt:'))
    try:
        file = open('myfile.txt', 'r')
        print(file.read())
    except FileNotFoundError:
        print('file not found')
    finally:
        file.close()

    book_numbers = open('booknum.txt','w')