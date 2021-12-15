<?php

echo "aw beans";

$conn = mysqli_connect("localhost", "root", "", "mydb");

// Check connection
if($conn === false){
    die("ERROR: Could not connect. "
        . mysqli_connect_error());
}

// Taking all 5 values from the form data(input)
$username =  $_REQUEST['Uname'];
$password = $_REQUEST['Pass'];


// Performing insert query execution
// here our table name is college

$hashed = md5($password);

$sql = "INSERT INTO user (firstname,password) VALUES ('$username','$hashed')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

    $conn->close();

?>