# SMART5🤓
#### Video Demo: https://youtu.be/yxg3NAgxW8k
#### Description:

# General Info About The Website

    SMART50 is designed to help students organize their schoolwork. Students can organize their homework and create a virtual
vocabulary with the help of SMART50. The design of the website is simple and neat at the same time. Every student has a portal which they access by logging in. There are two main web pages on this website: homework and vocabulary.

## Homework Web Page

    The homework web page contains a table where students can write down their homework. The table contains 4 columns: subject,
materials required, description, and deadline. In the subject column, the students choose the subject from which the homework was given from the select menu (e.g. math, physics, etc.). The column called materials required is where the students can write what is required to complete their homework. Hence, students will know what they need to take home when packing their bags. The other column called description is where the students write down what the homework is (e.g. read ten pages from the book, finish the worksheet, etc.). The last column called deadline is where students save the deadlines of the homework so that they stay aware of the upcoming homework deadline. As you add homework to the table, a button will appear next to the row created whose function is to delete the homework from the table and the database when completed.

## Vocabulary Web Page

    The second web page, vocabulary, is a virtual vocabulary where students can add words of their own choice. This web page contains
two buttons. One of which allows you to append a word manually by filling in all the required fields such as definition and part of speech. The other of which allows you to append the word automatically by just typing in the word. For automating this process, I used the web scrapping method. For this, I exploited three dictionaries: britannica (britannica.com), wordhippo (wordhippo.com), and yourdicitionary (yourdictionary.com). The words are displayed in flashcards composed of words, parts of speech, definitions, synonyms, antonyms, and sample sentences. Each flashcard comprises a button to delete the word from the database, thus, deleting the flashcard from the web page.


### Other Files

In project.db, I created three tables: users, homework, and vocab. In the templates folder, there are html codes for various web pages. In addition, I utilized some code from the cs50 (pset 9).