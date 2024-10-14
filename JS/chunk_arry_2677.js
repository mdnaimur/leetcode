// chunk_arry_2677.js


var chunk = function (arr, size) {

    let sub_arry = []

    for (var i = 0; i < arr.length; i += size) {

        //  console.log("i value", i)
        ////  console.log("size", size)
        let new_arr = arr.slice(i, i + size)
        //  console.log("new arry", new_arr);
        sub_arry.push(new_arr)
        //console.log("sub arry list", sub_arry)
    }

    return sub_arry;

};

console.log(chunk([1, 2, 3, 4, 5, 6], 2));