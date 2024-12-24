/**
 * @param {number[]} nums
 * @return {number}
 */


const removeDuplicates = (nums) =>  {
    if (nums.length === 0) {
      return 0, [];
    };

    let k = 1;
    let curr_item = 0;
    for (let i=1; i < nums.length; i++){
      if (nums[i] == nums[curr_item]) {
      } else {
        nums[curr_item + 1] = nums[i];
        k += 1;
        curr_item += 1;
      };
    };

    return k, nums.slice(0, curr_item + 1);
};

console.log(removeDuplicates([1, 1, 2]));
console.log(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]));