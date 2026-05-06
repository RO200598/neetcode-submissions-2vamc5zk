class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        match={")":"(" , "]":"[" , "}":"{"}

        for c in s:
            if c in match:
                if st and st[-1]==match[c]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c)
        return True if not st else False
