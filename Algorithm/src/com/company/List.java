package com.company;

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

    public void removeAll(String key)
    {
        Node curr = first, prev = null;

        while (curr != null)
        {
            if (curr.item.equals(key))
            {
                if (curr == first)
                    removeFirst();
                else if (curr == last)
                    removeLastItem();
                else
                    prev.next = curr.next;
                N--;
                prev = curr;
                curr = curr.next;
            }
        }
    }
}
