function sumArray(anArray) {
  sum = 0;
  anArray.forEach(function(elem) {
    sum += elem;
  });
  return sum;
}

function averageArray(anArray) {
  return sumArray(anArray) / anArray.length;
}

function minArray(anArray) {
  min = anArray[0];
  anArray.forEach(function(elem) {
    if (elem < min)
      min = elem
  });
  return min;
}

function maxArray(anArray) {
  max = anArray[0];
  anArray.forEach(function(elem) {
    if (elem > max)
      max = elem
  });
  return max;
}

function longestWord(anArray) {
  max = anArray[0];
  anArray.forEach(function(elem) {
    if (elem.length > max.length)
      max = elem
  });
  return max;
}

function shortestWord(anArray) {
  min = anArray[0];
  anArray.forEach(function(elem) {
    if (elem.length < min.length)
      min = elem
  });
  return min;
}

function isRightTriangle(a, b, c) {
  sides = [a, b, c];
  sides.sort(function(x, y) {
    return x - y;
  });
  return (Math.pow(sides[0],2) + Math.pow(sides[1],2)) == Math.pow(sides[2],2)
}

function ordinalSuffix(number) {
  tens = number % 10;
  hundreds = number % 100;
  if (tens == 1 && hundreds != 11)
    return "st";
  if (tens == 2 && hundreds != 12)
    return "nd";
  if (tens == 3 && hundreds != 13)
    return "rd";
  return "th";
}

function runMathTests() {
  console.log("Math Tests");

  arrayOne = [61, 98, 56, 99, 88, 58, 61, 93, 53, 57];
  arrayTwo = [479, 485, 445, 347, 334, 375, 351, 424, 335, 407, 348, 377];
  console.log(sumArray(arrayOne) == 724);
  console.log(sumArray(arrayTwo) == 4707);

  console.log(averageArray(arrayOne) == 72.4);
  console.log(averageArray(arrayTwo) == 392.25);

  console.log(minArray(arrayOne) == 53);
  console.log(minArray(arrayTwo) == 334);

  console.log(maxArray(arrayOne) == 99);
  console.log(maxArray(arrayTwo) == 485);
}

function runWordTests() {
  console.log("Word Tests");
  arrayWords = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur'];
  console.log(longestWord(arrayWords) == 'consectetur');
  console.log(shortestWord(arrayWords) == 'sit');
}

function runTriangleTests() {
  console.log("Triangle Tests");
  console.log(isRightTriangle(3, 4, 5) === true);
  console.log(isRightTriangle(13, 12, 5) === true);
  console.log(isRightTriangle(55, 23, 24) === false);
}

function runOrdinalTests() {
  console.log("Ordinal Tests");
  console.log(ordinalSuffix(1) == 'st');
  console.log(ordinalSuffix(31) == 'st');
  console.log(ordinalSuffix(2) == 'nd');
  console.log(ordinalSuffix(52) == 'nd');
  console.log(ordinalSuffix(3) == 'rd');
  console.log(ordinalSuffix(1003) == 'rd');
  console.log(ordinalSuffix(8) == 'th');
  console.log(ordinalSuffix(311) == 'th');
  console.log(ordinalSuffix(312) == 'th');
  console.log(ordinalSuffix(45617813) == 'th');
}

runMathTests();
runWordTests();
runTriangleTests();
runOrdinalTests();
