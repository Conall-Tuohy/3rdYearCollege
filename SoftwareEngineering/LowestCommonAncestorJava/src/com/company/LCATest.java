package com.company;


import com.sun.org.apache.xpath.internal.objects.XNull;

class Node {
    public Node prev;
    public Node left;
    public Node right;
    public int Value;

    Node(int value, Node prev, Node left, Node right){
        this.Value = value;
        this.left = left;
        this.right = right;
        this.prev = prev;
    }

    public void setLeft(Node left){ this.left = left; }
    public void setRight(Node right){
        this.right = right;
    }
}

public class LCATest {

    public static int maxDepth;
    public static int currentDepth;

    public static void main(String[] args) {
        int maxDepth =0;
        Node tree = setTree();
        Node highest = findHighestNode(tree);
        System.out.println("The lowest node in the tree is " + findDepth(highest) + " layers deep");
    }

    public static Node findHighestNode(Node tree) {
        while (tree.prev != null) {
            tree = tree.prev;
        } return tree;
    }

    public static int findDepth(Node highest) {
        if (currentDepth > maxDepth)   maxDepth = currentDepth;
        try {
            if (highest.left != null) {
                System.out.println(highest.Value);
                currentDepth++;
                findDepth(highest.left);
                currentDepth--;
            } else if (highest.right != null)
                currentDepth++;
            findDepth(highest.right);
            currentDepth--;
        } catch (NullPointerException e){}
        return maxDepth;
    }

    public static Node setTree(){
        Node tree = new Node(0, null,null,null);
        Node left1 = new Node(1,tree,null, null);
        tree.setLeft(left1);
        Node right1 = new Node(2 , tree, null, null);
        Node left2 = new Node(3, left1, null, null);
        left1.setLeft(left2);
        return tree;
    }


}
