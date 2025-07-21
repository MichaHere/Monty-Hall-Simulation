import random;

class Statistics:
    def __init__(self, size, samples, itterations = None):
        self.size = size;
        self.samples = samples;
        self.itterations = itterations or size - 1;

    def run(self, switch):
        wins = 0;
        losses = 0;

        for i in range(self.samples):
            game = Game(self.size);
            choice = random.randrange(0, self.size, 1);

            for i in range(self.itterations):
                options = game.play(choice);
                
                lastGame = i == self.itterations - 1;
                if switch and options and not lastGame:
                    options.remove(choice);
                    choice = random.choice(options);
            
            result = game.getResults(choice);

            wins = wins+1 if result else wins;
            losses = losses if result else losses+1;

        print(f"Wins: {wins}     Losses: {losses}      Ratio: { wins / (wins + losses) }")
    
    def compare(self):
        print("Run without changing the initial guess: ");
        self.run(False);
        print("\nRun by constantly changing the guess: ");
        self.run(True);

class Game:
    def __init__(self, size):
        self.size = size;
        self.doors = [0] * self.size;
        self.car = random.randrange(0, self.size, 1);

        self.chosen = None;
        self.done = False;

    def play(self, choice):
        if self.done:
            return;

        self.chosen = choice;

        if self.doors.count(0) > 2:
            self.eleminate();

            # for index, value in enumerate(self.doors):
            #     if value == 0:
            #         choosable.append(index);

            choosable = [index for index, value in enumerate(self.doors) if value == 0];
            return choosable;
        
        self.done = True;
        return;

    def getResults(self, choice):
        if choice == self.car:
            return True; # A win
        else:
            return False; # A loss    
    
    def eleminate(self):
        if self.done:
            return;

        # Get all the indexes
        indexes = list(range(len(self.doors)));

        for index, value in reversed(list(enumerate(self.doors))):
            if value == 1:
                indexes.pop(index);

        # Don't eleminate the chosen option or the car

        if self.chosen in indexes:
            indexes.remove(self.chosen);
        if self.car in indexes:
            indexes.remove(self.car);
        

        # Open a random door with a goat
        self.doors[random.choice(indexes)] = 1;


def main():
    doors = int(input("Number of doors (default is 3): ") or 3);
    itterations = 10_000;

    print(f"\nRunning with {doors} doors and {itterations} itterations. \n")

    stats = Statistics(doors, itterations);
    stats.compare();

if __name__=="__main__":
    main();