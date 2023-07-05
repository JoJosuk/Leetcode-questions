fn main() {
    // Test case 1
    let coordinates1 = vec![
        vec![0, 0],
        vec![0, 1],
        vec![0, -1],
    ];
    println!("Test case 1: {}", Solution::check_straight_line(coordinates1));  // Expected output: true

    // Test case 2
    let coordinates2 = vec![
        vec![0, 0],
        vec![1, 1],
        vec![2, 2],
    ];
    println!("Test case 2: {}", Solution::check_straight_line(coordinates2));  // Expected output: true

    // Test case 3
    let coordinates3 = vec![
        vec![0, 0],
        vec![1, 2],
        vec![2, 3],
    ];
    println!("Test case 3: {}", Solution::check_straight_line(coordinates3));  // Expected output: false
}
impl Solution {
    pub fn check_straight_line(coordinates: Vec<Vec<i32>>) -> bool {
        let x0 = coordinates[0][0];
        let y0 = coordinates[0][1];
        let x1 = coordinates[1][0];
        let y1 = coordinates[1][1];
        
        if x0 == x1 {
            // All points have the same x-coordinate, indicating a vertical line
            for i in 2..coordinates.len() {
                if coordinates[i][0] != x0 {
                    return false;
                }
            }
            return true;
        }
        
        let slope = (y1 - y0) as f64 / (x1 - x0) as f64;
        
        for i in 2..coordinates.len() {
            let x = coordinates[i][0];
            let y = coordinates[i][1];
            if (y - y0) as f64 / (x - x0) as f64 != slope {
                return false;
            }
        }
        
        true
    }
}
