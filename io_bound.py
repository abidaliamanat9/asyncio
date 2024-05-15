import asyncio
import time

# def func_io_simple():
#     print('before sleeping')
#     time.sleep(5)
#     print('after sleeping')

# def main():
#     for _ in range(3):
#         func_io_simple()

async def func_io():
    print('before sleeping')
    await asyncio.sleep(5)
    print('after sleeping')

async def main():
    await asyncio.gather(func_io(),func_io(),func_io())

if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter()-s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")