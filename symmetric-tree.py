"""
https://leetcode.com/problems/symmetric-tree/
"""


# Might be gross, but works like a charm!
def isSymmetricRecursive(self, root):

    self.symmetric = True

    def compare(n1, n2):

        if (not n1 and n2) or (not n2 and n1):
            self.symmetric = False

        elif not n1 and not n2:
            pass

        elif n1.val != n2.val:
            self.symmetric = False

    def dfs(n1, n2):

        if n1 and n2:

            compare(n1.left, n2.right)

            if self.symmetric:

                dfs(n1.left, n2.right)

                if self.symmetric:

                    compare(n1.left, n2.right)

                    if self.symmetric:
                        dfs(n1.right, n2.left)

    dfs(root, root)

    return self.symmetric
