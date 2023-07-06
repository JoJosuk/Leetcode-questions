struct Solution;

impl Solution {
    pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
        let arraylength = nums.len();
        let mut i: usize = 0;
        let mut j: usize = 0;
        let mut sum: i32 = 0;
        let mut min = i32::MAX;
        
        while j < arraylength {
            while sum < target && j < arraylength {
                sum += nums[j];
                j += 1;
            }
            
            while sum >= target {
                let subarray_length = (j - i) as i32;
                if subarray_length < min {
                    min = subarray_length;
                }
                
                sum -= nums[i];
                i += 1;
            }
        }
        
        if min == i32::MAX {
            return 0;
        }
        
        min
    }
}

fn main() {
    // Test case 1
    let target1 = 7;
    let nums1 = vec![2, 3, 1, 2, 4, 3];
    let result1 = Solution::min_sub_array_len(target1, nums1);
    println!("Result 1: {}", result1);  // Expected output: 2
    
    // Test case 2
    let target2 = 11;
    let nums2 = vec![1, 2, 3, 4, 5];
    let result2 = Solution::min_sub_array_len(target2, nums2);
    println!("Result 2: {}", result2);  // Expected output: 3
    
    // Test case 3
    let target3 = 100;
    let nums3 = vec![10, 20, 30];
    let result3 = Solution::min_sub_array_len(target3, nums3);
    println!("Result 3: {}", result3);  // Expected output: 0
}
