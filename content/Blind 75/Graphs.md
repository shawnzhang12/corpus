---
title: "Graphs"
weight: -20
---

### Flood Fill :green_book:

##### Problem

An image is represented by an `m x n` integer grid `image` where `image[i][j]` represents the pixel value of the image. You are also given three integers `sr`, `sc`, and `color`. You should perform a **flood fill** on the image starting from the pixel `image[sr][sc]`. To perform a **flood fill**, consider the starting pixel, plus any pixels connected **4-directionally** to the starting pixel of the same color as the starting pixel, plus any pixels connected **4-directionally** to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with `color`.

Return *the modified image after performing the flood fill*.

##### Solution

Our solution will use recursion. Basically we want to check the current pixel and then check its corresponding 4-directionally connected pixels whether they are the same color as the starting pixel or already the desired color.

In our recursive function, 

1. Check if the current pixel coordinates are out of bounds, if they are we can just return nothing. 

2. Check whether the current pixel is not the same color as the starting pixel or that it is already the desired color, if it is return nothing.
3. Change current pixel color to the one desired.
4. Check its surrounding pixels.

Now we just call the function on our starting pixel and it will flood fill the rest.

Time Complexity: O(mn)

Space Complexity: O(1)

```python
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        start_color = image[sr][sc]

        def flood_fill(x, y):
            if x < 0 or y < 0 or x >= len(image) or y >= len(image[0]):
                return

            if image[x][y] != start_color or image[x][y] == color:
                return

            image[x][y] = color

            flood_fill(x-1,y)
            flood_fill(x+1,y)
            flood_fill(x,y-1)
            flood_fill(x,y+1)

        flood_fill(sr,sc)
        return image
```

