import string

class Iterative_Nested_Word_Generator:
  def __init__(self):
    print("Iterative_nlNested_Word_Generator has been started.")
    # self.lowercase = string.ascii_lowercase          # a-z (26)
    self.lowercase = sorted(string.ascii_lowercase)          # a-z (26)
    # self.current_word = self.lowercase
    self.current_word = []
    self.iterative_nested_generator()
    # self.iterative_nested_generator(self.current_word)
    
  def iterative_nested_generator(self, given_word = ""):
    gw = given_word
    print(f"The given Word is = {gw}")
    created_word = []
    for lc in self.lowercase:
      created_word = [gw + lc]
      #created_word.append(gw + lc)
      print(f"The Created Word is = {created_word}")
      if len(created_word) <= 4:
        self.iterative_nested_generator(created_word[-1])
      elif len(created_word) > 4: return
    # yield created_word
    return created_word
if __name__ == "__main__":
  inwg = Iterative_Nested_Word_Generator()
  print(f"The Current Word Vocabulary are = {inwg.current_word}")
