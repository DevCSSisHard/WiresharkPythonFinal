import re
# Some devious Regex.
patterns = [r'Frame \d+', r'Src:\s.+?\(((?:[0-9a-f]{2}:){5}[0-9a-f]{2})\)', r'Dst:\s.+?\(((?:[0-9a-f]{2}:){5}[0-9a-f]{2})\)', r'0[xX][0-9a-fA-F]+']

if __name__ == '__main__':
    with open('wireShark1.txt', 'r') as f:
        text = f.read()

    start = 'Frame'
    end = 'No.'
    startind = text.find(start)
    endind = text.find(end, startind + 1)
    newtext = text[startind:endind]
    print(startind)
    print(endind)
    print(newtext)
    matches = []
    # re.findall returns a list.
    for pattern in patterns:
        matches.extend(re.findall(pattern, newtext))
    print("REGEX FOUND MATCHES :")
    # Yes, there will be extra hexadecimal matches, but we can discard them because it seems Type will ALWAYS be first.
    # Note: If this is not the case, I can probably adjust to take Type: match to end of line and then regex hexadecimal
    print(matches)
    print(matches[0])
    print('Src: ', matches[1])
    print('Dst: ', matches[2])
    print('Type: ',matches[3])

    #print(text)





