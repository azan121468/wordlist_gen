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

def are_same(string):
    if len(set(string))==1:
        return True
    else:
        return False

def createWordList(chars, min_length, max_length, head, tail, output):
    """Creates wordlist based on given data"""
    global total_words
    if min_length > max_length:
        print ("[!] Please `min_length` must smaller or same as with `max_length`")
        sys.exit()

    print ('[+] Creating wordlist at `%s`...' % output)

    output = open(output, 'w')
    try:
        for n in range(min_length, max_length + 1):
            for i in itertools.product(chars, repeat=n):
                x = head + ''.join(i) + tail
                output.write("%s\n" % x)
                sys.stdout.write('\r[+] saving character `%s`' % x)
                total_words += 1
                sys.stdout.flush()
           
        if (head or tail) and head!=tail:
            for n in range(min_length, max_length + 1):
                for i in itertools.product(chars, repeat=n):
                    if not are_same(i):
                        x = head + ''.join(i[::-1]) + tail
                        output.write("%s\n" % x)
                        sys.stdout.write('\r[+] saving character `%s`' % x)
                        total_words += 1
                        sys.stdout.flush()
            print("\n[+] Write in disk sucessful")
    except KeyboardInterrupt:
        print("\nUser has exited using CTRL + C")
        print("[-] Write in disk was interrupted")


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
    print("Head (if any) : ",end="")
    head=input() or ""
    print("Tail (if any) : ",end="")
    tail=input() or ""
    print("Enter output : ",end="")
    output=input() or "wordlist.txt"
    try:
        createWordList(chars, min_length, max_length, head, tail, output)
        if total_words:
            print(f"\nNumber of words written are {total_words}")
        else:
            print("\nNo word written on disk")
    except PermissionError:
        print("[!] You have no permission to write here")
        print("[?] You need administrator permission to wrote here")

if __name__=="__main__":
    main()
