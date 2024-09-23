import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Player {

    public static List<int[]> findNeighbors(char[][] grid) {
        int height = grid.length;
        int width = grid[0].length;
        List<int[]> nodes = new ArrayList<>();

        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                if (grid[y][x] == '0') {
                    nodes.add(new int[]{x, y});
                }
            }
        }

        List<int[]> results = new ArrayList<>();

        for (int[] node : nodes) {
            int nodeX = node[0];
            int nodeY = node[1];

            int rightX = -1, rightY = -1;
            for (int x = nodeX + 1; x < width; x++) {
                if (grid[nodeY][x] == '0') {
                    rightX = x;
                    rightY = nodeY;
                    break;
                }
            }

            int bottomX = -1, bottomY = -1;
            for (int y = nodeY + 1; y < height; y++) {
                if (grid[y][nodeX] == '0') {
                    bottomX = nodeX;
                    bottomY = y;
                    break;
                }
            }

            results.add(new int[]{nodeX, nodeY, rightX, rightY, bottomX, bottomY});
        }

        return results;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int width = scanner.nextInt();
        int height = scanner.nextInt();
        scanner.nextLine(); 
        
        char[][] grid = new char[height][];
        for (int i = 0; i < height; i++) {
            grid[i] = scanner.nextLine().toCharArray();
        }
        
        List<int[]> neighbors = findNeighbors(grid);
        
        for (int[] node : neighbors) {
            System.out.printf("%d %d %d %d %d %d%n", node[0], node[1], node[2], node[3], node[4], node[5]);
        }

        scanner.close();
    }
}
