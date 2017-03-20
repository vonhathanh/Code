package com.company;

import edu.princeton.cs.algs4.StdDraw;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

/**
 * Created by hanhvn on 3/18/2017.
 */
public class MyPoint2D
{
    private double x;
    private double y;

    public MyPoint2D()
    {
    }

    public MyPoint2D(double x, double y)
    {
        this.x = x;
        this.y = y;
    }

    public double x()
    {
        return x;
    }

    public double y()
    {
        return y;
    }

    public double distanceTo(MyPoint2D p)
    {
        return distanceOf(this, p);
    }

    public static double distanceOf(MyPoint2D p1, MyPoint2D p2)
    {
        double dx = p1.x - p2.x;
        double dy = p1.y - p2.y;
        return Math.sqrt(dx * dx + dy * dy);
    }

    public static void main(String[] args)
    {
        StdDraw.setPenRadius(0.005);
        MyPoint2D[] points = new MyPoint2D[10];
        for (int i = 0; i < 10; i++)
        {
            double x = StdRandom.uniform();
            double y = StdRandom.uniform();
            points[i] = new MyPoint2D(x, y);
            StdDraw.point(points[i].x(), points[i].y());
        }
        double smallestDistance = Double.MAX_VALUE;
        for (int i = 0; i < 10; i++)
            for (int j = i + 1; j < 10; j++)
            {
                smallestDistance = Double.min(smallestDistance, MyPoint2D.distanceOf(points[i], points[j]));
            }
        StdOut.print(smallestDistance);
    }
}
