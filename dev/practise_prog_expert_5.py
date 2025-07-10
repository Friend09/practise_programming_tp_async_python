# https://www.programmingexpert.io/advanced-programming/asynchronous-programming/practice-questions/5

import asyncio
import time

async def append_two_values(lst, value1, value2):
    lst.append(value1)
    await asyncio.sleep(0.5)
    lst.append(value2)


lst = []

async def main(lst):
    futures = [
        append_two_values(lst,1,4),
        append_two_values(lst,3,6),
        append_two_values(lst,2,5)
    ]
    await asyncio.gather(*futures)

start_time = time.time()
asyncio.run(main(lst))
print(f"{time.time() - start_time:.2f} seconds!") # type: ignore

print(lst)
