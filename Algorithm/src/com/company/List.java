package com.company;

import edu.princeton.cs.algs4.StdOut;

import java.util.Iterator;
import java.util.NoSuchElementException;

/**
 * Created by hanhvn on 3/20/2017.
 */
public class List<Item> implements Iterable<Item>
{
    private int N;
    private Node first;
    private Node last;

    private class Node
    {
        private Node next;
        private Item item;
    }

    public List()
    {
        first = null;
        last = null;
        N = 0;
    }

    public List(Item[] a)
    {
        for (Item t : a)
            append(t);
    }

    public List(Iterable<Item> a)
    {
        for (Item t : a)
            append(t);
    }

    public boolean isEmpty() {return first == null;}

    public int size() {return N;}

    public Item first()
    {
        if (isEmpty())
            throw new RuntimeException("list is empty");
        return first.item;
    }

    public Item last()
    {
        if (isEmpty())
            throw new RuntimeException("list is empty");
        return last.item;
    }

    public Item removeFirst()
    {
        if (isEmpty()) throw new RuntimeException("list is empty");
        Item item = first.item;
        first = first.next;
        N--;
        if (isEmpty()) last = null; //avoid loitering
        return item;
    }

    public void append(Item item)
    {
        Node node = new Node();
        node.item = item;
        if (isEmpty()) {first = last = node;}
        else
        {
            last.next = node;
            last = node;
        }
        N++;
    }

    public void prepend(Item item)
    {
        Node node = new Node();
        node.item = item;
        if (isEmpty()) {first = last = node;}
        else
        {
            node.next = first;
            first = node;
        }
        N++;
    }

    public String toString()
    {
        StringBuilder s = new StringBuilder();
        for (Item item : this)
        {
            s.append(item + " ");
        }
        return s.toString();
    }

    public Iterator<Item> iterator() { return new ListIterator();}

    public class ListIterator implements Iterator<Item>
    {
        public Node current = first;

        @Override
        public boolean hasNext()
        {
            return current != null;
        }

        public void remove() { throw new UnsupportedOperationException();}

        @Override
        public Item next()
        {
            if (!hasNext()) throw new NoSuchElementException();
            Item item = current.item;
            current = current.next;
            return item;
        }
    }

    //exercise

    public Item removeLastItem()
    {
        if (isEmpty()) { throw new NoSuchElementException();}
        if (first == last) return removeFirst();
        Item item = last.item;

        Node prev = null;
        Node current = first;
        while (current.next != null)
        {
            prev = current;
            current = current.next;
        }
        prev.next = null;
        last = prev;
        N--;
        return item;
    }

    public Item deleteKthElem(int k)
    {
        if (k < 1)
            return null;
        int i = 1;
        Node prev = null, curr = first;
        while (curr != null && i < k)
        {
            prev = curr;
            curr = curr.next;
            i++;
        }
        if (curr != null)
        {
            if (prev == null) first = curr.next;
            else prev.next = curr.next;

            if (curr.next == null)
                last = prev;

            N--;
            return curr.item;
        }
        else return null;
    }

    public boolean find(String key)
    {
        Node curr = first;
        while (curr != null && !curr.item.equals(key))
            curr = curr.next;
        return curr != null;
    }

    public void removeAfter(Node node)
    {
        if (node != null && node.next != null)
        {
            if (node.next.next == null)
                last = node.next;
            node.next = node.next.next;
            N--;
        }
    }

    public void insertAfter(Node prev, Node front)
    {
        if (prev != null && front != null)
        {
            if (last == prev)
                last = front;
            front.next = prev.next;
            prev.next = front;
            N++;
        }
    }

    public void remove(String key)
    {
        Node curr = first;

        while (curr != null)
        {
            if (curr.item.equals(key))
            {
                if (curr == first)
                    removeFirst();
                else
                {
                    curr = curr.next;
                    if (curr.next == null)
                        last = curr;
                    if (curr == null)
                        last = null;
                    N--;
                }
                curr = curr.next;
            }
        }
    }

    public Item max(Node first)
    {
        if (first == null)
            return null;
        Node curr = first;
        Item max = curr.item;
        while (curr.next != null)
        {
            if (((Comparable) max).compareTo(curr.item) < 0)
                max = curr.item;
            curr = curr.next;
        }
        return max;
    }

    public Item maxRec(Node curr, Item max)
    {
        if (curr == null)
            return max;
        else
        {
            if (((Comparable) max).compareTo(curr.item) < 0)
                max = curr.item;
            return maxRec(curr.next, max);
        }
    }

    public Node reverse(Node first)
    {
        Node reverse = null, second;
        while (first != null)
        {
            second = first.next;
            first.next = reverse;
            reverse = first;
            first = second;
        }
        return reverse;
    }

    public Node reverseRec(Node first)
    {
        if (first == null)
            return null;
        if (first.next == null)
            return first;
        Node second = first.next;
        Node rest = reverseRec(second);
        second.next = first;
        first.next = null;
        return rest;
    }

    public static void showList(List list)
    {
        StdOut.println(list);
        if (!list.isEmpty())
            StdOut.printf("Size: %d, first: %s, last: %s\n", list.size(), list.first(), list.last());
        else
            StdOut.printf("Size: %d\n", list.size());
    }

    private static void testBaseMethods()
    {
        int[] a = { 2, 4, 6, 8, 10, 12 };

        List<Integer> lst = new List<Integer>();
        for (int i = 0; i < a.length; i++)
            lst.append(a[i]);
        showList(lst);

        lst = new List<Integer>();
        for (int i = 0; i < a.length; i++)
            lst.prepend(a[i]);
        showList(lst);

        StdOut.println("removeFirst: " + lst.removeFirst());
        showList(lst);
    }

    private static void testRemoveLast()
    {
        List<Integer> lst = new List<Integer>(new Integer[] { 6, 8, 10, 12 });
        showList(lst);

        while (!lst.isEmpty())
        {
            StdOut.println("removeLast: " + lst.removeLastItem());
            showList(lst);
        }
    }

    private static void testDelete()
    {
        List<Integer> lst = new List<Integer>(new Integer[] { 2, 4, 6, 8, 10, 12 });
        showList(lst);

        StdOut.printf("delete(%d): %s\n", 5, lst.deleteKthElem(5));
        showList(lst);

        StdOut.printf("delete(%d): %s\n", 1, lst.deleteKthElem(1));
        showList(lst);

        StdOut.printf("delete(%d): %s\n", 4, lst.deleteKthElem(4));
        showList(lst);

        StdOut.printf("delete(%d): %s\n", 8, lst.deleteKthElem(8));
        showList(lst);

        StdOut.printf("delete(%d): %s\n", 0, lst.deleteKthElem(0));
        showList(lst);

        while (!lst.isEmpty())
        {
            StdOut.printf("delete(%d): %s\n", 1, lst.deleteKthElem(1));
            showList(lst);
        }
    }

    public static void main(String[] args)
    {
        //testBaseMethods();
        //testRemoveLast();
        //testDelete();
    }
}
