package com.company;

import edu.princeton.cs.algs4.Stack;
import edu.princeton.cs.algs4.StdOut;

/**
 * Created by hanhvn on 3/18/2017.
 */
public class Parentheses
{
    private Stack<Character> parenthesesStack;
    private String statement;

    public Parentheses(String s)
    {
        this.statement = s;
        parenthesesStack = new Stack<Character>();
    }

    public boolean isBalance()
    {
        int i = 0;
        while (i < statement.length())
        {
            if (statement.charAt(i) == '(' || statement.charAt(i) == '{' || statement.charAt(i) == '[')
                parenthesesStack.push(statement.charAt(i));
            else if (statement.charAt(i) == ')')
            {
                char c = parenthesesStack.pop();
                if (c != '(')
                    return false;
            } else if (statement.charAt(i) == '}')
            {
                char c = parenthesesStack.pop();
                if (c != '{')
                    return false;
            } else if (statement.charAt(i) == ']')
            {
                char c = parenthesesStack.pop();
                if (c != '[')
                    return false;
            }
            i++;
        }
        return parenthesesStack.isEmpty();
    }

    public static void main(String args[])
    {
        Parentheses p1 = new Parentheses("[()]{}{[()()]}");
        StdOut.print(p1.isBalance());
        Parentheses p2 = new Parentheses("[(])");
        StdOut.print(p2.isBalance());
    }
}
