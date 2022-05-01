public class HelloWorld { 
    public static void main(String []args) {
       /* println() function to write Hello, World! */
       int[] age = new int[3];
        age[0] = 1;
        age[1] = 3;
        age[2] = 6;

        for (int i=0; i < 3; i++){
            System.out.println(age[i]);
        }
        System.out.println("Hello, World!");     
    }
 }