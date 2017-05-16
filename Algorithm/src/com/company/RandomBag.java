package com.company;

import edu.princeton.cs.algs4.Bag;
import edu.princeton.cs.algs4.StdOut;

import java.util.*;

/**
 * Created by hanhvn on 3/25/2017.
 */
public class RandomBag<Item> implements Iterable<Item>
{
    private int N;         // number of elements in bag
    private Node first;    // beginning of bag

    // helper linked list class
    private class Node {
        private Item item;
        private Node next;
    }

    /**
     * Create an empty stack.
     */
    public RandomBag() {
        first = null;
        N = 0;
    }

    /**
     * Is the BAG empty?
     */
    public boolean isEmpty() {
        return first == null;
    }

    /**
     * Return the number of items in the bag.
     */
    public int size() {
        return N;
    }

    /**
     * Add the item to the bag.
     */
    public void add(Item item) {
        Node oldfirst = first;
        first = new Node();
        first.item = item;
        first.next = oldfirst;
        N++;
    }


    /**
     * Return an iterator that iterates over the items in the bag.
     */
    public Iterator<Item> iterator()  {
        return new ListIterator();
    }

    // an iterator, doesn't implement remove() since it's optional
    private class ListIterator implements Iterator<Item> {
        private Node current = first;
        private int currentIndex = -1;
        private Item[] randomArrayOfItem = (Item[]) new Object[size()];

        public ListIterator()
        {
            currentIndex = 0;
            while (current != null)
            {
                randomArrayOfItem[currentIndex] = current.item;
                current = current.next;
                currentIndex++;
            }
            Collections.shuffle(Arrays.asList(randomArrayOfItem));
            currentIndex = 0;
        }
        public boolean hasNext()  { return currentIndex < size();                     }
        public void remove()      { throw new UnsupportedOperationException();  }

        public Item next() {
            if (!hasNext()) throw new NoSuchElementException();
            return randomArrayOfItem[currentIndex++];
        }
    }

    public static void main(String[] args)
    {
        RandomBag<Integer> randomBag = new RandomBag<>();
        for (int i = 0; i < 10; i++)
        {
            randomBag.add(i);
        }
        for(Integer i:randomBag)
            StdOut.print(i + ", ");
    }
}
