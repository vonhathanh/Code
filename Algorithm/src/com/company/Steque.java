package com.company;

import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

/**
 * Created by hanhvn on 3/25/2017.
 */
public class Steque<Item> extends Stack
{
    public void enqueue(Item item)
    {
        if (isEmpty()) push(item);
        else
        {
            Node curr = first;
            Node x = new Node();
            x.item = item;
            while (curr.next != null)
            {
                curr = curr.next;
            }
            curr.next = x;
        }
    }

    public static void main(String[] args)
    {
        Steque<Integer> steque = new Steque<>();
        for (int i = 0; i < 10; i++)
        {
            steque.enqueue(StdRandom.uniform(1,20));
            steque.push(StdRandom.uniform(10,20));
        }
        StdOut.print(steque + "\n");
        for (int i = 0; i < 20; i++)
        {
            StdOut.print(steque.pop() + "\n");
        }
    }
}
