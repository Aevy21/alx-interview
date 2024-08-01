# Island Perimeter Calculator

This Python script contains a function `island_perimeter` that calculates the perimeter of an island represented in a grid. The grid is a 2D list where `1` represents land and `0` represents water. The function computes the perimeter of the island by considering only the land cells and their exposure to water or the grid's boundaries.

## Function

### `island_perimeter(grid)`

Calculates the perimeter of the island in a given grid.

#### Arguments

- `grid` (list of list of int): A 2D grid where each cell is either `1` (land) or `0` (water). The grid is rectangular, with its width and height not exceeding 100.

#### Returns

- `int`: The perimeter of the island, measured in units.

#### Description

- The function iterates over each cell in the grid.
- For each land cell (`1`), it initially assumes all 4 sides are exposed.
- It then checks adjacent cells (top, bottom, left, right). If an adjacent cell is also land, the shared edge is subtracted from the perimeter.
- The total perimeter is computed based on these adjustments.

## Example

Here's an example of how to use the `island_perimeter` function:

```python
grid = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
]

perimeter = island_perimeter(grid)
print(perimeter)  # Output: 12
