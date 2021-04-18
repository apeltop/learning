// 병합 정렬
function merge(leftA, rightA) {
    let results = [], leftIndex = 0, rightIndex = 0;

    while (leftIndex < leftA.length && rightIndex < rightA.length) {
        if (leftA[leftIndex] < rightA[rightIndex]) {
            results.push(leftA[leftIndex++]);
        } else {
            results.push(rightA[rightIndex++])
        }
    }

    let leftRemains = leftA.slice(leftIndex);
    let rightRemains = rightA.slice(rightIndex);

    return results.concat(leftRemains).concat(rightRemains)
}

function mergeSort(array) {
    if (array.length < 2) {
        return array;
    }

    let midpoint = Math.floor((array.length) / 2)
    let leftArray = array.slice(0, midpoint)
    let rightArray = array.slice(midpoint)

    return merge(mergeSort(leftArray), mergeSort(rightArray))
}

console.log(mergeSort([6, 1, 23, 4, 2, 3])) //[1, 2, 3, 4, 6, 23]

//스택
function Stack(array) {
    this.array = [];
    if (array) {
        this.array = array;
    }
}

Stack.prototype.getBuffer = function () {
    return this.array.slice();
}

Stack.prototype.isEmpty = function () {
    return this.array.length === 0;
}

Stack.prototype.peek = () => {
    return this.array[this.array.length - 1];
}

Stack.prototype.push = (value) => {
    this.array.push(value);
}

Stack.prototype.pop = () => {
    return this.array.pop();
}
