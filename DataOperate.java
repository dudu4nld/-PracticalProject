package information_system;

import java.awt.List;
import java.sql.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Random;
import java.util.Scanner;

public class DataOperate {      //Model模型层 JDBC操作
	Connection conn=null;
	Scanner input = new Scanner(System.in);
	public DataOperate() { // 构造数据库操作对象，同时连接数据库并返回结果  
		try {
			Class.forName("com.mysql.jdbc.Driver");
			try {
				conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/bookdate", "root", "123456");
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				System.out.println("连接数据库失败");
				e.printStackTrace();
			}
				
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			System.out.println("驱动加载失败");
			e.printStackTrace();
		}
	}
	
	public void selectall(){      //查看全部图书信息操作
		
		      
    }
	public void select(String message){     

       
    }
	public void delete(String id){       //删除学生信息操作
		try {
            PreparedStatement preparedStatement=conn.prepareStatement("delete from bookdate where name =?");
            preparedStatement.setString(1,id);
            
        } catch (SQLException throwables) {
            System.out.println("删除失败！");
        }
    }
	

	public static boolean isNumber(String str){       //判断输入是否为数字
	    for (int i = str.length();--i>=0;){ 
	        if (!Character.isDigit(str.charAt(i))){
	           return false;
	        }
		}
	   return true;
	}
}
