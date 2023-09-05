class library:
  def __init__ (self,book):
    self.book_list = book
  def show(self):
    print(*self.book_list)
  def lend_book(self,book_name):
    if book_name in self.book_list:
      self.book_list.remove(book_name)
      print("thank you,book issued")
      return True
    else:
      print("this is not available")
      return False


class customer:
  def __init__ (self):
    self.book_list = []
  def add_book(self,book_name):
    self.book_list.append(book_name)
  def request_book(self):
    print("enter the book: ")
    self.book = input()
    return self.book

lib_tvl=library(["book1","book2","book3","book4","book5","book2"])
lingam = customer()

while True:
  print("----------------------------------------------")
  print("select one option given below")
  print("1. show the book list","\n2. lending the book","\n0. exist")
  option = int(input())
  if option == 1:
    lib_tvl.show()
  elif option == 2:
    requested_book = lingam.request_book()
    status = lib_tvl.lend_book(requested_book)
    if status == True:
      lingam.add_book(requested_book)
  elif option == 0:
    break
