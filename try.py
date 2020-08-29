import sys


def solution(T):
  # Your solution goes here.
  if (T[0]!='?' and int(T[0])>2):
      return sys.stderr.write("Given value out of range")
  elif (T[3]!='?' and int(T[3])>5):
      print("e")
      return sys.stderr.write("Given value out of range")
  elif T[0]=='?':
      res='2'
      if T[1] =='?':
          res='2'
      elif int(T[1])>3:
          res ='1'
  elif T[1]=='?':
      if T[0]=='2':
          res='3'
      elif int(T[0])<=1 and T[3]=='?':
          res='5' 
      else:
          res='9'
  elif T[3]=='?':
      res='5'
  elif T[4]=='?':
      res='9'
  else:
      return T
    
  T = T.replace('?',res)
  
  return T

print(solution("26:??"))