class Solution:
  def __hasLowercaseLetter(self, password: str) -> bool:
    for i in password:
      if i.islower(): return True
    return False

  def __hasUppercaseLetter(self, password: str) -> bool:
    for i in password:
      if i.isupper(): return True
    return False

  def __hasAtLeastEightChars(self, password: str) -> bool:
    return len(password)>=8

  def __hasDigit(self, password: str) -> bool:
    for i in password:
      if i.isnumeric(): return True
    return False

  def __hasSpecial(self, password: str) -> bool:
    special="!@#$%^&*()-+"
    for i in password:
      if i in special: return True
    return False

  def __noDoubles(self, password: str) -> bool:
    lastChar=""
    for i in password:
      if i==lastChar: return False
      lastChar=i
    return True
  
  def strongPasswordCheckerII(self, password: str) -> bool:
    if self.__hasLowercaseLetter(password) and self.__hasUppercaseLetter(password) and self.__hasAtLeastEightChars(password) and self.__hasDigit(password) and self.__hasSpecial(password) and self.__noDoubles(password): return True
    return False
