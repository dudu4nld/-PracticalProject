package information_system;

import java.util.Scanner;

public class View {     //view视图层
	public static void main (String[] args) {
		Scanner input = new Scanner(System.in);
		Service ser = new Service();
		boolean flag = false;
			while(true) {
				System.out.println("========欢迎使用========");
				System.out.println("[1] 查询全部图书信息");
				System.out.println("[2] 模糊查找");
				System.out.println("[3] 删除图书信息");
				System.out.println("[4] 退出系统");
				System.out.println("请输入：");
				System.out.print("-->");
				int chioce=input.nextInt();
				switch(chioce) {
					case 1:
						ser.selectall();             //查看全部图书信息
						break;
					case 2:
						ser.select();
						break;
					case 3:
						ser.delete();                //删除图书信息
						break;
					case 4:
						System.out.println("欢迎下次登陆！");          //退出
						System.exit(0);
	                    break;
	                default:
	                	System.out.println("请输入正确的数字");          //输入错误，重新输入
				}
				System.out.println("======================================");
			}
		}
		
	}

