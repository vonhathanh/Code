package com.company;

import edu.princeton.cs.algs4.Stack;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

/**
 * Created by hanhvn on 3/18/2017.
 */

/*************************************************************************
 *
 *  % java Ex_1_3_09
 *  1 + 2 ) * 3 - 4 ) * 5 - 6 ) ) )
 *  ( ( 1 + 2 ) * ( ( 3 - 4 ) * ( 5 - 6 ) ) )
 *
 *  % java Ex_1_3_09
 *  sqrt 1 + 2 ) )
 *  ( sqrt ( 1 + 2 ) )
 *
 *************************************************************************/
public class InsertLeftParenthese
{

    public static void main(String[] args)
    {
        Stack<String> ops = new Stack<>();
        Stack<String> vals = new Stack<>();
        while (!StdIn.isEmpty())
        {
            String temp = StdIn.readString();
            if (temp.equals("(")) ;
            else if (temp.equals("+") || temp.equals("-") || temp.equals("*") || temp.equals("/") || temp.equals("sqrt"))
            {
                ops.push(temp);
            }
            else if (temp.equals(")"))
            {
                String op = ops.pop();
                String v = vals.pop();
                if (op.equals("sqrt"))
                    v = String.format("( %s %s )", op, v);
                else v = String.format("( %s %s %s )", vals.pop(), op, v);
                vals.push(v);
            }
            else vals.push(temp);
        }
        StdOut.print(vals.pop());
    }
}
