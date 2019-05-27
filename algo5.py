import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#word_tokenize accepts a string as an input, not a file.
stop_words = set(stopwords.words('english'))
# print(stop_words)
# line = File.read('text1.txt')
file1 = open("text1.txt",'r+')
line = file1.read()# Use this to read file content as a stream:
print(line[555:559])
words = line.split()
line  = list(line)
delcoor = []

#words = line.split()
# for r in words:
# 	if not r in stop_words:
# 		appendFile = open('filteredtext.txt','a')
# 		appendFile.write(" "+r)
# 		appendFile.close()

for r in words:
    print(r)


filestop = open("stopwords.txt")
stopline = filestop.read()
stopwordsnew = stopline.split( )
stopwordwithspace = []
for i in  range(len(stopwordsnew)):
    stopwordwithspace.append(" " + stopwordsnew[i] + " ")
    print(stopwordwithspace)

# if r in range(len())




# filestopintext = open("stopintext.txt")
# filenewfiltered = open("newfilteredwords.txt")

def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0    # hash value for pattern
    t = 0    # hash value for txt
    h = 1

    # The value of h would be "pow(d, M-1)% q"
    for i in range(M-1):
        h = (h * d)% q

    # Calculate the hash value of pattern and first window
    # of text
    for i in range(M):
        p = (d * p + ord(pat[i]))% q
        t = (d * t + ord(txt[i]))% q

    # Slide the pattern over text one by one
    for i in range(N-M + 1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters on by one
        if p == t:
            # Check for characters one by one
            for j in range(M):
                if txt[i + j] != pat[j]:
                    break

            j+= 1
            # if p == t and pat[0...M-1] = txt[i, i + 1, ...i + M-1]
            if j == M:
                # words = line.split(" ")
                # print(words)
                # # if line[i:i+M] in line:
                # #line.replace(line[i:i+M]," ")
                # # print(line[i:i+M])
                # for r in words:
                #     print(r)
                    # if r != line[i:i+M]:
                    #     appendFile = open('filteredtext.txt','a')
                	#     appendFile.write(r)
                	#     appendFile.close()
                # del words[i]
                  # for r in words:
                      # if r!=s[i:i+M]:
                      #   appendFile = open('filteredtext.txt','a')
                      #   appendFile.write(r)
                      #   appendFile.close()
                          print("Pattern found at index " + str(i))
                          i = int(i)
                          delcoor.append(i)
                      # new = ""
                      # for x in line[i+1:i+M-1]:
                      #        new += x
                      # print(new)
                    # # # for i in range(len())
                    # # for r in words:
                    #   if r!=new:
                    #      # print(r)
                    #      appendFile = open('filteredtext.txt','a')
                    #      appendFile.write(r + " ")
                    #      appendFile.close()
                # i = int(i)
                # for r in words:
                #     print(r)
                # if r !=line[i:i+M]:
                #     appendFile = open('filteredtext.txt','a')
                #     appendFile.write(r)
                #     appendFile.close()

        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i + M]))% q

            # We might get negative values of t, converting it to
            # positive
            if t < 0:
                t = t + q


d = 256

# pat  -> pattern
# txt  -> text
# q    -> A prime number


# def rabin_karp_search(pat, txt, q):
#     M = len(pat)
#     N = len(txt)
#     i = 0
#     j = 0
#     p = 0    # hash value for pattern
#     t = 0    # hash value for txt
#     h = 1
#
#     # The value of h would be "pow(d, M-1)% q"
#     for i in range(M-1):
#         h = (h * d)% q
#
#     # Calculate the hash value of pattern and first window
#     # of text
#     for i in range(M):
#         p = (d * p + ord(pat[i]))% q
#         t = (d * t + ord(txt[i]))% q
#
#     # Slide the pattern over text one by one
#     for i in range(N-M + 1):
#         # Check the hash values of current window of text and
#         # pattern if the hash values match then only check
#         # for characters on by one
#         if p == t:
#             # Check for characters one by one
#             for j in range(M):
#                 if txt[i + j] != pat[j]:
#                     break
#             j+= 1
#             # if p == t and pat[0...M-1] = txt[i, i + 1, ...i + M-1]
#             if j == M:
#                 words = line.split(" ")
#                 print(words)
#                 # if line[i:i+M] in line:
#                 #line.replace(line[i:i+M]," ")
#                 # print(line[i:i+M])
#                 for r in words:
#                     # print(r)
#                     if r != line[i:i+M]:
#                         appendFile = open('filteredtext.txt','a')
#                 	    appendFile.write(r)
#                 	    appendFile.close()
#
#                 # filestopintext.write(" "+line[i:i+M])
#                 #
#                 # wordsstopintext = filestopintext.split(" ")
#
#                 # for r in words:
#                 #     if not r in wordsstopintext:
#                 #         filenewfiltered = open("newfilteredwords.txt")
#                 #         filenewfiltered.append(" " + r)
#
#             print("Pattern found at index " + str(i))
#
#         # Calculate hash value for next window of text: Remove
#         # leading digit, add trailing digit
#         if i < N-M:
#             t = (d*(t-ord(txt[i])*h) + ord(txt[i + M]))% q
#
#             # We might get negative values of t, converting it to
#             # positive
#             if t < 0:
#                 t = t + q

# Driver program to test the above function
# txt = "GEEKS FOR GEEKS"
# pat = "GEEK"
prime_num = 101 # A prime number
#
# for i in  range len()


for i in range(len(stopwordwithspace)):
    search(stopwordwithspace[i],line, prime_num)

for i in range(len(delcoor)):
    del line[delcoor[i]:(delcoor[i]+len(stopwordwithspace[i]))]

appendFile = open('filteredtext.txt','a')
linestring = ''.join(line)
appendFile.write(linestring)
appendFile.close()
# for r in words:
#     appendFile = open('filteredtext.txt','a')
#     appendFile.write(r)
#     appendFile.close()
#

 # print(stopwordwithspace)
