fn main() {
    let column_title = String::from("ABC");
    let result = Solution::title_to_number(column_title);
    println!("Result: {}", result);
}

struct Solution;
impl Solution {
    pub fn title_to_number(column_title: String) -> i32 {
        let mut res=0;
        for ch in column_title.chars(){
            let chnum = ch as i32;
            res=res*26+(chnum-64)
        }
        res
    }
}