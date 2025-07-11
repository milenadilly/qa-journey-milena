# Test Case 1: Successful login with valid credentials

**Preconditions:**  
- User has an active Netflix account  
- User is on the Netflix login page  

**Steps to execute:**  
1. Go to https://www.netflix.com/login  
2. Enter a valid email and password  
3. Click the "Sign In" button  

**Expected result:**  
- User is redirected to the Netflix homepage with full access to content  

---

# Test Case 2: Login with incorrect password

**Preconditions:**  
- User has a registered email  
- Password is incorrect  

**Steps to execute:**  
1. Go to https://www.netflix.com/login  
2. Enter a valid email and an incorrect password  
3. Click the "Sign In" button  

**Expected result:**  
- System displays an error message: "Incorrect password. Please try again or you can reset your password."  
- User remains on the login page  

---

# Test Case 3: Login with empty email and password fields

**Preconditions:**  
- User is on the Netflix login page  

**Steps to execute:**  
1. Leave both email and password fields empty  
2. Click the "Sign In" button  

**Expected result:**  
- System displays validation messages requesting both fields to be filled  
- Login is not processed  
