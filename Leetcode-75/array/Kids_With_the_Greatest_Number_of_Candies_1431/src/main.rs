
pub struct Solution;

impl Solution {
    pub fn kids_with_candies(candies: Vec<i32>, extra_candies: i32) -> Vec<bool> {
        let max_value = *candies.iter().max().unwrap();
        let mut v: Vec<bool> = Vec::new();
        for element in candies {
            if element + extra_candies >= max_value {
                v.push(true);
            } else {
                v.push(false);
            }
        }
        v
    }
}

fn main() {
    let candies = vec![2, 3, 5, 1, 3];
    let extra_candies = 3;

    let result = Solution::kids_with_candies(candies.clone(), extra_candies);

    println!("{:?}", result);
}
