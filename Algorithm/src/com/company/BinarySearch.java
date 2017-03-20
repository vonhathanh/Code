package com.company;

import edu.princeton.cs.algs4.*;

import java.awt.*;
import java.util.Arrays;

/**
 * Created by hanhvn on 3/16/2017.
 */
public class BinarySearch
{

    public static int rank(int key, int[] a)
    {
        int lo = 0;
        int hi = a.length - 1;
        while (lo <= hi)
        {
            int mid = lo + (hi - lo) / 2;
            if (key < a[mid]) hi = mid - 1;
            else if (key > a[mid]) lo = mid + 1;
            else return mid;
        }
        return -1;
    }

    public static int lg(int n)
    {
        int temp = 1;
        int result = -1;
        do
        {
            result++;
            temp *= 2;
        } while (temp <= n);
        return result;
    }

    public static String exR1(int n)
    {
        if (n <= 0) return "";
        return exR1(n - 3) + n + exR1(n - 2) + n;
    }

    public static int mystery(int a, int b)
    {
        if (b == 0) return 0;
        if (b % 2 == 0) return mystery(a + a, b / 2);
        return mystery(a + a, b / 2) + a;
    }

    public static double binomial(int n, int k, double p)
    {
        if (n == 0 && k == 0)
            return 1.0;
        else if (n < 0 || k < 0)
            return 0.0;
        return (1.0 - p) * binomial(n - 1, k, p) + p * binomial(n - 1, k - 1, p);
    }

    public static double binomialDP(int n, int k, double p)
    {
        double[][] b = new double[n + 1][k + 1];
        b[0][0] = 1.0;
        for (int i = 1; i <= n; i++)
            b[i][0] = (1 - p) * b[i - 1][0];
        for (int i = 1; i <= k; i++)
            b[0][k] = 0.0;
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= k; j++)
                b[i][j] = (1 - p) * b[i - 1][j] + p * b[i - 1][j - 1];
        }
        return b[n][k];
    }

    public static void randomConnection()
    {
        int N = 4;
        double p = 0.2;
        double[] x = new double[N];
        double[] y = new double[N];
        StdDraw.setPenRadius(0.005);
        StdDraw.setPenColor(StdDraw.BLUE);
        StdDraw.setXscale(0, 100);
        StdDraw.setYscale(0, 100);
        StdDraw.circle(50, 50, 40);
        StdDraw.setPenColor(StdDraw.RED);
        double space = 6.28 / N;
        for (int i = 0; i < N; i++)
        {
            x[i] = 50 + Math.sin(space * i) * 40;
            y[i] = 50 + Math.cos(space * i) * 40;
            StdDraw.point(x[i], y[i]);
        }
        StdDraw.setPenColor(Color.DARK_GRAY);
        for (int i = 0; i < N - 1; i++)
        {
            for (int j = i + 1; j < N; j++)
            {
                double chance = StdRandom.uniform();
                if (chance < 0.5)
                    StdDraw.line(x[i],y[i],x[j],y[j]);
            }
        }

    }

    public static void main(String[] args)
    {
        randomConnection();
    }
}
