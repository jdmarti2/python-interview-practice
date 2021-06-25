"""Find two lines such that the container contains the most water."""


def maxarea(height):
    """Function takes list of heights and finds max area."""
    # Start from largest width and move towards taller containers
    n = len(height)
    left = 0
    right = n - 1
    max_area = min(height[left], height[right]) * (right - left)
    # Start with the maximum width container and go to a shorter
    # width container if there is a vertical line longer than the
    # current containers shorter line. This way we are compromising
    # on the width but we are looking forward to a longer length container.
    while (left < right):
        if height[left] < height[right]:
            left += 1
            max_area = max((min(height[left], height[right]) * (right - left)),
                           max_area)
        else:
            right -= 1
            max_area = max((min(height[left], height[right]) * (right - left)),
                           max_area)

    return max_area
