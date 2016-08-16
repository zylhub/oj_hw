class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def create_tree(inp,i,n):
    if i>=n:
        return None
    root = TreeNode(None)
    root.val = inp[i]
    root.left = create_tree(inp,2*i+1, n)
    root.right = create_tree(inp, 2*i+2, n)
    return root


def FindPath(root, expectNumber):
    if root == None or expectNumber == None:
        return []
    if root.val > expectNumber:
        return []
    elif root.val == expectNumber:
        if root.left or root.right:
            return []
        else:
            return [[root.val]]
    rst = []
    if root.left:
        rstleft = FindPath(root.left, expectNumber - root.val)
        if rstleft:
            for i in rstleft:
                i.insert(0, root.val)
                rst.append(i)
    if root.right:
        rstright = FindPath(root.right, expectNumber - root.val)
        if rstright:
            for i in rstright:
                i.insert(0, root.val)
                rst.append(i)
    if rst:
        return rst
    else:
        return []


import sys

try:
    while True:
        num = sys.stdin.readline().strip()
        if not num:
            break
        inp = sys.stdin.readline().strip().split(',')
        inp = map(int, inp)
        pRoot = create_tree(inp,0,len(inp))
        # print num, inp
        ret = FindPath(pRoot, int(num))
        # print ret
        if not ret:
            print 'error'
        else:
            for each in ret:
                print ','.join(map(str, each))
except:
    pass
