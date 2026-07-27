import string

class Iterative_Nested_Word_Generator:
  def __init__(self, c = 4):
    print("Iterative_nlNested_Word_Generator has been started.")
    self.ch_len = c
    # self.lowercase = string.ascii_lowercase          # a-z (26)
    self.lowercase = sorted(string.ascii_lowercase)          # a-z (26)
    # self.current_word = self.lowercase
    self.current_word = []
    self.current_word = self.iterative_nested_generator()
    # self.iterative_nested_generator(self.current_word)
    
  def iterative_nested_generator(self, given_word = ""):
    gw = given_word
    print(f"The given Word is = {gw}")
    created_word = []
    if len(created_word) < self.ch_len:
      for lc in self.lowercase:
        created_word += [gw + lc]
        print(f"The Created Word is = {created_word}")
        if len(created_word[-1]) < self.ch_len:
          # self.iterative_nested_generator(created_word[-1])
          created_word[-1] = self.iterative_nested_generator(created_word[-1])
        #elif len(created_word) > 4: return
    else:
      return
    """
    for lc in self.lowercase:
      created_word += [gw + lc]
      #created_word.append(gw + lc)
      print(f"The Created Word is = {created_word}")
      if len(created_word[-1]) <= 4:
        self.iterative_nested_generator(created_word[-1])
      elif len(created_word) > 4: return
      """
    # yield created_word
    print(f"The Created Word is before return = {created_word}")
    return created_word
if __name__ == "__main__":
  inwg = Iterative_Nested_Word_Generator(2)
  print(f"The Current Word Vocabulary are = {inwg.current_word}")
