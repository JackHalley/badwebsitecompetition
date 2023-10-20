<?php
// Database connection parameters
$servername = "your_db_server";
$username = "your_db_username";
$password = "your_db_password";
$dbname = "your_db_name";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Handle form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["name"];
    $email = $_POST["email"];
    $website = $_POST["website"];
    $description = $_POST["description"];

    // Insert data into the database
    $sql = "INSERT INTO submissions (name, email, website, description) VALUES ('$name', '$email', '$website', '$description')";

    if ($conn->query($sql) === TRUE) {
        echo "Submission successful!";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}

// Close the database connection
$conn->close();
?>
