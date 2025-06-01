use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
pub fn linear_search(nums: Vec<i32>, target: i32) -> bool {
    for index in 0..nums.len() {
        if nums[index] == target {
            return true
        }
    }
    false
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_linear_search_array() {
        let foo = vec![1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420];

        assert_eq!(linear_search(foo.clone(), 69), true);
        assert_eq!(linear_search(foo.clone(), 1336), false);
        assert_eq!(linear_search(foo.clone(), 69420), true);
        assert_eq!(linear_search(foo.clone(), 69421), false);
        assert_eq!(linear_search(foo.clone(), 1), true);
        assert_eq!(linear_search(foo.clone(), 0), false);
    }
}

#[pymodule]
fn linear_search_rs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(linear_search, m)?)?;
    Ok(())
}