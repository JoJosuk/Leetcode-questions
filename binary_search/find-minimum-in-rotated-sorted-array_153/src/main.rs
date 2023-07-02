struct Solution;

impl Solution {
    pub fn find_min(nums: Vec<i32>) -> i32 {
        let mut left = 0 as usize ;
        let mut right = nums.len() ;
        right -= 1;
        while left < right {
            let mid = (left + right) / 2 as i32 as usize;
            if nums[mid] > nums[right] {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        nums[left]
    }
}

fn main() {
    let nums = vec![4, 5, 6, 7, 0, 1, 2];
    let min_value = Solution::find_min(nums);

    println!("The minimum value in the vector is: {}", min_value);
}
