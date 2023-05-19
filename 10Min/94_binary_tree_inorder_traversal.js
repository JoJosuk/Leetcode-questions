/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var inorderTraversal = function(root) {
    let stack = []
    let values =[]
    let now = root
    while (now || stack.length!==0 ){
        while (now){
            stack.push(now);
            now = now.left   
        }
        now=stack.pop()
        values.push(now.val)
        now=now.right
    }
    return values
};
console.log(inorderTraversal({"val":1,"right":{"val":2,"left":{"val":3,"left":null,"right":null},"right":null},"left":null}))