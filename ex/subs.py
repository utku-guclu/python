dictionary = ["below","down","go","going","horn","how","howdy","it","i","low","own","part","partner","sit"]

def substrings(text, dictionary):
    result = {}
    lowered_text = text.lower().split(" ")
    el = ""
    for e in dictionary:
        el += e
    
    for i in lowered_text:
        count = 0
        a = ""
        b = ""
        for x in i:
            a = i[:i.index(x)]
            b = i[i.index(x):]
            if a in el:
                count += 1
                result[a] = count
            elif b in el:
                count += 1
                result[b] = count
    return result
   
print(substrings("Howdy partner, sit down! How's it going?", dictionary))
#  => { "down" => 1, "go" => 1, "going" => 1, "how" => 2, "howdy" => 1, "it" => 2, "i" => 3, "own" => 1, "part" => 1, "partner" => 1, "sit" => 1 }
