import random
import asyncio
import os
letters = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)] + [chr(i) for i in range(48, 58)] + [' ']
target = 'kbzx4'
def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
async def bruteforce_effect():
    current_str = [''] * len(target)
    for i in range(len(target)):
        while current_str[i] != target[i]:
            randNum = random.randint(0, len(letters) - 1)
            current_str[i] = letters[randNum]
            clear_screen()
            print(''.join(current_str))
            await asyncio.sleep(0.0005)
async def main():
    await bruteforce_effect()
asyncio.run(main())