public class JavaExample {
    public static void main(String args[]) {
      int a = 7;
      int b = 3;
      
      int temp = a;
      
      a = b;
      b = temp;

      System.out.println("a = " + a + " b = " + b);
    }
}