def main():
     book_path = "books/frankenstein.txt"
     text = get_book_text(book_path)
     num_words = get_num_words(text)
     char_counts = get_char_counts(text)
     #print(f"{num_words} words found in the document")
     #print(char_counts)
     print_report(book_path,num_words,char_counts)

def get_book_text(path):
     with open(path) as f:
          return f.read()
     
def get_num_words(text):
     words = text.split()
     return len(words)

def get_char_counts(text):
     char_counts = {}
     words = text.split()
     for word in words:
          for letter in word:
               lowercase_letter = letter.lower()
               if lowercase_letter.isalpha():
                    if lowercase_letter in char_counts:
                         char_counts[lowercase_letter] += 1
                    else:
                         char_counts[lowercase_letter] = 1
     return char_counts

def print_report(book, word_count, char_counts):
     print(f"--- Begin report of {book} ---")
     print(f"{word_count} words found in the document\n")
     sorted_char_counts = list_and_sort(char_counts)
     for num_chars in sorted_char_counts:
          print(f"The '{num_chars["name"]}' character was found {num_chars["num"]} times")
     print("--- End report ---")

def sort_on(dict):
     return dict["num"]

def list_and_sort(dict):
     dict_list = []
     for d in dict:
          #tmp_list = list(d)
          dict_list.append({"name": d,"num": dict[d]})
     dict_list.sort(reverse=True,key=sort_on)
     return dict_list

main()

# with open("books/frankenstein.txt") as f:
#     file_contents = f.read()
#     pass

# def main():
#      word_count = file_contents.split()
#      print(len(word_count))

# main()