package com.company;


import edu.princeton.cs.algs4.StdOut;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class LinkedList<Item> implements Iterable<Item>
{
    private int N;
    private Node first;
    private Node last;

    private class Node
    {
        private Item item;
        private Node next;
    }

    public LinkedList()
    {
        first = null;
        last  = null;
    }

    public LinkedList(Item[] a)
    {
        for (Item t : a)
            append(t);
    }

    public LinkedList(Iterable<Item> coll)
    {
        for (Item t : coll)
            append(t);
    }

    public boolean isEmpty()
    {
        return first == null;
    }

    public int size()
    {
        return N;
    }

    public Item first()
    {
        if (isEmpty()) throw new RuntimeException("List is empty");
        return first.item;
    }

    public Item last()
    {
        if (isEmpty()) throw new RuntimeException("List is empty");
        return last.item;
    }

    public Item removeFirst()
    {
        if (isEmpty()) throw new RuntimeException("List is empty");
        Item item = first.item;
        first = first.next;
        N--;
        if (isEmpty()) last = null;   // to avoid loitering
        return item;
    }

    public void prepend(Item item)
    {
        Node x = new Node();
        x.item = item;
        if (isEmpty()) { first = x;      last = x;  }
        else           { x.next = first; first = x; }
        N++;
    }

    public void append(Item item)
    {
        Node x = new Node();
        x.item = item;
        if (isEmpty()) { first = x;     last = x; }
        else           { last.next = x; last = x; }
        N++;
    }

    public String toString()
    {
        StringBuilder s = new StringBuilder();
        for (Item item : this)
            s.append(item + " ");
        return s.toString();
    }

    public Iterator<Item> iterator()
    {
        return new ListIterator();
    }

    private class ListIterator implements Iterator<Item>
    {
        private Node current = first;

        public boolean hasNext()  { return current != null;                     }
        public void remove()      { throw new UnsupportedOperationException();  }

        public Item next()
        {
            if (!hasNext()) throw new NoSuchElementException();
            Item item = current.item;
            current = current.next;
            return item;
        }
    }

    /*****************
     * Exercise 1.3.19
     *****************/
    public Item removeLast()
    {
        if (isEmpty()) throw new RuntimeException("List is empty");
        if (first == last) return removeFirst();
        Item item = last.item;

        Node prev = null,
                curr = first;
        while (curr.next != null)
        {
            prev = curr;
            curr = curr.next;
        }
        prev.next = null;
        last = prev;
        N--;

        return item;
    }

    /*****************
     * Exercise 1.3.20
     *****************/
    public Item delete(int k)
    {
        if (k < 1) return null;

        int i = 1;
        Node prev = null,
                curr = first;

        while (i < k && curr != null)
        {
            prev = curr;
            curr = curr.next;
            i++;
        }

        if (curr != null)
        {
            if (prev == null)
                first = curr.next;
            else
                prev.next = curr.next;

            if (curr.next == null)
                last = prev;

            N--;
            return curr.item;
        }
        else
            return null;
    }

    /*************************************
     * Exercise 1.3.21
     * (Renamed from find() to contains())
     *************************************/
    public boolean contains(Item item)
    {
        Node curr = first;
        while (curr != null && !curr.item.equals(item))
            curr = curr.next;
        return curr != null;
    }

    /*****************
     * Exercise 1.3.26
     *****************/
    public void remove(Item item)
    {
        LinkedList<Integer> idx = new LinkedList<Integer>();
        int i = 1;

        for (Item x : this)
        {
            if (x.equals(item))
                idx.prepend(i);
            i++;
        }

        for (int k : idx)
            delete(k);
    }

    /***************************************
     * Recursive solution to Exercise 1.3.26
     ***************************************/
    public void removeRec(Item item)
    {
        first = remove_Node(first, item);
        setLastAndN();
    }

    private Node remove_Node(Node node, Item item)
    {
        if (node != null)
        {
            Node rest = remove_Node(node.next, item);

            if (node.item.equals(item))
                return rest;
            else
            {
                node.next = rest;
                return node;
            }
        }
        else
            return null;
    }

    private void setLastAndN()
    {
        last = first;
        N = 0;
        if (first != null)
        {
            N++;
            while (last.next != null)
            {
                last = last.next;
                N++;
            }
        }
    }


    /*********************
     * Operations on nodes
     *********************/

    public Node node(int k)
    {
        if (k < 1) return null;

        int i = 1;
        Node curr = first;

        while (i < k && curr != null)
        {
            curr = curr.next;
            i++;
        }

        return curr;
    }

    public Node createNode(Item item)
    {
        Node node = new Node();
        node.item = item;
        return node;
    }

    /*****************
     * Exercise 1.3.24
     *****************/
    public void removeAfter(Node node)
    {
        if (node != null && node.next != null)
        {
            if (node.next.next == null)
                last = node;
            node.next = node.next.next;
            N--;
        }
    }

    /*****************
     * Exercise 1.3.25
     *****************/
    public void insertAfter(Node a, Node b)
    {
        if (a != null && b != null)
        {
            if (last == a)
                last = b;
            b.next = a.next;
            a.next = b;
            N++;
        }
    }

    /*************************************************
     * Exercise 1.3.27
     * Type 'Item' must implement interface Comparable
     *************************************************/
    public Item max(Node node)
    {
        if (node == null) throw new RuntimeException("List is empty");
        return max(node, null);
    }

    public Item max(Node node, Item def)
    {
        if (node == null)
            return def;

        Item max = node.item;
        Node curr = node;

        while (curr.next != null)
        {
            curr = curr.next;
            if (((Comparable)max).compareTo(curr.item) < 0)
                max = curr.item;
        }

        return max;
    }

    /*************************************************
     * Exercise 1.3.28
     * (recursive variant of Exercise 1.3.27)
     * Type 'Item' must implement interface Comparable
     *************************************************/
    public Item maxRec(Node node, Item def)
    {
        if (node == null)
            return def;
        else
            return maxRec(node);
    }

    public Item maxRec(Node node)
    {
        if (node == null) throw new RuntimeException("List is empty");

        if (node.next == null)
            return node.item;
        else
        {
            Item maxTail = maxRec(node.next);
            return ((Comparable)node.item).compareTo(maxTail) > 0 ? node.item : maxTail;
        }
    }

    /*****************
     * Exercise 1.3.30
     *****************/
    public void reverse()
    {
        first = reverse(first);
        setLastAndN();
    }

    public Node reverse(Node node)
    {
        Node srcFirst = node,
                destFirst = null;
        while (srcFirst != null)
        {
            Node next = srcFirst.next;
            srcFirst.next = destFirst;
            destFirst = srcFirst;
            srcFirst = next;
        }

        return destFirst;
    }

    /***************************************
     * Recursive solution to Exercise 1.3.30
     ***************************************/
    public void reverseRec()
    {
        first = reverseRec(first);
        setLastAndN();
    }

    private Node reverseRec(Node node)
    {
        return reverseRec(node, null);
    }

    private Node reverseRec(Node srcFirst, Node destFirst)
    {
        if (srcFirst == null)
            return destFirst;
        else
        {
            Node next = srcFirst.next;
            srcFirst.next = destFirst;
            return reverseRec(next, srcFirst);
        }
    }

    public static void main(String[] args)
    {
    }
}
