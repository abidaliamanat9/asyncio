import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

def loop():
    for _ in range(100000000):
       continue

def main():
    for _ in range(5):
        loop()

# async def main():
#     loop_count = 5
#     with ProcessPoolExecutor() as executor:
#         # Schedule the loop function to run in the thread pool
#         tasks = [asyncio.get_event_loop().run_in_executor(executor, loop) for _ in range(loop_count)]
#         await asyncio.gather(*tasks)


if __name__ == "__main__":
    s = time.perf_counter()
    # asyncio.run(main())
    main()
    elapsed = time.perf_counter()-s
    print(f"{__file__} take {elapsed:0.2f} seconds")