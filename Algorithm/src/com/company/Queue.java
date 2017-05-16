package com.company;

import edu.princeton.cs.algs4.StdOut;

import java.util.Iterator;
import java.util.NoSuchElementException;

/**
 * Created by hanhvn on 3/25/2017.
 */
public class Queue<Item> implements Iterable<Item>
{
    private Node first;
    private Node last;
    private int N = 0;

    private class Node
    {
        private Node next;
        private Item item;
    }

    public boolean isEmpty() { return first == null; }

    public int size() { return N; }

    @Override
    public Iterator<Item> iterator()
    {
        return new QueueIterator();
    }

    public class QueueIterator implements Iterator<Item>
    {
        Node curr = first;

        @Override
        public boolean hasNext()
        {
            return curr != null;
        }

        @Override
        public Item next()
        {
            if (hasNext())
            {
                Item item = curr.item;
                curr = curr.next;
                return item;
            }
            throw new NoSuchElementException();
        }

        @Override
        public void remove()
        {
            throw new UnsupportedOperationException();
        }
    }

    public void enqueue(Item item)
    {
        Node x = new Node();
        x.item = item;
        if (isEmpty()) { first = x; last = x; }
        else
        {
            last.next = x;
            last = x;
        }
        N++;
    }

    public Item deque()
    {
        if (isEmpty()) throw  new NoSuchElementException("list is empty");
        else
        {
            Item item = first.item;
            first = first.next;
            N--;
            if (first == null)
                last = null; //avoid loitering
            return item;
        }
    }

    public String toString()
    {
        StringBuilder sb = new StringBuilder();
        for (Item item : this)
            sb.append(item + " ");
        return sb.toString();
    }

    public static void main(String[] args)
    {
        Queue<String> queue = new Queue<>();
        for(int i = 1; i < 10; i++)
        {
            queue.enqueue(i + ", ");
        }
        StdOut.print(queue);
        for(int i = 1; i < 10; i++)
        {
            StdOut.print(queue.deque());
        }
        StdOut.print(queue.deque());
    }
}
