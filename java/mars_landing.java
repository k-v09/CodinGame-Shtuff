import java.util.Scanner;

class Player {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int surfaceN = sc.nextInt(); 
        sc.nextLine();
        for (int i = 0; i < surfaceN; i++) {
            sc.nextLine(); 
        }
        while (true) {
            try {
                String[] input = sc.nextLine().split(" ");
                int X = Integer.parseInt(input[0]);
                int Y = Integer.parseInt(input[1]);
                int hSpeed = Integer.parseInt(input[2]);
                int vSpeed = Integer.parseInt(input[3]);
                int fuel = Integer.parseInt(input[4]);
                int rotate = Integer.parseInt(input[5]);
                int power = Integer.parseInt(input[6]);
                int thrust_power = 0;
                int height_threshold = 300; 
                if (Y < height_threshold) {
                    thrust_power = 4; 
                } else {
                    if (vSpeed < -40) {
                        thrust_power = Math.min(4, fuel); 
                    } else if (vSpeed < -20) {
                        thrust_power = Math.min(3, fuel); 
                    } else if (vSpeed < 0) {
                        thrust_power = Math.min(2, fuel); 
                    } else {
                        thrust_power = 0; 
                    }
                }
                thrust_power = Math.max(0, Math.min(thrust_power, fuel));
                System.out.println("0 " + thrust_power);
            } catch (NumberFormatException | ArrayIndexOutOfBoundsException e) {
                System.out.println("Error: Invalid input");
            }
        }
    }
}
