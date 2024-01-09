// var a = 0;
// while (a < 3) {
//   a = a + 3;
// }
// console.log(a)

// var a = 0;
// var x = 3;
// while (a < x) {
//   a = a + 2;
//   x = x + 1;
// }
// console.log(a)

// var a = -10;
// while (a >= -20) {
//   a = a - 3;
// }
// console.log(a)

// var a = 4;
// var b = 10;
// while (a <= b) {
//   a = a + 1;
//   b = b - 2;
// }
// console.log(a,b)

// var a = 1;
// var b = 1;
// var x = -5;
// while (x < 0) {
//   a = a * 1;
//   b = b * 2;
//   x = x + 1;
// }
// console.log(a, b)

// var a = 3;
// var b = 100;
// var c = -2;
// while (a * c < b) {
//   a = a * 2;
//   c = c + 2;
// }
// console.log(a, b, c)

// var x = Number(15)
// // console.log(x)
// var x = Number('6' + 4)
// console.log(x)

// var a = 0;
// var b = 4;
// while (b >= 0) {
//   b = b - 1;
//   a = b;
// }
 
// var c = 0;
// while (b < 8) {
//   b = b + 2;
//   c = c + 1;
// }
// console.log(a, b, c)

// var a = 10;
// var b = 7;
// while (b < 7) {
//   b = b - 1;
//   a = b;
// }
 
// var c = 9;
// while (c == 9) {
//   c = a - b;
// }
// console.log(a, b, c)

var a = 0;
var b = -1;
var c = -2;
var d = -4;
while (a > b) {
  a = a - 1;
  var temp = b;
  b = c;
  c = temp;
}
 
while (a >= d) {
  d = d / 2;
}
 
while (a > c) {
  var temp = d;
  a = d;
  d = temp;
}

console.log(a, b, c, d)
