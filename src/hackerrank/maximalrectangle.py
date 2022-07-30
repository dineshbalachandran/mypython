def largestRectangleArea(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    heights.append(0)
    print(heights)
    stack = []
    max_area = 0
    for i in range(len(heights)):        
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    return max_area


if __name__ == "__main__":
    rows = int(input())
    matrix = [input().split(',') for _ in range(rows)]
    
    m = len(matrix)
    n = len(matrix[0])
    max_area = 0
    heights = [0] * (n + 1)
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                heights[j] += 1
            else:
                heights[j] = 0
        max_area = max(max_area, largestRectangleArea(heights))

    print(max_area)
    
