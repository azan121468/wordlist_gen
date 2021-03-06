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

def not_same(string):
    """return true if all characters are not same"""
    if len(set(string))==1:
         return False
    else:
         return True

def createWordList(chars, min_length, max_length, head, tail, output):
    """Creates wordlist based on given data"""
    global total_words
    if min_length > max_length:
        print ("[!] Please `min_length` must smaller or same as with `max_length`")
        sys.exit()

    print ('[+] Creating wordlist at `%s`...' % output)

    output = open(output, 'w')
    try:
        strings_to_write=[]
        reverse_of_strings_to_write=[]
        print("[+] Saving strings in memory")
        try:
            for n in range(min_length, max_length + 1):
                for i in itertools.product(chars, repeat=n):
                   word = head+''.join(i)+tail
                   reverse_word = head + ''.join(i)[::-1] + tail
                   strings_to_write.append(word)
                   if not_same(reverse_word):
                       reverse_of_strings_to_write.append(reverse_word)
        except MemoryError:
            print("[-] Memory Error has been occured")
            print("[-] Use big_wgen.py to generate wordlist")
            print("[+] Removing list from memory")
            del strings_to_write
            print("[+] Sucessfully deleted list from memory")
            sys.exit()
        except KeyboardInterrupt:
            print("[-] User has interrupt while chraracter were being saved in memory.")
            print("[+] Removing list from memory")
            del strings_to_write
            print("[+] Sucessfully deleted list from memory")
            sys.exit()
        print("[+] Removing duplicates if any")
        strings_to_write = list(set(strings_to_write))
        reverse_of_strings_to_write = list(set(reverse_of_strings_to_write))
        print("[+] Duplicates removed sucessfully")
        print("[+] Write in memory sucessful")
        print("[+] Writing strings on disk")
        for i in strings_to_write:
            output.write("%s\n" % i)
            sys.stdout.write('\r[+] saving character `%s`' % i)
            total_words += 1
            sys.stdout.flush()
        if (head or tail) and head!=tail:
            for m in reverse_of_strings_to_write:
                output.write("%s\n" % m)
                sys.stdout.write('\r[+] saving character `%s`' % m)
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
        print(f"\nNumber of words written are {total_words}")
    except PermissionError:
        print("[!] You have no permission to write here")
        print("[?] You need administrator permission to wrote here")

if __name__=="__main__":
    main()
