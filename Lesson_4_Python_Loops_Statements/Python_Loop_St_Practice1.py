#Loops Statement Pracie 1-16-2025
chapters_legacy = ["Chapter 1", "Chapter 2", "Chapter 3"]
pages_chapter = ["100", "200", "400"]
for book_chapters in chapters_legacy:
    for pages_in_chapters in pages_chapter:
        print("Lets read " + pages_in_chapters + " " "pages of" " " + book_chapters + " " "before end of week")
        #Note We cannot concatenate int (intergers) it will not work at least for right now.
for book_chapters in chapters_legacy:
        if book_chapters == "Chapter 2":
              break
