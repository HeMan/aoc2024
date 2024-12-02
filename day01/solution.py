#!/bin/env python
from typing import Dict, List

from pydantic import BaseModel


class Line(BaseModel):
    first: int
    second: int

    def __init__(self, value: str):
        super().__init__(**dict(zip(Line.model_fields, value.split())))


def parse(filename: str = "input.txt") -> List[Line]:
    with open("input.txt") as f:
        return [Line(line) for line in f.readlines()]


def part1(lines: List[Line]) -> int:
    first: List[int] = []
    second: List[int] = []
    val: int = 0
    for line in lines:
        first.append(line.first)
        second.append(line.second)

    for v in zip(sorted(first), sorted(second)):
        val += abs(v[0] - v[1])
    return val


def part2(lines: List[Line]) -> int:
    first: List[int] = []
    third: Dict[int, int] = {}
    val: int = 0
    for line in lines:
        first.append(line.first)
        if third.get(line.second):
            third[line.second] += 1
        else:
            third[line.second] = 1
    for v2 in first:
        if count := third.get(v2):
            val += v2 * count
    return val


def main():
    lines = parse()
    print(part1(lines))
    print(part2(lines))


if __name__ == "__main__":
    main()
