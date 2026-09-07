class DotCom:
    def __init__(self):
        # Holds the ship's cells (e.g., [2, 3, 4])
        self.location_cells = []

        # Counts the number of hits
        self.num_of_hits = 0

    def set_location_cells(self, locs):
        # Store a copy to avoid outside changes
        self.location_cells = locs.copy()

    def check_yourself(self, user_input):
        try:
            guess = int(user_input)
        except ValueError:
            return "miss"  # invalid input counts as miss

        # Scan the list for a hit
        # Mark a hit by replacing the cell with -1
        for i in range(len(self.location_cells)):

            if self.location_cells[i] == guess:

                self.location_cells[i] = -1
                self.num_of_hits += 1

                if self.num_of_hits == len(self.location_cells):
                    return "kill"

                return "hit"

        return "miss"