const gen_btn = document.getElementById("generate_btn");
gen_btn.addEventListener("click", function () {
    const keep = document.getElementById("inp");
    const keeped = keep.value;
    var keepingInArr = [];
    for (let i = 0; i < keeped; i++) {
        var randomm1 = Math.round(Math.random() * 9);
        keepingInArr.push(randomm1);
    }


    //
    const gen_btn0 = document.getElementById("generate_btn0");
    gen_btn.addEventListener("click", function () {
        const calling = document.getElementById("showingPass");

        calling.value = keepingInArr;
    });


});


// const gen_btn0 = document.getElementById("generate_btn0");
// gen_btn.addEventListener("click", function () {
//     const calling = document.getElementById("showingPass");
//     const keep = document.getElementById("inp");
//     const keeped = keep.value;
//     var keepingInArr = [];
//     for (let i = 0; i < keeped; i++) {
//         var randomm1 = Math.round(Math.random() * 9);
//         keepingInArr.push(randomm1);
//     }
//     calling.value = keepingInArr;

// });
