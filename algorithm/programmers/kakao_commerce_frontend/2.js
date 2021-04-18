function Stack(array) {
    this.array = [];
    if (array) {
        this.array = array;
    }
}

Stack.prototype.getBuffer = function (start = 0) {
    return this.array.slice(start);
}

Stack.prototype.isEmpty = function () {
    return this.array.length === 0;
}

Stack.prototype.peek = () => {
    return this.array[this.array.length - 1];
}

Stack.prototype.push = function (value) {
    this.array.push(value);
}

Stack.prototype.pop = () => {
    return this.array.pop();
}

Stack.prototype.size = function () {
    return this.array.length;
};

function RowStack(m) {
    this.curIndex = 0;
    this.m = m;
}

RowStack.prototype.size = function () {
    return this.curIndex;
}

RowStack.prototype.isRemains = function (size) {
    return this.m - this.size() >= size;
}

RowStack.prototype.stacking = function (size) {
    this.curIndex += size;
}

function ColumnStack(m) {
    this.stack = new Stack()
    this.m = m;
}

ColumnStack.prototype.size = function () {
    return this.stack.size();
}

ColumnStack.prototype.addRow = function () {
    let newRow = new RowStack(this.m)
    this.stack.push(newRow)
    return newRow;
}

ColumnStack.prototype.getPossibleIndex = function (v) {
    let stk = this.stack.getBuffer().reverse()
    for (let i = 0 ; i < this.size(); i++) {
        let row = stk[i];
        if (!row.isRemains(v)) {
            return this.size() - i;
        }
    }

    return 0;
}

ColumnStack.prototype.addBlock = function (v) {
    for (const row of this.stack.getBuffer(this.getPossibleIndex(v))) {
        if (row.isRemains(v)) {
            row.stacking(v)
            return;
        }
    }
    let newRow = this.addRow();
    newRow.stacking(v)
}

function solution(m, v) {
    let columnStack = new ColumnStack(m)

    for (const r of v) {
        columnStack.addBlock(r)
    }

    return columnStack.size();
}


//2
console.log(solution(4, [2, 3, 1]))

//3
console.log(solution(4, [3, 2, 3, 1]))

//2
console.log(solution(4, [1, 4, 1, 1]))

//4
console.log(solution(4, [3, 2, 3, 2]))

