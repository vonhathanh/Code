package com.company;

import java.util.Iterator;
import java.util.NoSuchElementException;

/**
 * Created by hanhvn on 3/22/2017.
 */
public class DoublyLinkedList<Item> implements Iterable<Item>
{
    private int N;
    private DoubleNode first;
    private DoubleNode last;

    public DoublyLinkedList()
    {
        N = 0;
        first = null;
        last = null;
    }

    public DoublyLinkedList(Item[] a)
    {
        for (Item item : a)
            append(item);
    }

    public boolean isEmpty() { return first == null;}

    public void append(Item item)
    {
        DoubleNode node = new DoubleNode();
        node.item = item;
        if (first == null)
            first = last = node;
        else
        {
            node.prev = last;
            last.next = node;
            last = node;
        }
        N++;
    }

    public void prepend(Item item)
    {
        DoubleNode node = new DoubleNode();
        node.item = item;
        if (isEmpty())
        {
            first = node;
            last = node;
        }
        else
        {
            node.next = first;
            first.prev = node;
            first = node;
        }
        N++;
    }

    public Item removeFirst()
    {
        if (isEmpty()) throw new NoSuchElementException("list is empty");
        Item item = first.item;
        if (first.next != null) first.next.prev = null;
        first = first.next;
        N--;
        if (first == null) last = null; //avoid loitering
        return item;
    }

    public Item removeLast()
    {
        if (isEmpty()) throw new NoSuchElementException("list is empty");
        Item item = last.item;
        if (last.prev != null)
            last.prev.next = null;
        last = last.prev;
        N--;
        if (last == null) first = null; //avoid loitering
        return item;
    }

    public void insertBefore(DoubleNode node, Item item)
    {
        if (node == first)
            prepend(item);
        else
        {
            DoubleNode prev= node.prev;
            DoubleNode newNode = new DoubleNode();
            newNode.item = item;
            prev.next = newNode;
            newNode.prev = prev;
            newNode.next = node;
            node.prev = newNode;
            N++;
        }
    }

    public void insertAfter(DoubleNode node, Item item)
    {
        if (node == last)
            append(item);
        else
        {
            DoubleNode before = node.next;
            DoubleNode x = new DoubleNode();
            x.item = item;
            x.next = before;
            before.prev = x;
            node.next = x;
            x.prev = node;
            N++;
        }
    }

    @Override
    public Iterator<Item> iterator()
    {
        return new DoubleLinkedListIterator();
    }

    public class DoubleLinkedListIterator implements Iterator<Item>
    {
        DoubleNode curr = first;

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
            else throw new NoSuchElementException("list is empty");
        }

        @Override
        public void remove()
        {
            throw new UnsupportedOperationException();
        }
    }

    private class DoubleNode
    {
        private Item item;
        private DoubleNode next;
        private DoubleNode prev;
    }
}
