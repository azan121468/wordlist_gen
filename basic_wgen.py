import os
import sys
import itertools

total_words=0

def title():
    """display title box"""
    print("****************************")
    print("*    Wordlist Generator    *")
    print("*            By            *")
    print("*        Azan  Shahid      *")
    print("****************************")

def sort_string(string):
    """sort characters of string"""
    return_string=''.join(sorted(string))
    return return_string

def remove_duplicates(string):
    """remove duplicate words from string"""
    string=set(string)
    return_string=""
    for i in string:
        return_string+=i
    return_string=sort_string(return_string)
    return return_string

def createWordList(chars, min_length, max_length, output):
    global total_words
    if min_length > max_length:
        print("[!] Please `min_length` must smaller or same as with `max_length`")
        sys.exit()

    print('[+] Creating wordlist at `%s`...' % output)

    output = open(output, 'w')
    try:
        for n in range(min_length, max_length + 1):
            for i in itertools.product(chars, repeat=n):
                string_to_write = ''.join(i)
                output.write("%s\n" % string_to_write)
                sys.stdout.write('\r[+] saving character `%s`' % string_to_write)
                total_words += 1
                sys.stdout.flush()
    except KeyboardInterrupt:
        print("User Interrupt using Ctrl + C")

def main():
    """main part of program"""
    title()
    print("Enter characterset : ",end="")
    chars=input()
    if not chars:
        print("[-] No characterset was given")
        sys.exit()
    chars=remove_duplicates(chars)
    print("Enter minimum length : ",end="")
    min_length=int(input())
    print("Enter maximum length : ", end="")
    max_length = int(input())
    print("Enter output : ",end="")
    output=input() or "wordlist.txt"
    createWordList(chars, min_length, max_length, output)
    if not total_words:
        print("\nNo words written in disk")
    else:
        print(f"\nNumber of words written in disk : {total_words}")

if __name__ == '__main__':
    main()
