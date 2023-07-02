struct Solution;

impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let mut flag = 0;
        let mut x = x;
        if x < 0 {
            flag = 1;
            x = -1 * x;
        }
        let mut a = x;
        let mut rem: i32;
        let mut res: i32 = 0;
        while a > 0 {
            rem = a % 10;
            res = res * 10 + rem;
            a = a / 10 as i32;
        }
        if flag == 1 {
            return res * -1;
        }
        res
    }
}

fn main() {
    let x = 123;
    println!("Input: {}", x);
    println!("Reversed: {}", Solution::reverse(x));

    let x = -123;
    println!("Input: {}", x);
    println!("Reversed: {}", Solution::reverse(x));

    let x = 120;
    println!("Input: {}", x);
    println!("Reversed: {}", Solution::reverse(x));
}
