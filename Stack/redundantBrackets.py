def checkRedundancy(Str):
    st = []
    for ch in Str:
        if ch == ")":
            top = st[-1]
            st.pop()
            flag = True

            while top != "(":
                if top == "+" or top == "-" or top == "*" or top == "/":
                    flag = False
                top = st[-1]
                st.pop()

            if flag == True:
                return True

        else:
            st.append(ch)  
    return False


# Function to check redundant brackets
def findRedundant(Str):
    ans = checkRedundancy(Str)

    return ans


str = "(a+c*b)+(c)"

print(findRedundant(str))
