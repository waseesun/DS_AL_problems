/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */

const removeElement = (nums, val) => {
  if (nums.length === 0) {
    return 0, [];
  };

  let k = 0;
  let left = 0;
  let right = nums.length - 1;

  while (left <= right){
    if (nums[left] === val && nums[right] === val){
      right -= 1;
    } else if (nums[left] === val){
      nums[left] = nums[right];
      k += 1;
      right -= 1;
      left  += 1;
    } else {
      k += 1;
      left += 1;
    };
  };

  return k, nums.slice(0, k);
};

console.log(removeElement([3,2,2,3], 3));
console.log(removeElement([3, 3], 3));
console.log(removeElement([4, 5], 5));
console.log(removeElement([0,1,2,2,3,0,4,2], 2));