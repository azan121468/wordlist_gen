import os
import sys
import string
import itertools
import sys

def title():
    print("****************************")
    print("*    Wordlist Generator    *")
    print("*            By            *")
    print("*        Azan  Shahid      *")
    print("****************************")
def remove_duplicates(str_of_chars):
    set_of_chars=set(str_of_chars)
    string=""  #string which functio will return
    for i in set_of_chars:
        string+=i
    return string
def combination(n,r):
   pass

def createWordList(chrs, min_length, max_length, head, tail, output):

    if min_length > max_length:
        print ("[!] Please `min_length` must smaller or same as with `max_length`")
        sys.exit()

    print ('[+] Creating wordlist at `%s`...' % output)

    output = open(output, 'w')

    try:
        for n in range(min_length, max_length + 1):
            for i in itertools.product(chrs, repeat=n):
                chars = head+''.join(i)+tail
                output.write("%s\n" % chars)
                sys.stdout.write('\r[+] saving character `%s`' % chars)
                sys.stdout.flush()
        output.close()
    except KeyboardInterrupt:
        print("\nUser has exited using CTRL + C")


def main():
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
    except PermissionError:
        print("[!] You have no permission to write here")
        print("[?] You need administrator permission to wrote here")
main()
