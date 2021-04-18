function Queue(array) {
    this.array = [];
    if (array) this.array = array;
}

Queue.prototype.getBuffer = function () {
    return this.array.slice();
}

Queue.prototype.isEmpty = function () {
    return this.array.length === 0;
}

Queue.prototype.peek = function () {
    return this.array[0];
}

Queue.prototype.enqueue = function (value) {
    return this.array.push(value);
}

Queue.prototype.dequeue = function () {
    return this.array.shift();
};

Queue.prototype.size = function () {
    return this.array.length;
};

function queueSearch(queue, element) {
    let bufferArray = queue.getBuffer();

    let bufferQueue = new Queue(bufferArray);

    while (!bufferQueue.isEmpty()) {
        if (bufferQueue.dequeue() === element) {
            return true;
        }
    }
    return false;
}


function Server() {
    this.charQ = new Queue();
}

Server.prototype.createChar = function (name) {
    if (queueSearch(this.charQ, name))
        return;

    if (this.charQ.size() === 5) {
        this.charQ.dequeue()
        this.charQ.enqueue(name);
    } else {
        this.charQ.enqueue(name);
    }
}

Server.prototype.getChars = function () {
    return this.charQ.getBuffer();
}

function solution(n, record) {
    let answer = [];

    let serverDict = {}
    for (let i = 0; i < n; i++) {
        let serverId = i + 1;
        serverDict[serverId] = new Server(serverId);
    }

    for (const elem of record) {
        let [serverId, name] = elem.split(" ")
        serverDict[serverId].createChar(name);
    }

    for (const server in serverDict) {
        for (const name of serverDict[server].getChars()) {
            answer.push(name);
        }
    }

    return answer;
}

//["sina", "hana", "robel", "abc", "lynn"]
console.log(solution(1, ["1 fracta", "1 sina", "1 hana", "1 robel", "1 abc", "1 sina", "1 lynn"]))

//["abc", "abcd", "aaa", "z", "q", "k", "q", "z", "m", "b"]
console.log(solution(4, ["1 a", "1 b", "1 abc", "3 b", "3 a", "1 abcd", "1 abc", "1 aaa", "1 a", "1 z", "1 q", "3 k", "3 q", "3 z", "3 m", "3 b"]))

