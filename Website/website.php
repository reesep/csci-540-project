<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "mydb";
// Create connection
$conn = new mysqli($servername, $username, $password,$dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";

$c = "CREATE TABLE IF NOT EXISTS User (
    firstname VARCHAR(30),
    password VARCHAR(30)
)";
if ($conn->query($c) === TRUE) {
    echo "Table MyGuests created successfully";
}

$conn->close();
?>

<html>
<head>
    <title>Login Form</title>
    <link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body>

<h2>Login</h2><br>

<a href="Create.php"> Click here to create an account </a>

<br><br>

<div class="login">
    <form id="login" method="get" action="login.php">
        <label><b>User Name
            </b>
        </label>


        <input type="text" name="Uname" id="Uname" placeholder="Username">
        <br><br>
        <label><b>Password
            </b>
        </label>
        <input type="Password" name="Pass" id="Pass" placeholder="Password">
        <br><br>
        <input type="button" name="log" id="log" value="Log In Here">
        <br><br>


    </form>
</div>

</body>
</html>
