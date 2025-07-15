/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */

const sum = (a, b) => a - b; 

var fourSum = function(nums, target) {
  nums.sort(sum)
  let lst = [];

  for (let i = 0; i < nums.length - 3; i ++) {
    if (i > 0 && nums[i] == nums[i - 1]) {
      continue;
    };

    let left = i + 1;
    let right = nums.length - 1;
    let left_mid = left + 1;
    let right_mid = right - 1;

    while (left_mid < right) {
      let total1, total2;
      total1 = nums[i] + nums[left] + nums[left_mid] + nums[right];
      total2 = nums[i] + nums[left] + nums[right_mid] + nums[right];
      item1 = [nums[i], nums[left], nums[left_mid], nums[right]];
      item2 = [nums[i], nums[left], nums[right_mid], nums[right]];

      if (total1 == target || total2 == target) {
        if (lst.length == 0) {
          if (item1.sort(sum).toString() === item2.sort(sum).toString()) {
            lst.push([nums[i], nums[left], nums[left_mid], nums[right]]); 
          } else {
            if (total1 == target) {
              lst.push([nums[i], nums[left], nums[left_mid], nums[right]]);
            };
            if (total2 == target) {
              lst.push([nums[i], nums[left], nums[right_mid], nums[right]]);
            };
          }
        } else {
          if (lst[lst.length - 1].sort(sum).toString() !== item1.sort(sum).toString() && total1 == target) {
            lst.push(item1);
          };
          if (lst[lst.length - 1].sort(sum).toString() !== item2.sort(sum).toString() && total2 == target) {
            lst.push(item2);
          };
        };
      };
      
      if (left_mid < right_mid) {
        left_mid += 1;
        right_mid -= 1;
      } else {
        if (total1 < target && total2 < target) {
          left += 1;
        } else {
          right -= 1;
        };
        left_mid = left + 1;
        right_mid = right - 1;
      };
    };
  };
  
  return lst;
};

console.log(fourSum([1, 0, -1, 0, -2, 2], 0));
console.log(fourSum([2, 2, 2, 2, 2], 8));
console.log(fourSum([-3,-2,-1,0,0,1,2,3], 0));
console.log(fourSum([-3,-1,0,2,4,5], 0));