struct Solution;

impl Solution {
    pub fn can_place_flowers(flowerbed: Vec<i32>, n: i32) -> bool {
        let mut present = false;
        let mut n = n;

        for flower in flowerbed.iter() {
            if present {
                if flower == &1 {
                    return false;
                } else if flower == &0 {
                    present = false;
                }
            } else {
                if flower == &1 {
                    present = true;
                    n -= 1;
                }
            }
        }

        n <= 0
    }
}

fn main() {
    let flowerbed = vec![1, 0, 0, 0, 1];
    let n = 1;

    let can_place = Solution::can_place_flowers(flowerbed, n);

    if can_place {
        println!("It is possible to place {} flower(s) in the flowerbed.", n);
    } else {
        println!("It is not possible to place {} flower(s) in the flowerbed.", n);
    }
}
