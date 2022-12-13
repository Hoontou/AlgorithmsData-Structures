class Node:
  def __init__(self, key):
    self.parent = None
    self.left = None
    self.right = None
    self.key = key
    self.height = 0

class AVL:
  def __init__(self):
    self.root = None
    self.count = 0 # 노드 갯수
  
  def insert(self, key): 
    #키가 들어갈 자리를 찾는다.
    #루트가 없다?
    if self.root == None:
      new_node = Node(key)
      self.root = new_node
      
    else: #루트가 있다.
      current = self.root
      p = current.parent
      
      while current != None: #현재를 계속 보면서, None이 뜨면 루프탈출.
      #키가 커렌트보다 작을때
        if current.key > key:
          current.height -= 1
          p = current
          current = current.left

    #키가 커렌트보다 클때
        elif current.key < key:
          current.height += 1
          p = current
          current = current.right
      #키가 커렌트일때.
        elif current.key == key:
          print('이미 존재하는 키 삽입중임')
          #다시 height를 되돌려 놓는다. 
          tmp_p = p
          cur_tmp = current
          while tmp_p != None:
            if tmp_p.left == cur_tmp: # 내가 들어온 곳이 왼쪽이면
              tmp_p.height += 1 #1을 더함으로써 다시 되돌려놓는다.
            else:
              tmp_p.height -= 1 #아니면 오른쪽으로 왔으므로 -1 한다.
          #height 수정 했으면 링크관계 다시 정리.
          #바라보는 노드가 부모노드가 되고, 부모노드는 그것의 부모가 된다.
            cur_tmp = tmp_p
            tmp_p = cur_tmp.parent
          return current # 다 되돌려 놨으면 이미 존재하는 키의 노드를 리턴.
    
    #그러면 이제 current는 새로운 노드가 들어갈 위치, p는 그것의 부모임.
      new = Node(key)
      if p.key > key:
        p.left = new
        new.parent = p
      else:
        p.right = new
        new.pareng = p
    
    ###노드 삽입이 끝났으면 ROTATION을 호출한다
    #self.rotation()
    
  def rotation(self):
    ##로테이션 정의.
    pass

avl = AVL()
avl.insert(10)
avl.insert(5)
avl.insert(8)
avl.insert(13)

print(avl.root.height)
print(avl.root.left.height)
avl.insert(8)

print(avl.root.height)
print(avl.root.left.height)
