package com.company;

public class Main
{
    public static void main(String[] args)
    {
        Node head = new Node(1);
        Node tail = new Node(3);
        for(int i = 0; i < 3; i++)
        {
            head.append(i);
            tail.append(i);
        }
        Node result = Node.addList(head,tail,0);
        //System.out.print(Node.deleteNodeInTheMiddle(tmp));
        while (result != null)
        {
            System.out.print(result.data + ", ");
            result = result.next;
        }
    }
}
