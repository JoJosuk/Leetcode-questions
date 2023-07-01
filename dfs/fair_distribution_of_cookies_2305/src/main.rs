//not an optimized solution as it uses dfs idealy we have to use bitmask with dp
fn main() {
    let cookies = vec![8, 15, 10, 20, 8];
    let k = 2;

    let min_unfairness = Solution::distribute_cookies(cookies, k);

    println!("Minimum Unfairness: {}", min_unfairness);
}
struct Solution;


impl Solution {
    pub fn distribute_cookies(cookies: Vec<i32>, k: i32) -> i32 {
        let mut a = vec![0;k as usize];
        println!("{:?}",a);
        Self::dfs(&cookies, &mut a,0)
    }
    fn dfs(cookies: &[i32],a:&mut [i32],i: usize)->i32{
        if i==cookies.len(){
            return *a.iter().max().unwrap();
        }
        let mut res = i32::MAX;
        for j in 0..a.len(){
            a[j]+=cookies[i];
            println!("{:?}",a);
            res = res.min(Self::dfs(cookies,a,i+1));
            a[j]-=cookies[i];
        }
        res

    }
}