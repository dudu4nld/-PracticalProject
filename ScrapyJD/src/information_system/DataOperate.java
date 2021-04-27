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
		String sql="select * from bookdate";
		try {
			Statement statement = conn.createStatement();
			ResultSet resultSet=null;
	        resultSet=statement.executeQuery(sql);
        	System.out.println("图书名称"+"\t"+"图书价格"+"\t"+"图书细节");
	        while (resultSet.next())
            {	
	        	System.out.print(resultSet.getString("name")+"\t");
	        	System.out.print(resultSet.getString("price")+"\t");
	        	System.out.print(resultSet.getString("detail")+"\t");
	        	System.out.println();
            }
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		      
    }
	public void select(String message){     

        try {
        	Statement stmt=conn.createStatement();//创建一个Statement对象
        	String sql="select * from bookdate where name like '%"+message+"%' ";
        	ResultSet rs=null;
        	rs=stmt.executeQuery(sql);
        	while (rs.next())
            {	
	        	System.out.print(rs.getString("name")+"\t");
	        	System.out.print(rs.getString("price")+"\t");
	        	System.out.print(rs.getString("detail")+"\t");
	        	System.out.println();
            }
        } catch (SQLException e) {
        	e.printStackTrace();
        }
    }
	public void delete(String id){       //删除学生信息操作
		try {
            PreparedStatement preparedStatement=conn.prepareStatement("delete from bookdate where name =?");
            preparedStatement.setString(1,id);
            int num=preparedStatement.executeUpdate();
            if(num!=0){
                System.out.println("删除成功！");
            }
            else System.out.println("未找到ID，删除失败！");
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
