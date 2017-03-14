package com.company;

import java.util.Hashtable;

/**
 * Created by hanhvn on 3/12/2017.
 */
public class Node {

    int data;
    Node next = null;

    public Node(int d)
    {
        data = d;
    }

    void append(int d)
    {
        Node end = new Node(d);
        Node n = this;
        while (n.next != null) n = n.next;
        n.next = end;
    }

    Node delete(Node head, int d)
    {
        Node n = head;
        if (n.data == d)
            return head.next;
        while(n.next != null)
        {
            if (n.next.data == d)
            {
                n.next = n.next.next;
                return head;
            }
            n = n.next;
        }
        return null;
    }

    public static void deleteDupUsingHashTable(Node head)
    {
        Node previous = null;
        Hashtable table = new Hashtable();
        while (head != null)
        {
            if (table.containsKey(head.data)) previous.next = head.next;
            else
            {
                table.put(head.data,true);
                previous = head;
            }
            head = head.next;
        }
    }

    public static void deleteDup(Node head)
    {
        if ( head == null)
            return;
        Node previous = head;
        Node current = head.next;
        while (current != null)
        {
            Node runner = head;
            while (runner != current)
            {
                if (runner.data == current.data)
                {
                    Node tmp = current.next;
                    previous.next = tmp;
                    current = tmp;
                    break;
                }
                runner = runner.next;
            }
            if (runner == current)
            {
                previous = current;
                current = current.next;
            }
        }
    }

    public static Node findNthToLast(Node head, int n)
    {
        if (head == null || n < 1)
            return null;
        Node p1 = head;
        Node p2 = head;
        for (int i = 1; i < n; i++ )
        {
            if (p2 == null)
                return null;
            p2 = p2.next;
        }
        while (p2.next != null)
        {
            p2 = p2.next;
            p1 = p1.next;
        }
        return p1;
    }

    public static boolean deleteNodeInTheMiddle(Node n)
    {
        if (n == null || n.next == null)
            return false;
        n.data = n.next.data;
        n.next = n.next.next;
        return true;
    }

    public static Node addList(Node l1, Node l2, int carry)
    {
        if (l1 == null && l2 == null)
            return null;
        int value = carry;
        Node result = new Node(value);
        if (l1 != null)
            value += l1.data;
        if (l2 != null)
            value += l2.data;
        result.data = value % 10;
        Node more = addList(l1 == null ? null : l1.next, l2 == null ? null : l2.next, value > 10 ? 1: 0);
        if (more != null)
            result.append(more.data);
        return result;
    }
}
