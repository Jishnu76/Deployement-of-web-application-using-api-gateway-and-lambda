<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Contact Us</title>
<style>
  body {
    font-family: 'Roboto', Arial, sans-serif;
    line-height: 1.6;
    background-color: #f5f5f5;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
  header, footer {
    background-color: #333;
    color: white;
    text-align: center;
    padding: 10px 0;
    width: 100%;
  }
  .container {
    width: 80%;
    max-width: 600px;
    background: #ffffff;
    padding: 30px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    border-radius: 12px;
  }
  h1 {
    margin-top: 0;
    font-size: 36px;
    font-weight: 700;
    color: #333;
  }
  h2 {
    color: #333;
    border-bottom: 2px solid #333;
    padding-bottom: 10px;
    margin-bottom: 20px;
    font-size: 24px;
  }
  label {
    display: block;
    margin-bottom: 8px;
    color: #555;
    font-size: 16px;
  }
  input[type="text"],
  input[type="email"],
  textarea {
    width: 100%;
    padding: 12px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
    border-radius: 6px;
    box-sizing: border-box;
    font-size: 16px;
    transition: border-color 0.3s ease;
  }
  textarea {
    height: 150px;
    resize: vertical;
  }
  input[type="submit"] {
    background-color: #3498db;
    color: white;
    padding: 12px 20px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.3s ease;
  }
  input[type="submit"]:hover {
    background-color: #2980b9;
  }
  footer p {
    margin: 0;
  }
  .success-message {
    display: none;
    background-color: #dff0d8;
    border-color: #d0e9c6;
    color: #3c763d;
    padding: 20px;
    margin-top: 20px;
    border-radius: 6px;
    border: 1px solid #c8e1b2;
    text-align: center;
    font-size: 18px;
    font-weight: bold;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }
</style>
</head>
<body>

<header>
  <h1>Contact Us</h1>
</header>

<div class="container">
  <h2>Send us a message</h2>
  <form id="contactForm" action="#" method="post">
    <label for="fname">First Name</label>
    <input type="text" id="fname" name="firstname" placeholder="Your first name.." required>
    
    <label for="lname">Last Name</label>
    <input type="text" id="lname" name="lastname" placeholder="Your last name.." required>
    
    <label for="email">Email</label>
    <input type="email" id="email" name="email" placeholder="Your email.." required>
    
    <label for="message">Message</label>
    <textarea id="message" name="message" placeholder="Write your message.." required></textarea>
    
    <input type="submit" value="Submit">
  </form>

  <div id="successMessage" class="success-message">
    Thank you! Your message has been sent successfully.
  </div>
</div>

<footer>
  <p>&copy; AWS Project of Jishnu</p>
</footer>

<script>
  document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting

    // Display the success message
    document.getElementById('successMessage').style.display = 'block';

    // Optional: You can reset the form after submission
    this.reset();
  });
</script>

</body>
</html>
