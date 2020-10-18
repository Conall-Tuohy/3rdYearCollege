package com.company;

import org.junit.Test;
import static org.junit.jupiter.api.Assertions.*;

public class MainTest {
    @Test
    public void testSetLeftNode(){
        Node tree = new Node(0, null,null,null);
        Node left1 = new Node(1,tree,null, null);
        tree.setLeft(left1);
        assertEquals(tree.left, left1);
    }
    @Test
    public void testSetRightNode(){
        Node tree = new Node(0, null,null,null);
        Node right1 = new Node(1,tree,null, null);
        tree.setRight(right1);
        assertEquals(tree.right, right1);
    }

    @Test
    public void testFindHighestNode() {
        LCATest testMain = new LCATest();
        Node tree = new Node(0, null,null,null);
        Node left1 = new Node(1, tree,null, null);
        tree.setLeft(left1);
        Node right1 = new Node(2 , tree, null, null);
        Node left2 = new Node(3, left1, null, null);
        left1.setLeft(left2);
        System.out.println("The highest node was: " + testMain.findHighestNode(left2).Value + "\nThe top value was: " + tree.Value + "\nLeft1s prev was: " + (left1.left).Value);
        assertEquals(testMain.findHighestNode(left2), tree);
    }

    @Test
    public void TestFindDepth() {
        LCATest testMain = new LCATest();
        Node tree = new Node(0, null,null,null);
        Node left1 = new Node(1,tree,null, null);
        tree.setLeft(left1);
        Node right1 = new Node(2 , tree, null, null);
        Node left2 = new Node(3, left1, null, null);
        left1.setLeft(left2);
        assertEquals(testMain.findDepth(tree), 2);
    }
}