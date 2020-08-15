import os
import sys
import itertools
import sys

total_words=0

def title():
    """display title box"""
    print("****************************")
    print("*    Wordlist Generator    *")
    print("*            By            *")
    print("*        Azan  Shahid      *")
    print("****************************")

def remove_duplicates(string):
    """remove duplicate words from string"""
    string=set(string)
    return_string=""
    for i in string:
        return_string+=i
    return_string=sort_string(return_string)
    return return_string

def sort_string(string):
    """sort characters of string"""
    return_string=''.join(sorted(string))
    return return_string



def createWordList(chars, min_length, max_length, head, tail, output):
    """Creates wordlist based on given data"""
    global total_words
    if min_length > max_length:
        print ("[!] Please `min_length` must smaller or same as with `max_length`")
        sys.exit()

    print ('[+] Creating wordlist at `%s`...' % output)

    output = open(output, 'w')

    try:
        reverse_chars=[]
        for n in range(min_length, max_length + 1):
            for i in itertools.product(chars, repeat=n):
                chars = head+''.join(i)+tail
                reverse_chars.append(chars[::-1])
                output.write("%s\n" % chars)
                sys.stdout.write('\r[+] saving character `%s`' % chars)
                total_words+=1
                sys.stdout.flush()
            for i in reverse_chars:
                output.write("%s\n" % i)
                sys.stdout.write('\r[+] saving character `%s`' % i)
                total_words += 1
                sys.stdout.flush()
        output.close()
    except KeyboardInterrupt:
        print("\nUser has exited using CTRL + C")


def main():
    """main part of program"""
    title()
    print("Enter characterset : ",end="")
    chars=input()
    chars=remove_duplicates(chars)
    print("Enter minimum length : ",end="")
    min_length=int(input())
    print("Enter maximum length : ", end="")
    max_length = int(input())
    print("Head (if any) : ",end="")
    head=input() or ""
    print("Tail (if any) : ",end="")
    tail=input() or ""
    print("Enter output : ",end="")
    output=input()
    try:
        createWordList(chars, min_length, max_length, head, tail, output)
        print(f"\nNumber of words written are {total_words}")
    except PermissionError:
        print("[!] You have no permission to write here")
        print("[?] You need administrator permission to wrote here")
main()
