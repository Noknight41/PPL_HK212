public class HelloWorld { 
    public static void main(String []args) {
       /* println() function to write Hello, World! */
        int n = 10;
        int sum = 0;
        for(int i = 1; i < n; i++){
            if(i % n == 0){
                continue;
            }
            else sum += i;
        }
        System.out.println("Hello, World!");     
    }
 }