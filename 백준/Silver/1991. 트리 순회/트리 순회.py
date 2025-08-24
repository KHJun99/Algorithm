class node():
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

def preorder(now, out):
    out.append(tree[now].key)
    if tree[now].left != '.':
        preorder(tree[now].left, out)
    if tree[now].right != '.':
        preorder(tree[now].right, out)

def inorder(now, out):
    if tree[now].left != '.':
        inorder(tree[now].left, out)
    out.append(tree[now].key)
    if tree[now].right != '.':
        inorder(tree[now].right, out)

def postorder(now, out):
    if tree[now].left != '.':
        postorder(tree[now].left, out)
    if tree[now].right != '.':
        postorder(tree[now].right, out)
    out.append(tree[now].key)


N = int(input())
tree = {}
for _ in range(N):
    n, l, r = map(str, input().split())
    tree[n] = node(n, l, r)

pre, ino, post = [], [], []
preorder('A', pre)
inorder('A', ino)
postorder('A', post)

print(*pre, sep = '')
print(*ino, sep = '')
print(*post, sep = '')