package information_system;

import java.util.HashMap;
import java.util.Scanner;

public class Service {       //菜单类 controller控制层
	Scanner input = new Scanner(System.in);
	DataOperate data_operate = new DataOperate();
	public Service() {          //无参构造方法
    }
	public void selectall() { //调用数据库查询全部图书信息操作
		data_operate.selectall();
	}
	
	public void select() { //调用数据库模糊查询
		System.out.println("请输入需要查询的信息:  ");
        String message=input.nextLine();
        data_operate.select(message);
	}
	public void delete() { //调用数据库删除操作
		System.out.println("请输入删除的图书ID：");
        String id=input.nextLine();
        data_operate.delete(id);
	}
	



}