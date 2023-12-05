# requires_nas
Make sure your NAS-requiring software has a connection to it

# Usage
To use, import the `requires_nas` or `requires_nas_loop` function and plug into your code before it tries to reach the NAS 

#### Example
Before:
```python
import file_processing
file = "NAS/files/to_process/1.tiff"
file_processing(file)
```
```terminal
>>> Error: No such file or directory "NAS/files/to_process/1.tiff" 
```

After
```python
from requires_nas import requires_nas_loop # import the function
import file_processing
file = "NAS/files/to_process/1.tiff"
requires_nas_loop()                        # call it here
file_processing(file)
```
```terminal
>>> Waiting for NAS...
>>> NAS Mounted!
>>> File processed.
```