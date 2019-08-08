public static LinkedListNode intersect(LinkedListNode a, LinkedListNode b){

    if (a == null || b == null) return null;

    LinkedListNode a_head = a;
    LinkedListNode b_head = b;
    int a_len, b_len = 1;

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
    if (a_len == 1 or b_len == 1) return a_head;

    // improved
    LinkedListNode shorter = a_len < b_len ? a : b;
    LinkedListNode longer = b_len < a_len ? b : a;
    int diff = Math.abs(a_len - b_len);

    while(k > 0 && longer != null){
        longer = longer.next;
        k--;
    }

    // there's intersection
    while(shorter != longer){
        shorter = shorter.next;
        longer = longer.next;
    }

    return shorter;
}