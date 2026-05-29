key = input().strip()
q = int(input())

def get_colors(key, guess):
    if len(key) != len(guess):
        return None
    
    if guess == key:
        return 'G' * len(key)
    

    from collections import Counter
    key_count = Counter(key)
    
    result = [''] * len(key)
    
  
    for i in range(len(key)):
        if key[i] == guess[i]:
            result[i] = 'G'
            key_count[key[i]] -= 1
    
   
    for i in range(len(key)):
        if result[i] == '': 
            char = guess[i]
            if char in key_count and key_count[char] > 0:
                result[i] = 'Y'
                key_count[char] -= 1
            else:
                result[i] = 'R'
    
    return ''.join(result)


game_over = False

for _ in range(q):
    guess = input().strip()
    
    if game_over:
        print("Game Over")
        continue
    
    if len(guess) != len(key):
        print("Invalid Length")
        continue
    
    colors = get_colors(key, guess)
    print(colors)
    
    if guess == key:
        game_over = True