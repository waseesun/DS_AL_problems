/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */

class ListNode {
  constructor(val, next) {
    this.val = (val===undefined ? null : val);
    this.next = (next===undefined ? null : next);
  };
};

const recremoveNthfromEnd = (head, current, n) => {
  if (current === null) {
    return 0;
  };

  let val = recremoveNthfromEnd(head, current.next, n);

  if (typeof val === "number") {
    if (current === head && val == n - 1) {
      current = current.next;
      return current;
    } else if (val === n) {
      current.next = current.next.next
      return current
    } else {
      return val + 1
    };
  } else {
    return current
  };
}

const removeNthFromEnd = (head, n) => {
  let current = head;
  head = recremoveNthfromEnd(head, current, n);
  return head;
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

// let lst = ls([1, 2, 3, 4, 5])
let lst = ls([1, 2])
console.log(removeNthFromEnd(lst, 2))
// console.log(removeNthFromEnd(lst, 1))