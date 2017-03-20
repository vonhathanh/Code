package com.company;

import edu.princeton.cs.algs4.Stack;
import edu.princeton.cs.algs4.StdOut;

/**
 * Created by hanhvn on 3/18/2017.
 */

/*************************************************************************
 *  Exercise 1.3.10
 *
 *  % java InfixToPostfix
 *  ( 1 + ( ( 2 + 3 ) * ( 4 * 5 ) ) )
 *  1 2 3 + 4 5 * * +
 *
 *  % java InfixToPostfix
 *  ( sqrt ( 1 + 2 ) )
 *  1 2 + sqrt
 *
 *************************************************************************/
public class InfixToPostfix
{
    private Stack<Character> ops;
    private Stack<Character> vals;
    private String expression;

    public InfixToPostfix(String s)
    {
        expression = s;
        ops = new Stack<>();
        vals = new Stack<>();
    }

    public void doConvert()
    {
        String s = "";
        for (int i = 0; i < expression.length(); i++)
        {
            if (expression.charAt(i) == '+'
                    || expression.charAt(i) == '-'
                    || expression.charAt(i) == '*'
                    || expression.charAt(i) == '/')
            {
                ops.push(expression.charAt(i));
            }
            else if (Character.isDigit(expression.charAt(i)))
                s += " " + expression.charAt(i);
            else if (expression.charAt(i) == ')')
            {
                if (!ops.isEmpty())
                s += " " + ops.pop();
            }
        }
        while (!ops.isEmpty())
            s += " " + ops.pop();
        StdOut.print(s);
    }

    public static void main(String[] args)
    {
        InfixToPostfix t = new InfixToPostfix("( 1 + ( ( 2 + 3 ) * ( 4 * 5 ) ) )");
        t.doConvert();
    }
}
