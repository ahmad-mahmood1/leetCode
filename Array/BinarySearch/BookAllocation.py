def isPossible(arr, n, m, curr_min):
    studentsRequired = 1
    curr_sum = 0

    for i in range(n):
        # cannot assign page to student if page number is greater than page number
        if arr[i] > curr_min:
            return False

        # move to next student when pages alloted to student exceed min page number
        if curr_sum + arr[i] > curr_min:
            studentsRequired += 1
            curr_sum = arr[i]

            # moving to next student return false if var exceeds existng students
            if studentsRequired > m:
                return False
        else:
            # allocate pages to current student
            curr_sum += arr[i]

    return True


def findPages(arr, n, m):
    sum = 0

    # if no of books is greater than no of students
    if n < m:
        return -1

    # get all pages sum
    for i in range(n):
        sum += arr[i]

    start, end = 0, sum
    result = 10**9

    while start <= end:
        mid = (start + end) // 2

        if isPossible(arr, n, m, mid):
            # as we need minimum pages for each student
            # move to left of search space having smaller page number
            result = mid
            end = mid - 1

        else:
            start = mid + 1

    return result


arr = [10, 20, 30, 40]
n = len(arr)
m = 2  # students

print("Minimum number of pages = ", findPages(arr, n, m))
