using System;
using System.Collections.Generic;

class Program
{
    static List<(int, int, int, int, int, int)> FindNeighbors(char[][] grid)
    {
        int height = grid.Length;
        int width = grid[0].Length;
        var nodes = new List<(int, int)>();

        for (int y = 0; y < height; y++)
        {
            for (int x = 0; x < width; x++)
            {
                if (grid[y][x] == '0')
                {
                    nodes.Add((x, y));
                }
            }
        }

        var results = new List<(int, int, int, int, int, int)>();

        foreach (var (node_x, node_y) in nodes)
        {
            int right_x = -1, right_y = -1;
            for (int x = node_x + 1; x < width; x++)
            {
                if (grid[node_y][x] == '0')
                {
                    right_x = x;
                    right_y = node_y;
                    break;
                }
            }

            int bottom_x = -1, bottom_y = -1;
            for (int y = node_y + 1; y < height; y++)
            {
                if (grid[y][node_x] == '0')
                {
                    bottom_x = node_x;
                    bottom_y = y;
                    break;
                }
            }

            results.Add((node_x, node_y, right_x, right_y, bottom_x, bottom_y));
        }

        return results;
    }

    static void Main()
    {
        
        int width = int.Parse(Console.ReadLine());
        int height = int.Parse(Console.ReadLine());

        var grid = new char[height][];
        for (int i = 0; i < height; i++)
        {
            grid[i] = Console.ReadLine().ToCharArray();
        }

        var neighbors = FindNeighbors(grid);

        foreach (var node in neighbors)
        {
            Console.WriteLine($"{node.Item1} {node.Item2} {node.Item3} {node.Item4} {node.Item5} {node.Item6}");
        }
    }
}
