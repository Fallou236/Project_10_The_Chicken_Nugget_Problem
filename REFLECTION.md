Reflection: Python Project 10 — The Chicken Nugget Problem


1. What was the project about?
The objective of this project was to determine whether a given number of nuggets could be obtained using boxes containing 6, 9, and 20 nuggets. We also had to identify all the amounts that could not be made between 0 and 100, find the largest impossible amount, count the number of possible combinations for a given amount, and observe what happens when using even box sizes. Finally, we had to complete the extra task.
What were the main challenges and reflections?
For the first question, we did not encounter any major difficulties because everyone understood that we had to use the function provided at the end of the exercise.
The first challenge arose in Question 2. Initially, we wanted to display all the amounts that could not be made by defining a new function. However, we did not immediately consider that the next question required us to find the largest impossible amount. We realized that storing the impossible amounts in a list would make this easier. We therefore decided to create an empty list, add all the impossible amounts to it, and then find the maximum value.
For Question 4, we first tested different amounts manually to understand how the combinations worked. We then defined another function and used a counter to count the number of possible combinations for each amount.
The extra task generated the most discussion within our group. We had several questions:
Should we define a new function, given that the function we had already written required three parameters?
If we kept the same function, how could we make the program consider only the first two parameters when checking whether they were relatively prime?
How could we express the condition that the two parameters must have no common divisor other than 1, so that the largest impossible amount would be equal to (a \times b - a - b)?
Was it enough for the two numbers to be prime, or could one be prime while the other was not?
What exactly did the instruction mean by “boxes of size 1000”?
We spent considerable time discussing whether we needed a new function with two parameters, whether the parameters had to add up to 1000, or whether one of the parameters simply had to be 1000. We were also unsure which version of the function—one, two, or three parameters—we were expected to use.
What challenges did we face with GitHub?
In addition to the programming challenges, we encountered several difficulties while using Git and GitHub to manage our project.
Branch management: We had to switch between branches and understand the difference between our local branches and the corresponding remote branches on GitHub.
Merge conflicts: We encountered conflicts while integrating changes from different versions of the project. We had to identify the conflicting sections and resolve them carefully without losing our work.
Synchronizing branches: We experienced errors when running `git pull`, particularly when our local branch had diverged from the remote branch or when the branch did not have tracking information configured.
Unstaged changes: Git sometimes prevented us from pulling updates because it detected local modifications that had not been committed.
Python cache files: Files in `__pycache__`, such as `.pyc` files, were automatically modified when we ran our code. These files caused Git to report unwanted changes, even though we had not intentionally modified the source code. We learned to use `.gitignore` and `git restore` to manage these files appropriately.
Commit and push management: We also learned to check our Git status, review commit history, commit relevant changes, and push our work to the correct remote branch.
These difficulties helped us understand that GitHub collaboration requires more than uploading code. We must also manage branches carefully, understand Git's error messages, preserve local changes, and ensure that our work is properly synchronized with the remote repository.



2. How did you use AI as a teammate?
We spent a lot of time trying to understand what “a box of size 1000” meant in the exercise. To clarify the instruction, we copied it into an AI tool and asked it to explain the meaning of the expression.
We also used AI to help us understand some Git errors and identify appropriate commands when we encountered problems with pulling updates, managing branches, and handling generated Python files.
AI served as a support tool that helped us interpret instructions and troubleshoot technical problems. However, we still had to test commands, examine the results, and decide which solutions were appropriate for our project.


3. What solutions did we finally adopt?
After discussing different possibilities and testing several values, we decided to:
Define a new function that takes two parameters.
Import the `gcd` function from Python's `math` module to check whether the two parameters are relatively prime.
Display the largest amount that cannot be made.
Calculate (a \times b - a - b) and compare it with the result obtained by our function.
Finally, we understood that a box of size 1000 meant that one of the parameters was (c = 1000).
After testing different values manually, we observed that, for amounts between 0 and 100, whenever a combination was possible, the coefficient multiplying 1000 was always zero. In other words, no amount between 0 and 100 could include even one box containing 1000 nuggets.
We therefore concluded that, within this range, adding a very large box size of 1000 effectively made the problem behave like a two-parameter problem. This led us back to the previous question about relatively prime numbers and the formula for finding the largest impossible amount.
To address the GitHub challenges, we learned to inspect the working tree using `git status`, restore unwanted changes to generated files, configure branch tracking, and resolve conflicts before continuing synchronization. We also learned the importance of checking which branch we are on before pulling or pushing changes.


4. What did we learn from this project?
This project taught us several important lessons.
First, we learned that manually testing different values can help us understand a problem and identify patterns before writing the final solution.
Second, we discovered that Python's `math` module provides a built-in `gcd` function that makes it easier to determine whether two numbers are relatively prime.
Third, we improved our understanding of Git and GitHub, particularly branch management, commits, pushes, pulls, merge conflicts, and the importance of a clean working tree. We also learned that generated files should be excluded from version control when they are not part of the project source code.
Finally, the project gave each of us an opportunity to practise and consolidate the Python syntax and concepts we had learned in class. It also showed us the importance of teamwork, communicating different approaches, questioning our assumptions, and using AI responsibly to clarify instructions and troubleshoot problems.