# Quiz #1: Local Variable Value Tracer


Your submission must satisfy the following requirements:

* R1. Shall initialize your assignment repository from the link posted by the Slack channel.
* R2. Write your `LVVTracer.py` in the repository (based on the template given in this repository).
* R3. Test your `LVVTracer.py` by using `pytest`.
* R4. `LVVTracer` class should be defined in the `LVVTracer.py`
* R5. The above class is tested as:

```
from LVVTracer import LVVTracer

def test_lvv_sha256():
    with LVVTracer(target_func = "target_function") as traced:
        func1(args)

    ...  
	  func2(args2)
```

* R6. LVVTracer should count the number of value changes for each local variables in “target_function()”.
* R7. There is a member function called “getLVVmap()” in LVVTracer, which returns a dictionary of {“var1”: change_count1, “var2”: change_count2, …}.  LVVTracer should count the changes of local variables ONLY in “target_function()”.
* R8. "target_function" can be called multiple times. Everytime "target_function" returns, stored values for local variables should be cleared.



Note:

* N1. `pytest` (based on `test_lvv1.py`) is just for validating your program. The final grading will be made by other test cases.
* N2. Submissions via GitHub Classroom will only be accepted. Submissions via LMS are not accepted.
* N3. Late submissions are NOT allowed.
* N4. DO NOT change files in this repository except for `LVVTracer.py`. Adding new files are NOT allowed.
