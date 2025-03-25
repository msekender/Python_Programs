'''
'Problem Recap
Given a list of non-overlapping rectangles, we must determine if we can make two horizontal or vertical cuts to divide the grid into three non-overlapping sections, such that:

Each section contains at least one rectangle.

No rectangle crosses a cut (i.e., each rectangle must lie fully within one section).'
'''

def can_cut_grid(n, rectangles):
    def check(rects, vertical=True):
        coords = set()
        for r in rects:
            coords.add(r[0] if vertical else r[1])
            coords.add(r[2] if vertical else r[3])
        sorted_coords = sorted(coords)

        for i in range(1, len(sorted_coords)):
            for j in range(i + 1, len(sorted_coords)):
                cut1, cut2 = sorted_coords[i], sorted_coords[j]
                sections = [0, 0, 0]  # left/bottom, middle, right/top
                valid = True

                for r in rects:
                    start = r[0] if vertical else r[1]
                    end = r[2] if vertical else r[3]

                    if end <= cut1:
                        sections[0] += 1
                    elif start >= cut2:
                        sections[2] += 1
                    elif start >= cut1 and end <= cut2:
                        sections[1] += 1
                    else:
                        valid = False  # rectangle spans across cuts
                        break

                if valid and all(count > 0 for count in sections):
                    return True

        return False

    return check(rectangles, vertical=True) or check(rectangles, vertical=False)


# 🔍 Test Cases
tests = [
    (5, [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]], True),
    (4, [[0, 0, 1, 1], [2, 0, 3, 4], [0, 2, 2, 3], [3, 0, 4, 3]], True),
    (4, [[0, 2, 2, 4], [1, 0, 3, 2], [2, 2, 3, 4], [3, 0, 4, 2], [3, 2, 4, 4]], False),
]

for n, rects, expected in tests:
    result = can_cut_grid(n, rects)
    print(f"n={n}, rects={rects} => {result} (Expected: {expected})")

'''
Time Complexity
Let:

N = number of rectangles

Each rectangle has 2 endpoints, so total endpoints = 2N

Let P = number of unique x or y coordinates (≤ 2N)

Steps:
Extract unique coordinates: O(N)

Sort coordinates: O(N log N)

Try all pairs of cuts (cut1, cut2): O(P^2)

For each pair, classify rectangles: O(N)

Total worst-case: O(P^2 * N)
In worst case, P = 2N ⇒ O(N^3)

Practical Optimizations:
Early termination when a valid cut is found.

Fewer unique coordinates (P ≪ 2N) in real scenarios.

Space Complexity
Storing unique coordinates: O(P) = O(N)

Auxiliary variables and section counts: O(1)

No extra structures per rectangle

Total Space: O(N) '''