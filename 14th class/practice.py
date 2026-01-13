# import re

# text = "STEAM UP A Computer science portal for steam up"
# match = re.search(r'Computer',text)

# print(match)
# print("Matched Text:",match.group())
# print("Start Text:",match.start())
# print("End Text:",match.end())

# import re

# pattern = r"Computer"
# match = re.search(pattern,"A Computer Sceince")

# print(match)
# if match:
#     print("Matched Text:" , match.group())


# import re

# string = "The quick brown fox jumps over the lazy dog"
# pattern = "[a-n]"
# result = re.findall(pattern,string)

# print(result)

# import re
# regex = r"^The"
# strings = ['The quick brown fox', 'The lazy dog' , 'A quick brown fox']
# for string in strings:
#     if re.match(regex,string):
#         print(f"Matched : {string}")
#     else:
#         print(f"Not Matched : {string}")

# import re

# string = "Hello World!"
# pattern = r"World!$"

# match = re.search(pattern,string)
# if match:
#     print("Match Found! ")
# else:
#     print("Match Not Found.")


# import re

# string = "The quik brown fox jumps over the lazy dog."
# pattern = r"brown.fox"

# match = re.search(pattern , string)
# if match:
#     print("Match Found")
# else:
#     print("Match Not Found")

# import re 
# pattern = r"a|b"
# string = ['abc' , 'bcd' , 'abcd' , 'xyz']
# match = [s for s in string if re.search(pattern , s)]
# print(match)


# import re 
# pattern = r"ab?c"
# string = ['abc' , 'acb' , 'dabc' , 'abbc' , 'absc' , 'acbbbbsd']
# match = [s for s in string if re.search(pattern , s)]
# print(match)


# import re 
# pattern = r"ab*c"
# string = ['abc' , 'acb' , 'dabc' , 'abbc' , 'absc' , 'acbbbbsd']
# match = [s for s in string if re.search(pattern , s)]
# print(match)

# import re 
# pattern = r'a{2,4}'
# string = ['aaab' , 'baaaac' , 'gaad' , 'abc' , 'bc' ]
# match = [s for s in string if re.search(pattern , s)]
# print(match)


# import re 
# pattern = r'(a|b)cd'
# string = ['aacb' , 'abcd' , 'gacd' , 'abcd' , 'xyz' ]
# match = [s for s in string if re.search(pattern , s)]
# print(match)


# import re 
# pattern = r'\d'
# string = ['aacb' , 'ab123' , 'g1223' , '1223' ]
# match = [s for s in string if re.search(pattern , s)]
# print(match)

# import re 
# pattern = r'\D'
# string = ['aa' , 'ab123' , '1223'  ]
# match = [s for s in string if re.search(pattern , s)]
# print(match)

# import re 
# pattern = r'\s'
# string = ['hello world' , 'helloworld' , 'hello\nworld' ,  ]
# match = [s for s in string if re.search(pattern , s)]
# print(match)

# import re 
# pattern = r'\S'
# string = ['   ' , 'helloworld' , 'hello\nworld' ,  ]
# match = [s for s in string if re.search(pattern , s)]
# print(match)

# import re 
# string = """Hello my number is 0475943873 and my friend's number is 859440484"""
# pattern = r"\d+"
# match = re.findall(pattern , string)
# print(match)


# import re
# p = re.compile('[a-e]')

# print(p.findall("Aye , said Mr . Ali Abbas"))

