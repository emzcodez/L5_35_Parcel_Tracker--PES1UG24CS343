# L5_35_Parcel_Tracker--PES1UG24CS343
## Development and Verification

Activate the virtual environment before running the tools.

```bash
python -m pylint parcel_tracker.py
python -m bandit -r parcel_tracker.py
python -m flake8 parcel_tracker.py
python -m unittest discover -s tests -v
```

### Static Analysis Reports

- `reports/before/` contains the initial analysis reports.
- `reports/after/` contains the reports generated after the fixes.

The parcel tracker uses Python's `secrets` module for OTP generation and avoids shell-based subprocess execution.
