# **Coverage Report**

### **Code Coverage Summary**
| Name               | Statements | Missed | Coverage |
|--------------------|------------|--------|----------|
| `functions.py`     | 106        | 78     | 26%      |
| `main.py`          | 8          | 8      | 0%       |
| `test_midi.py`     | 32         | 0      | 100%     |
| `test_note.py`     | 17         | 0      | 100%     |
| `user_interface.py`| 0          | 0      | 100%     |
| **Total**          | 163        | 86     | 47%      |

### **Remarks**
- **Current Coverage**: 47%
- **Planned Improvements**: Additional tests will be added to improve coverage and validate edge cases further.

---

## **Testing Overview**

### **What Has Been Tested and How?**
- **Unit Testing**: 
  - Most functions have been tested individually to verify their behavior and expected outputs.
  - Some functions do not have specific unit tests but are indirectly tested through higher-level tests.
- **End-to-End Testing**:
  - Full system functionality has been tested to ensure integration and correctness of workflows.

---

### **Test Input Types**
- **Usual Inputs**:
  - Regular inputs expected during normal usage.
- **Wrong Type**:
  - Inputs with incorrect types to validate error handling.
- **Invalid Values**:
  - Out-of-range values, e.g., `128` when the maximum allowable value is `127`.
- **Edge Cases**:
  - Scenarios that test the boundaries of input validity.

---

### **How to Repeat the Tests**
1. **Run Unit Tests**:
   poetry run pytest

2. **Run Coverage Report**:
   poetry run coverage report