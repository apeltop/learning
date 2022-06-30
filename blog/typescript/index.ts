var foo = 1;
console.log(`foo = ${foo}`);

if (1 === 1) {
    var foo = 2;
    console.log(`foo = ${foo}`);
}

console.log(`foo = ${foo}`);

let bar = 1;
console.log(`bar = ${bar}`);

if (bar) {
    let bar = 2;
    console.log(`bar = ${bar}`);
}

console.log(`bar = ${bar}`);

const blog = {
    title: 'blog title'
}

blog.title = 'changed';

console.log(`blog.title = ${blog.title}`)
