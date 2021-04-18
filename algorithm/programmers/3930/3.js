function solution(x, y, a, b) {
    let answer = 0;
    let xy = []
    for (let i = 0; i < x.length; i++) {
        xy.push([x[i], y[i]])
    }
    let answerList = []
    let prevList = [];
    let nextList = xy.slice();

    function dfs(elements) {
        // if (elements.length === 0) {
        if (prevList.length === a) {
            answerList.push(prevList.slice())
        }

        for (let i = 0; i < elements.length; i++) {
            nextList = elements.slice(prevList.length, nextList.length)

            prevList.push(elements[i])
            dfs(nextList)
            prevList.pop()
        }
    }

    dfs(xy)
    console.log(answerList)

    return answer;
}

function remove(_arr, value) {
    let arr = []
    let index = _arr.indexOf(value)
    if (index !== -1) {
        if (index !== 0)
            arr.push(_arr.slice(0, index));
        arr.push(_arr.slice(index + 1));
        return arr[0]
    }
    return _arr
}

console.log(solution([0, 1, 2, 3, 4], [0, 1, 2, 3, 4], 2, 2)) //18
console.log(solution([0, 1, 2, 3, 4], [0, 0, 0, 0, 0], 3, 2)) //4
