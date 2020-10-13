# 11. Testing

Interviewers are looking for:

* Big picture understanding
  * how to prioritize tests, some are more important
* Knowing how the pieces fit together
  * not just test the product, test the product that the product interacts with. integrations etc
* Organization
  * break down tests into sections
* Practicality

## Testing a piece of software

* Manual vs. automated testing
  * sometimes manual is necessary, human observation can reveal new issues that haven't been physically examined.
* Black box testing vs. white box testing
  * how much access do we have into the software?

An approach from start to end:

1. Are we doing black box testing or white box testing?
2. Who will use it and why?
3. What are the use cases?
4. What are the bounds of use?
5. What are the stress/failure conditions?
   1. Is it acceptable that the product fails, what should failure mean? It shouldn't crash the computer
6. What are the test cases? How would you perform the testing?

## Testing a function

1. Define test cases
   1. Normal case: generating the correct output for typical inputs
   2. Extreme cases: empty inputs, very small, very large inputs
   3. Nulls and 'illegal' input: if the function expects a number but a string is given
   4. Strange input: passing an already sorted array to a sort function, or a reverse sorted array
2. Define the expected results
3. Write test code

## Troubleshooting questions

How to debug or troubleshoot an existing issue. Instead of reinstalling the software, we can try a systematic approach

1. Understand the scenario
   1. How long has the user been experiencing this issue?
   2. What version of the browser is it? What OS?
   3. Does the issue happen consistently, or how often? When does it happen?
   4. Is there an error report that launches?
2. Break down the problem
   1. Break down the problem into testable units
3. Create specific, manageable tests
