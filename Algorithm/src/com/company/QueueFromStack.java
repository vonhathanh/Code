package com.company;

import edu.princeton.cs.algs4.StdOut;

/**
 * Created by hanhvn on 3/25/2017.
 */
public class QueueFromStack<E>
{
    private Stack<E> inbox = new Stack<E>();
    private Stack<E> outbox = new Stack<E>();

    public void queue(E item)
    {
        inbox.push(item);
    }

    public E dequeue()
    {
        if (outbox.isEmpty())
        {
            while (!inbox.isEmpty())
            {
                outbox.push(inbox.pop());
            }
        }
        return outbox.pop();
    }

    public static void main(String[] args)
    {
        QueueFromStack<Integer> q = new QueueFromStack<>();
        for (int i = 0; i < 10; i++)
        {
            q.queue(i);
        }
        StdOut.print(q.dequeue()+ "\n");
        StdOut.print(q.dequeue()+ "\n");
        q.queue(5);
        StdOut.print(q.dequeue()+ "\n");
    }
}
