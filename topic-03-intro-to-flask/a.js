/*function a(x){returnx*2}
a(2)
output: 4

b = function(x) {returnx*3}
b(4)
12

function(x) {return x*4}
cant have function with no name

(x) => {return x*6} (5)
creates anonymous function

c = (x) =>{return x*6} (4)
c(5)*/

fetch("http://127.0.0.1/data").then(x => x.text()).then(y => console.log(y))
// fetch gets a response and when gotten it promises to call the next thing then when that response is recieved it promise to call the next thing
// this is called chaining promises

