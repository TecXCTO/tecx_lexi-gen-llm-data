import string

class Iterative_nlNested_Word_Generator:
  def __init__(self):
    print("Iterative_nlNested_Word_Generator has been started.")
    lowercase = string.ascii_lowercase          # a-z (26)
    self.current_word = lowercase
    
  def iterative_nested_generator(self, given_word):
    gw = given_word
    for lc in lowercase:
      created_word = gw.append(lc)
      if len(created_word) < 4:
        self.iterative_nested_generator(created_word)
    yield created_word
    # return created_word
