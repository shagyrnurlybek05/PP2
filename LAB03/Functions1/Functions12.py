def histogram(nums):
    for num in nums:
        if num is not None:
            print(f"{'#' * num}")
data = list(map(int, input().split()))
histogram(data)