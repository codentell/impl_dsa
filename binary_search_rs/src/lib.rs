use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use numpy::PyReadonlyArray1;

/// A binary search function that returns the index or -1 if not found.
#[pyfunction]
pub fn binary_search(nums: PyReadonlyArray1<i32>, target: i32) -> i32 {
    let nums = nums.as_slice().unwrap();
    if nums.is_empty() {
        return -1;
    }

    let mut start = 0;
    let mut end = nums.len() - 1;

    while start <= end {
        let mid = (start + end) / 2;

        if nums[mid] == target {
            return mid as i32;
        } else if nums[mid] < target {
            start = mid + 1;
        } else {
            if mid == 0 { break; }
            end = mid - 1;
        }
    }
    -1
}

#[pymodule]
fn binary_search_rs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(binary_search, m)?)?;
    Ok(())
}
