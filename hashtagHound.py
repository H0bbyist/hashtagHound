
# Tool to list and study hashtags in a text document
# Version 1.0


import re
import operator


def main():
    while True:
        
        source = input("What file are we looking at? Or quit?(q) ")
        if source == "q":
            exit()
        else:
            file_object = open(source, 'r')
            text = file_object.read()
            
            raw = re.findall(r'#\w*',text)
            file_object.close()
            
            hashes = {

            }
            for x in raw:
                if x not in hashes:
                    hashes[x] = 1
                else:
                    hashes[x] += 1
            sorted_hashes = sorted(hashes.items(), key=operator.itemgetter(1))

            print(sorted_hashes)
          

    

if __name__ == '__main__':
    main()
