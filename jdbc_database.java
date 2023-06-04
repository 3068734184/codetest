import java.sql.*;

public class DatabaseProgram {
    public static void main(String[] args) {
        // 数据库连接信息
        String url = "jdbc:mysql://localhost:3306/mydatabase";
        String username = "root";
        String password = "password";

        // 连接到数据库
        try (Connection connection = DriverManager.getConnection(url, username, password)) {
            System.out.println("成功连接到数据库！");

            // 创建Statement对象
            Statement statement = connection.createStatement();

            // 创建表
            String createTableQuery = "CREATE TABLE IF NOT EXISTS employees (id INT PRIMARY KEY, name VARCHAR(50))";
            statement.executeUpdate(createTableQuery);
            System.out.println("成功创建表！");

            // 插入数据
            String insertQuery = "INSERT INTO employees (id, name) VALUES (1, 'John Doe')";
            statement.executeUpdate(insertQuery);
            System.out.println("成功插入数据！");

            // 查询数据
            String selectQuery = "SELECT * FROM employees";
            ResultSet resultSet = statement.executeQuery(selectQuery);

            // 处理结果集
            while (resultSet.next()) {
                int id = resultSet.getInt("id");
                String name = resultSet.getString("name");
                System.out.println("ID: " + id + ", Name: " + name);
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
