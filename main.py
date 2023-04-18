import re
# devious regex
patterns = [r'Frame \d+', r'Src:\s.+?\(((?:[0-9a-f]{2}:){5}[0-9a-f]{2})\)', r'Dst:\s.+?\(((?:[0-9a-f]{2}:){5}[0-9a-f]{2})\)', r'0[xX][0-9a-fA-F]+']
# Stuff from the 'hints and notes'
# samples of searching/splitting a string.
def sampleCode():
    seedStr = "Internet Protocol Version 4"
    a_Str = "Internet Protocol Version 4, Src: 192.168.1.180, Dst: 239.255.255.250"
    x = a_Str.find(seedStr)
    print(x)

    x_str = "(I am Fisrt Last)"
    x = x_str.find(seedStr)
    print(x)

    x = x_str[1:len(x_str) - 1]
    print(x)

    a_str = "Internet Protocol Version 4, Src: 192.168.1.180, Dst: 239.255.255.250"
    a_parts = a_str.split(", ")
    print(a_parts)

    x = a_parts[0]
    words = x.split()
    print(words)

    x = a_parts[2]
    words = x.split()
    print(words)


if __name__ == '__main__':
    #sampleCode()
    with open('wireShark1.txt', 'r') as f:
        text = f.read()

    start = 'Frame'
    end = 'No.'
    #for line in f:
    startind = text.find(start)
    endind = text.find(end, startind + 1)
    newtext = text[startind:endind]
    print(startind)
    print(endind)
    print(newtext)
    matches = []
    # re.findall returns a list. Gotta adjust and add onto a list I guess.
    for pattern in patterns:
        matches.extend(re.findall(pattern, newtext))
    print("REGEX FOUND MATCHES :")
    # yes there will be extra hexadecimal matches, but we can discard them because it seems Type will ALWAYS be first.
    # Note: If this is not the case, I can probably adjust to take Type: match to end of line and then regex hexadecimal
    print(matches)
    print(matches[0])
    print('Src: ', matches[1])
    print('Dst: ', matches[2])
    print('Type: ',matches[3])

    #print(text)





