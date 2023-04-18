import re
# Some devious Regex.
patterns = [r'Frame \d+', r'Src:\s.+?\(((?:[0-9a-f]{2}:){5}[0-9a-f]{2})\)', r'Dst:\s.+?\(((?:[0-9a-f]{2}:){5}[0-9a-f]{2})\)', r'0[xX][0-9a-fA-F]+']

def aFunction():
    # Get number of lines because we cant use len(f.readlines()) after we read the file.
    # x = sum(1 for line in open('wireShark1.txt'))
    # scratch last - I can just move the read position.

    with open('wireShark1.txt', 'r') as f:
        # thanks python.
        x = len(f.readlines())
        f.seek(0)
        text = f.read()

        start = 'Frame'
        end = 'No.'
        startind = text.find(start)
        endind = text.find(end, startind + 1)
        # print(x, startind, endind)
        while True:
            # print(text)
            newtext = text[startind:endind]
            # print(startind)
            # print(endind)
            # print(newtext)
            matches = []
            # re.findall returns a list.
            for pattern in patterns:
                matches.extend(re.findall(pattern, newtext))
            # print("REGEX FOUND MATCHES :")
            # Yes, there will be extra hexadecimal matches, but we can discard them because it seems Type will ALWAYS be first.
            # Note: If this is not the case, I can probably adjust to take Type: match to end of line and then regex hexadecimal
            # Yeah cheese method. If there is no more matching regex, quit.
            if len(matches) < 1:
                return
            print(matches[0]+',', 'Src: ', matches[1]+',', 'Des: ', matches[2]+',', 'Type: ', matches[3])
            # print('Src: ', matches[1])
            # print('Dst: ', matches[2])
            # print('Type: ',matches[3])
            # move the position in file?
            startind = endind
            endind = text.find(end, startind + 1)

if __name__ == '__main__':
    aFunction()

    #print(text)





