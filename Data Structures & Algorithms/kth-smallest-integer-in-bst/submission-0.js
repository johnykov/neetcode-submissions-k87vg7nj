/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @param {number} k
     * @return {number}
     */
    // let count = 0;
    kthSmallest(root, k) {
        let count = 0;
        let result = 0;
    function inorder(root) {
        if (!root) return;
        if (root.left) inorder(root.left);
        count++;
        if (count == k) result = root.val
        if (root.right) inorder(root.right);
    }
    inorder(root);
    return result;
    }
}
