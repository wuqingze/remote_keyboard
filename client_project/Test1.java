import java.time.format.DateTimeFormatter;
import java.time.LocalDateTime;
class Test1{

	public static void main(String[] args){
	    System.out.println(String.format("[%s] 接受消息:%s",
		    LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")),
		    "akdjfk")
	    );
	    return;
	}
}
