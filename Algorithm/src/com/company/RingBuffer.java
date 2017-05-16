package com.company;

import edu.princeton.cs.algs4.StdOut;

import java.util.NoSuchElementException;

/**
 * Created by hanhvn on 3/25/2017.
 */
public class RingBuffer
{
    private int currSize;
    private int size;
    private int index;
    private int[] data;
    private boolean[] contains;

    public RingBuffer(int size)
    {
        assert size > 0;
        data = new int[size];
        contains = new boolean[size];
        this.index = 0;
        this.currSize = 0;
        this.size = size;
    }

    public boolean isEmpty() { return currSize == 0; }

    public boolean isFull() { return currSize == size; }

    public void deposit(int item)
    {
        if (isFull()) throw new RuntimeException("buffer is full");
        data[(index + currSize) % size] = item;
        currSize++;
    }

    public int widthdraw()
    {
        if (isEmpty()) throw new NoSuchElementException("buffer is empty");
        int item = data[index];
        index++;
        index = index % size;
        currSize--;
        return item;
    }

    public String toString()
    {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < size; i++)
        {
            sb.append(data[i] + " ");
        }
        return sb.toString();
    }

    public static void main(String[] args)
    {
        RingBuffer ringBuffer = new RingBuffer(5);
        for (int i = 0; i < 5; i++)
        {
            ringBuffer.deposit(i);
        }
        StdOut.print(ringBuffer + "\n");
        StdOut.print(ringBuffer.widthdraw() + "\n");
        StdOut.print(ringBuffer.widthdraw() + "\n");
        ringBuffer.deposit(5);
        ringBuffer.deposit(5);
        ringBuffer.deposit(5);
        StdOut.print(ringBuffer + "\n");
    }
}
