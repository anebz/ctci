public static LinkedListNode intersect(LinkedListNode a, LinkedListNode b){

    if (a == null || b == null) return null;

    LinkedListNode a_head = a;
    LinkedListNode b_head = b;
    int a_len = 1;
    int b_len = 1;

    // iterate through A
    while (a_head.next != null){
        a_head = a_head.next;
        a_len += 1;
    }

    // iterate through B
    while (b_head.next != null){
        b_head = b_head.next;
        b_len += 1;
    }

    // last node inequal, return null
    if (a_head != b_head) return null; // changed from before

    // compare lengths, adjust node
    if (a_len == 1 || b_len == 1) return a_head;

    // improved
    LinkedListNode shorter = a_len < b_len ? a : b;
    LinkedListNode longer = b_len < a_len ? b : a;
    int diff = Math.abs(a_len - b_len);

    while(diff > 0 && longer != null){
        longer = longer.next;
        diff--;
    }

    // there's intersection
    while(shorter != longer){
        shorter = shorter.next;
        longer = longer.next;
    }

    return shorter;
}

// https://stackoverflow.com/questions/1594061/check-if-two-linked-lists-merge-if-so-where/14956113#14956113
static int FindMergeNode(LinkedListNode headA, LinkedListNode headB) {
    LinkedListNode currentA = headA;
    LinkedListNode currentB = headB;

    // Do till the two nodes are the same
    while (currentA != currentB) {
        // If you reached the end of one list start at the beginning of the other one
        // currentA
        if (currentA.next == null) {
            currentA = headB;
        } else {
            currentA = currentA.next;
        }
        // currentB
        if (currentB.next == null) {
            currentB = headA;
        } else {
            currentB = currentB.next;
        }
    }
    return currentB.data;
}