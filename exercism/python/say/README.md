# Say

Welcome to Say on Exercism's Python Track.
If you need help running the tests or submitting your code, check out `HELP.md`.

## Introduction

Your friend Yaʻqūb works the counter at the busiest deli in town, slicing, weighing, and wrapping orders for a never-ending line of hungry customers.
To keep things moving, each customer takes a numbered ticket when they arrive.

When it’s time to call the next person, Yaʻqūb reads their number out loud, always in full English words to make sure everyone hears it clearly.

## Instructions

Given a number, your task is to express it in English words exactly as your friend should say it out loud.
Yaʻqūb expects to use numbers from 0 up to 999,999,999,999.

Examples:

- 0 → zero
- 1 → one
- 12 → twelve
- 123 → one hundred twenty-three
- 1,234 → one thousand two hundred thirty-four

## Exception messages

Sometimes it is necessary to [raise an exception](https://docs.python.org/3/tutorial/errors.html#raising-exceptions). When you do this, you should always include a **meaningful error message** to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. For situations where you know that the error source will be a certain type, you can choose to raise one of the [built in error types](https://docs.python.org/3/library/exceptions.html#base-classes), but should still include a meaningful message.

This particular exercise requires that you use the [raise statement](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement) to "throw" a `ValueError` if the number input to `say()` is out of range. The tests will only pass if you both `raise` the `exception` and include a message with it.

To raise a `ValueError` with a message, write the message as an argument to the `exception` type:

```python
# if the number is negative
raise ValueError("input out of range")

# if the number is larger than 999,999,999,999
raise ValueError("input out of range")
```

## Source

### Created by

- @behrtam

### Contributed to by

- @AndrejTS
- @cmccandless
- @csabella
- @Dog
- @fortrieb
- @gabriellhrn
- @ikhadykin
- @mandel01
- @N-Parsons
- @pheanex
- @pranasziaukas
- @tqa236
- @tsamoglou

### Based on

A variation on the JavaRanch CattleDrive, Assignment 4 - https://web.archive.org/web/20240907035912/https://coderanch.com/wiki/718804