import java.rmi.RemoteException;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.io.InputStream;
import java.io.OutputStream;

public class KeyboardServiceImpl implements KeyboardService{

    private InputStream inputStream;

    private OutputStream outputStream;

    public KeyboardServiceImpl(InputStream inputStream, OutputStream outputStream){
	this.inputStream = inputStream;
	this.outputStream = outputStream;
    }

    public String type(String key) throws RemoteException {
	String stackMsg = String.format("[%s] $s", 
		LocalDate.now().format(DateTimeFormatter.ofPattern("yyyyMMdd HH:mm:ss")),
		key);
	String result = null;
	try{
	    outputStream.write(key.getBytes());
	    byte[] b = new byte[32];
	    inputStream.read(b);
	    result = new String(b);
	}catch(Exception e){
	    e.printStackTrace();
	    throw new RemoteException("输入失败,"+stackMsg);
	}
	return result;
    }
}
