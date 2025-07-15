/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */


var threeSumClosest = function(nums, target) {
  nums.sort((a, b) => a - b)
  let min_target;

  for (let i = 0; i < nums.length - 2; i ++) {
    if (i > 0 && nums[i] == nums[i - 1]) {
      continue;
    };

    let left = i + 1;
    let right = nums.length - 1;
    let total;

    while (left < right) {
      total = nums[i] + nums[left] + nums[right];

      if (!min_target && min_target !== 0) {
          min_target = total;
      } else {
        if (Math.abs(total - target) < Math.abs(min_target - target)) {
          min_target = total;
        };
      };

      if (total < target) {
        left += 1;
      } else {
        right -= 1;
      };
    };
  };
  
  return min_target;
};

console.log(threeSumClosest([-1,2,1,-4], 1));
console.log(threeSumClosest([-4,2,2,3,3,3], 0));
console.log(threeSumClosest([1,1,1,0], -100));