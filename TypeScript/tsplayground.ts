console.log("Md Naimur Rahman Calling.....")

const myMap = new Map<string, number>();

console.log('This is mymap',myMap);

myMap.set("apple",150);

console.log('Map value ==: \n',myMap);

myMap.set("banana", 50);
myMap.set('orange', 150);

console.log(myMap.get('apple'));

console.log(myMap.has('orange'));

myMap.delete('orange')

myMap.forEach((value,key) => {
    console.log(`${key}: ${value}`);
    
});