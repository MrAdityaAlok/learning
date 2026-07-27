# Pythagorean Triplet

Welcome to Pythagorean Triplet on Exercism's Python Track.
If you need help running the tests or submitting your code, check out `HELP.md`.

## Introduction

You are an accomplished problem-solver, known for your ability to tackle the most challenging mathematical puzzles.
One evening, you receive an urgent letter from an inventor called the Triangle Tinkerer, who is working on a groundbreaking new project.
The letter reads:

> Dear Mathematician,
>
> I need your help.
> I am designing a device that relies on the unique properties of Pythagorean triplets — sets of three integers that satisfy the equation a² + b² = c².
> This device will revolutionize navigation, but for it to work, I must program it with every possible triplet where the sum of a, b, and c equals a specific number, N.
> Calculating these triplets by hand would take me years, but I hear you are more than up to the task.
>
> Time is of the essence.
> The future of my invention — and perhaps even the future of mathematical innovation — rests on your ability to solve this problem.

Motivated by the importance of the task, you set out to find all Pythagorean triplets that satisfy the condition.
Your work could have far-reaching implications, unlocking new possibilities in science and engineering.
Can you rise to the challenge and make history?

## Instructions

A Pythagorean triplet is a set of three natural numbers, {a, b, c}, for which,

```text
a² + b² = c²
```

and such that,

```text
a < b < c
```

For example,

```text
3² + 4² = 5².
```

Given an input integer N, find all Pythagorean triplets for which `a + b + c = N`.

For example, with N = 1000, there is exactly one Pythagorean triplet for which `a + b + c = 1000`: `{200, 375, 425}`.

~~~~exercism/note

The description above mentions [_mathematical sets_][math-sets], but also that a Pythagorean Triplet {a, b, c} _**must**_ be ordered such that a < b < c (_ascending order_). 

This makes Python's [`set` type][python-sets] unsuited to this exercise, since it is inherently _unordered_. 
You should return a [`list`][python-list] of `list`s instead (_e.g. `[[a, b, c]]`_). 
You can generate the triplets themselves in whichever order you would like, as the enclosing `list`'s order will be ignored in the tests. 

[math-sets]: https://en.wikipedia.org/wiki/Set_(mathematics)
[python-sets]: https://docs.python.org/3/tutorial/datastructures.html#sets
[python-list]: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
~~~~

## Source

### Created by

- @betegelse

### Contributed to by

- @behrtam
- @BethanyG
- @cmccandless
- @Dog
- @ikhadykin
- @kytrinyx
- @morganpartee
- @N-Parsons
- @olufotebig
- @omer-g
- @parinporecha
- @pheanex
- @rootulp
- @sjakobi
- @tqa236
- @yawpitch

### Based on

A variation of Problem 9 from Project Euler - https://projecteuler.net/problem=9