This project is a console-based software designed to simplify the daily work of a 
librarian. In many schools, library records are still kept in big registers, which makes 
finding a book or calculating fines very slow and error-prone. My project solves this by 
automating the entire process. It allows the librarian to digitally track which books are 
in stock, who has borrowed them, and when they are due. It acts as a central system 
to ensure books are returned on time and inventory is always up to date.
Features
1. Live Stock Tracking: The system doesn't just list books; it counts them. If there 
are 5 copies of "Python Programming" and one is issued, the system instantly 
updates the available count to 4.
2. Issue System: It records the student's name and the exact date and time when a 
book is borrowed. It also prevents a single student from borrowing multiple 
copies of the same book.
3. Automatic Fine Calculation: This is the key feature. When a book is returned, 
the system compares the return date with the issue date. If the duration 
exceeds 7 days, it automatically shows a fine of Rs 50.
4. Dynamic Database: We can add new books to the library at any time without 
restarting the program.
5. Validation: It stops users from doing invalid actions, like trying to borrow a book 
that isn't in stock or returning a book that was never issued.
Technologies/Tools Used
• Language: Python (Version 3.x) because it is easy to read and has powerful 
libraries.
• Concepts Used: Object-Oriented Programming (Classes & Objects) for 
structure, and Dictionaries for efficient data storage.
• Modules: The datetime module is used to handle real-time date and time 
tracking for issuing and returning.
• IDE: The code was written and tested on VS Code (Visual Studio Code), but it 
runs on any standard Python IDLE.
Steps to Install & Run the Project
1. Install Python: Ensure Python is installed on your computer. You can check this 
by typing python --version in your command prompt.
2. Save the Code: Copy the source code and save it as a Python file, for example: 
Library_management.py.
3. Open Terminal: Open your command prompt (cmd) or terminal and navigate to 
the folder where you saved the file.
4. Run the Command: Type python Library_management.py and hit Enter.
5. Interact: The menu will appear on the screen, and you can start using the 
system by entering numbers (1-5).
Instructions for Testing
To verify that the project works perfectly, follow these test cases:
1. Test Availability: Select Option 1 to see the list of books. Note the quantity of 
"Harry Potter".
2. Test Issuing: Select Option 2. Enter your name and "Harry Potter". You will see a 
success message. Check the list again (Option 1)—the quantity should be one 
less.
3. Test Out-of-Stock: Try to issue a book that has 0 quantity. The system should 
politely refuse.
4. Test Returning & Fine: Select Option 3. Enter the same name and book title.
o Note: Since we can't wait 7 days in real-time during a demo, you can 
verify the logic by temporarily changing the code limit from > 7 to > 0
seconds/days to see the fine message appear immediately.
5. Test Adding Stock: Select Option 4, add a new book name and quantity, and 
check Option 1 to see if it appears in the list.
