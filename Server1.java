import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;

public class Server1{
    public static void main(String[] args){ 
        System.out.println("hreljr");
	try{
		ServerSocket serverSocket = (args == null || args.length<1)?new ServerSocket(9999):new ServerSocket(Integer.parseInt(args[0]));
		Socket socket= serverSocket.accept();
		BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
		String str =bufferedReader.readLine();
		System.out.println(str);
	} catch(Exception e){ e.printStackTrace();}
    }
}

