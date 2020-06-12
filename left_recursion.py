import java.util.*;
import java.io.*;

public class lefrec {
	
	static String input_file ="C:\\Users\\Varsha\\Desktop\\input1.txt";
	
	public static void main(String[] args) throws Exception{
		String s,s0,left,right;
		BufferedReader br0 = new BufferedReader(new InputStreamReader(new FileInputStream(input_file)));	
		BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(input_file)));		
		//BufferedReader br1 = new BufferedReader(new InputStreamReader(new FileInputStream(input_file)));
		
		System.out.println("The input grammar is:");
		
		while((s0=br0.readLine())!=null){
			System.out.println(s0);
		}
		
		while((s=br.readLine())!=null){
			System.out.println("\n" + s);
			StringTokenizer st = new StringTokenizer(s, " ->", false);
			left = st.nextToken();
			right = st.nextToken();
			
			/*while((s1=br1.readLine())!=null){
				StringTokenizer st1 = new StringTokenizer(s1, " ->", false);
				left1 = st1.nextToken();
				right1 = st1.nextToken();
				
				if(right.charAt(0)==left1.charAt(0)){
					//right = right1 + right.substring(1);
					
					//System.out.println(left+"->"+right);
				    
				}
			}*/
				
				leftrec(left,right);
			}
		}
	
	public static void leftrec(String left,String right) throws Exception {
		
		StringTokenizer st=new StringTokenizer(right,"|",false);
		String arr[] = new String[st.countTokens()];
		for(int i=0;i<arr.length;i++){
			arr[i]=st.nextToken();
			//System.out.println(arr[i]);
		}  
		
		for(int i=0;i<arr.length;i++){
			if(left.charAt(0) == arr[i].charAt(0)){
				System.out.println("\nGrammar is left recursive");								
				System.out.println(left + "\'" + "->" + arr[i].substring(1) + left + "\'");	
				System.out.println(left + "\'" + "->" + null);				
				while(i!=(arr.length-1)){
					System.out.println(left + "->" + arr[++i] + left + "\'");
				}
			}	
		}
	}
}
