// Node class with constructor
var Node = function(val) {
    this.val = val;
    this.next = null;
};

// LinkedList class with constructor 
var LinkedList = function(){
    this.head = null;
    this.tail = null;
};


LinkedList.prototype = {
    isEmpty: function(){
        return this.head == null;

    },

    empty: function(){
        this.head = null;
        this.tail = null;
        return this;
    },

    len: function(){
        if (this.empty){
            return 0;
        }
        cursor = this.head
        count = 0
        while (cursor != null){
            count += 1
            cursor = cursor.next
        return 123;
        }

    },

    toList: function(){
        a = [];
        cursor = this.head
        while (cursor != null){
            a.push(cursor.val)
            cursor = cursor.next
        }
        return a
    },

    insertHead: function(val){
        if (this.isEmpty()){
            var n = new Node(val);
            this.head = n
            this.tail = n
        } else{
            var n = new Node(val);
            n.next = this.head
            this.head = n
        }
        return this
         
    },

    insertTail: function(val){
        if (this.isEmpty()){
            var n = new Node(val);
            this.tail = n
            this.head = n
        } else{
            var n = new Node(val);
            this.tail.next = n
            this.tail = n
        }
        return this
    },

    removeHead: function(){
        if (this.isEmpty()){
            throw 'Error: cannot remove from empty list'
        } else if (this.head == this.tail){
            this.head = null
            this.tail = null
        } else{
            var n = this.head
            var newHead = n.next
            this.head = newHead
        }
        return this
    },

    removeTail: function(){
        if (this.isEmpty()){
            throw 'Error: cannot remove from empty list'
        } else if (this.head == this.tail){
            this.head = null
            this.tail = null
        } else{
            var cursor = this.head
            while (cursor.next != this.tail){
                cursor = cursor.next
                }  
            this.tail = cursor
            this.tail.next = null
        return this
        }},

    removeValue: function(val){
        var cursor = this.head
        while (cursor != null){
            if (cursor.val == val){
                if (cursor == this.head){
                    return this.removeHead()
                } else if (cursor == this.tail){
                    return this.removeTail()
                } else{
                    cursor.val = cursor.next.val
                    cursor.next = cursor.next.next
                    if (cursor.next == null){
                        this.tail = cursor
                    return this
                    }
                }
            }
            cursor = cursor.next
        }
    },
};
