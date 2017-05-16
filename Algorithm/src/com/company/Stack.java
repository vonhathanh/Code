package com.company;

import edu.princeton.cs.algs4.StdOut;

import java.util.Iterator;
import java.util.NoSuchElementException;

/**
 * Created by hanhvn on 3/25/2017.
 */
public class Stack<Item> implements Iterable<Item>
{
    protected Node first;
    protected int N = 0;

    @Override
    public Iterator<Item> iterator()
    {
        return new StackIterator();
    }

    public class StackIterator implements Iterator<Item>
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

    protected class Node
    {
        protected Node next;
        protected Item item;
    }

    public boolean isEmpty() { return first == null; }

    public int size() { return N; }

    public void push(Item item)
    {
        Node oldFirst = first;
        first = new Node();
        first.item = item;
        first.next = oldFirst;
        N++;
    }

    public Item pop()
    {
        if (isEmpty()) throw new NoSuchElementException("list is empty");
        else
        {
            Item item = first.item;
            first = first.next;
            N--;
            return item;
        }
    }

    public Item top()
    {
        if (isEmpty()) throw new NoSuchElementException("list is empty");
        else return first.item;
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
        Stack<Integer> stack = new Stack<>();
        int[] array = {1, 2, 3, 4, 5};
        for (int t : array)
            stack.push(t);
        for (int i = 0; i <= 5; i++)
            StdOut.print(stack.pop());
    }
}
