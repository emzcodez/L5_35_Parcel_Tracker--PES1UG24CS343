
# Lab 5: Static Code Analysis

| Issue | Type | Original finding | Fix applied |
|---|---|---|---|
| Missing module docstring | Code quality | Pylint C0114 | Added module docstring |
| Missing function docstrings | Code quality | Pylint C0116 | Added function docstrings |
| Non-snake_case names | Style | Pylint C0103 | Renamed functions, arguments and variables |
| Mutable default argument | Bug | Pylint W0102 | Changed the default to None and initialized the list inside the function |
| Broad exception handling | Code quality | Pylint W0718 | Replaced broad exception handling with explicit missing-parcel handling |
| Insecure temporary filename | Security | Bandit B306 | Replaced tempfile.mktemp() with NamedTemporaryFile |
| Shell injection risk | Security | Bandit B602 | Removed shell=True and replaced the helper with a safer approach before removing the unused helper |
| Weak OTP generation | Security | Bandit B311 | Replaced random with secrets |
| Spacing and blank-line errors | Style | Flake8 E225, E261, E231, E305 | Corrected spacing and blank lines |
| Subprocess-related warnings | Security | Bandit B404, B607, B603 | Removed the unused ping helper and its subprocess import |

## Final verification

- Initial Pylint score: 4.91/10
- Improved Pylint score before final cleanup: 10.00/10
- Initial Bandit findings: 1 high, 1 medium, 2 low
- Improved Bandit findings before final cleanup: 3 low
- Flake8: No violations after formatting
- Program execution: Successful
