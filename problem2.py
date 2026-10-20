'''def book_position(codes, wanted):
    count=0
    for i in range(len(codes)):
        if wanted==codes[i]:
            count=i
            break
    return wanted.index(codes)
codes=["BK103", "BK207", "BK103", "BK410"]
wanted=input("Which book do you need? ")'''

def book_position(codes, wanted):
    index=-1
    for i in range(len(codes)):
        if codes[i]==wanted:
            index=i
            break
    return index
codes=["BK103", "BK207", "BK103", "BK410"]


assert book_position(codes, "BK207")==1
assert book_position(codes, "BK103")==0
assert book_position(codes, "BK410")==3

print(book_position(codes, "BK207"))  # Natija: 1 chiqishi kerak
print(book_position(codes, "BK103"))  # Natija: 0 chiqishi kerak
print("Hamma testlar muvaffaqiyatli o'tdi!")

    