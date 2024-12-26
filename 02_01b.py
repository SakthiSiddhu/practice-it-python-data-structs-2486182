from collections import deque
def main():
    #add code here
    recent_foods= deque(["Pizza", "Burger", "Pasta", "Sushi", "Tacos"],maxlen=5)
    print(recent_foods)
    recent_foods.extend(['Idli','Dosa'])
    # recent_foods.append('Dosa')
    print(recent_foods)
    return

if __name__ == "__main__":
    main()