/**
 * Definition for singly-linked list.
 */
/**
//  * @param {ListNode} list1
//  * @param {ListNode} list2
//  * @return {ListNode}
 */

class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  };
};

var mergeTwoLists = function(list1, list2) {
  if (list1 === null && list2 === null) {
    return null;
  }
  else if (list1 === null) {
    return list2;
  }
  else if (list2 === null) {
    return list1;
  }

  if (list1.val <= list2.val) {
    var head = new ListNode(list1.val);
    var current = head;
    list1 = list1.next;
  } else {
    var head = new ListNode(list2.val);
    var current = head;
    list2 = list2.next;
  }

  while (list1 !== null && list2 !== null) {
    if (list1.val <= list2.val) {
      current.next = new ListNode(list1.val);
      current = current.next;
      list1 = list1.next;
    }
    else {
      current.next = new ListNode(list2.val);
      current = current.next;
      list2 = list2.next;
    };
  };

  while (list1 !== null) {
    current.next = new ListNode(list1.val);
    current = current.next;
    list1 = list1.next;
  };

  while (list2 !== null) {
    current.next = new ListNode(list2.val);
    current = current.next;
    list2 = list2.next;
  };

  return head
};

const ls = (lst) => {
  if (lst.length === 0) {
    return null;
  }

  let head = new ListNode(lst[0]);
  let current = head;

  for (let i = 1; i < lst.length; i++) {
    current.next = new ListNode(lst[i]);
    current = current.next;
  };

  return head
};


console.log(mergeTwoLists(ls([1,2,4]), ls([1,3,4])))
console.log(mergeTwoLists(ls([]), ls([])))