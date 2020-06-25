import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
public class Test3{

	public static void main(String[] args){
		String path = "hello";
		String arg = "";
		if(args != null && args.length > 1){
			path = args[0];
			arg = args[1];
		}

		String httpurl = "http://192.168.0.108:8080/"+path+"?"+arg;
	        System.out.println("result-----------"+
			doGet(httpurl)
		);	
	}

    public static String doGet(String httpurl) {
	System.out.println("httpurl-----------"+httpurl);
        HttpURLConnection connection = null;
        InputStream is = null;
        BufferedReader br = null;
        String result = null;// 返回结果字符串
        try {
            URL url = new URL(httpurl);
            connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.connect();
            if (connection.getResponseCode() == 200) {
                is = connection.getInputStream();
               	byte[] b = new byte[is.available()]; 
		is.read(b);
                result = new String(b); 
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (null != br) {
                try {
                    br.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if (null != is) {
                try {
                    is.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            connection.disconnect();
        }
        return result;
    }
}
