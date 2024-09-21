import asyncio

async def greet(name):
    print(f"Hallo, {name}!")
    await asyncio.sleep(1)
    print("Fertig!")

async def main():
    task1 = asyncio.create_task(greet("Welt"))
    task2 = asyncio.create_task(greet("Python"))
    await asyncio.gather(task1, task2)

asyncio.run(main())