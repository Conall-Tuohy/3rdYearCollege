This is an old and original version of the LCATest file. Please ignore, Didn't want to delete as that would remove all traces of the file being uploaded
package com.company;


import com.sun.org.apache.xpath.internal.objects.XNull;

class Node {
    public Node prev;
    public Node left;
    public Node right;
    public int Value;

    Node(int value, Node prev, Node left, Node right){
        this.Value = value;
    }

}

public class Main {

    private static int maxDepth;
    private static int currentDepth;

    public static void main(String[] args) {
        int maxDepth =0;
        Node tree = setTree();
        Node highest = findHighestNode(tree);
        System.out.println("The lowest node in the tree is " + findDepth(highest) + " layers deep");
    }

    private static Node findHighestNode(Node tree) {
        while (tree.prev != null) {
            tree = tree.prev;
        }
        return tree;
    }

    private static int findDepth(Node highest) {
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

    private static void setLeft(Node main, Node left){
        main.left = left;
    }

    private static void setRight(Node main, Node right){
        main.right = right;
    }


    private static Node setTree(){
        Node tree = new Node(0, null,null,null);
        Node left1 = new Node(1,tree,null, null);
        setLeft(tree, left1);
        Node right1 = new Node(2 , tree, null, null);
        Node left2 = new Node(3, left1, null, null);
        setLeft(left1,left2);
        return tree;
    }


}
