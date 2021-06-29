import asyncio

###############################################
## 协程调度方式
###############################################

async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')

# asyncio.run(main())

# main()

import time

###############################################
## 并行的协程
###############################################

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

# async def main():
#     print(f"started at {time.strftime('%X')}")

#     await say_after(1, 'hello')
#     await say_after(2, 'world')

#     print(f"finished at {time.strftime('%X')}")

# async def main():
#     task1 = asyncio.create_task(
#         say_after(1, 'hello'))

#     task2 = asyncio.create_task(
#         say_after(2, 'world'))

#     print(f"started at {time.strftime('%X')}")

#     # Wait until both tasks are completed (should take
#     # around 2 seconds.)
#     await task1
#     await task2

#     print(f"finished at {time.strftime('%X')}")

# asyncio.run(main())

###############################################
## 可等待对象, 1. 协程，任务，Future
###############################################

# 协程函数
# async def nested():
#     return 42

# async def main():
#     nested()

#     print(await nested()) # 协程对象

# asyncio.run(main())

async def nested():
    return 42

async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    await task

asyncio.run(main())

