"""
Write a function named add_one that accepts a coroutine as a mandatory parameter,
then calls the coroutine and returns the coroutine's return value plus one.
"""

import asyncio

async def add_one(coro):
    result = await coro()
    return result + 1

def example_coroutine():
    async def inner():
        return 41
    return inner()

def main():
    result = asyncio.run(add_one(example_coroutine()))
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
