
###### Question: Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" and t = "ad", then the function returns True. Your function definition should look like: question1(s, t) and return a boolean True or False. ######

import collections

def check_anagram(string1,string2):
  length_string2 = len(string2);
  count_string2 = {};
  count_string1 = {};
  all_comparedStr = [];
  
  # construct a dictionary of each character and its occurance for shorter string
  for i in string2:
    letter_occurance_in_string2 = string2.count(i);
    count_string2[i]=letter_occurance_in_string2
  
  all_comparedStr = extract_Str(string1,length_string2)
  
  # construct a dictionary of each character and its occurance for each set of the longer string, finally compare the 2 dictionary
  for x in all_comparedStr:
    count_string1 = collections.Counter(x)
    # if the two dictionary matches then the shorter string is a anagram substring of the longer string
    if count_string1 == count_string2:
      return True
  return False
 
 
# Chopped string at specific length into set
def extract_Str(string,length):
  all_sets = [];
  for i in range(len(string)):
    set = string[i:i+length];
    all_sets.append(set);
  return all_sets
 
 
print "Expected: True"
print check_anagram("udacity","da")
print "Expected: True"
print check_anagram("banana","anb")
print "Expected: False"
print check_anagram("4732890793878894351", "13") 
 
 
