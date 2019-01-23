BEAD = 1
EMPTY = 0


def sort(items):
    """
    Sort the given items using bead sort.
    The items should be non-negative integers.
    """
    if not all(isinstance(item, int) for item in items) or any(item < 0 for item in items):
        raise ValueError("All items must be non-negative integers")
    beads = create_beads(items)
    beads = drop_beads(beads)
    return count_beads(beads)


def create_beads(items):
    """
    Create the beads from the given list of items.
    """
    num_cols = max(items) if items else 0
    rows = []
    for item in items:
        row = [BEAD] * item + [EMPTY] * (num_cols - item)
        rows.append(row)
    return rows


def drop_beads(beads):
    """
    Lets all the beads "drop".
    """
    num_rows = len(beads)
    num_cols = len(beads[0]) if beads else 0
    for row in range(num_rows - 1, 0, -1):
        for col in range(num_cols):
            _drop_from_above(beads, row, col)
    return beads


def count_beads(beads):
    """
    Returns the number of beads on each row.
    """
    return [row.count(BEAD) for row in beads]


def _drop_from_above(beads, row, col):
    # If there is a bead here, can't do anything
    if beads[row][col] == BEAD:
        return
    # Otherwise find the next bead above,
    # and drop it to the current position.
    for row_above in range(row - 1, -1, -1):
        if beads[row_above][col] == BEAD:
            beads[row][col] = beads[row_above][col]
            beads[row_above][col] = EMPTY
            break
