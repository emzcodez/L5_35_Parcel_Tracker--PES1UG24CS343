
# Lab 5: Reflection

### 1. What is static code analysis?

Static code analysis examines source code without executing it to identify possible bugs, security vulnerabilities and style violations.

### 2. What are the differences between Pylint, Bandit and Flake8?

Pylint checks general code quality and programming practices. Bandit identifies potentially insecure coding patterns. Flake8 checks Python style and formatting rules.

### 3. What issues did you identify and fix?

I corrected naming and documentation issues, replaced a mutable default argument, improved exception handling, removed insecure temporary-file creation, avoided shell-based command execution, and switched OTP generation to the secrets module. I also corrected formatting violations.

### 4. What did you learn?

I learned that code can run correctly while still containing security and maintainability problems. Static analysis tools complement one another, and rerunning them after changes helps verify the improvements.
