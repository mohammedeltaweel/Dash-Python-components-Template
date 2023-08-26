function sliderValShow(){
let rangeInput = document.querySelector(".range-input input");
let rangeValue = document.querySelector(".range-input .value div");

let start = parseInt(rangeInput.min);
let end = parseInt(rangeInput.max);
let step = parseInt(rangeInput.step);
console.log(start);
console.log(end);
console.log(step);

for(let i=start;i<=end;i+=step){
  rangeValue.innerHTML += '<div>'+i+'</div>';
}

rangeInput.addEventListener("input",function(){
  let top = parseInt(rangeInput.value - start) * -40;


  console.log(top);
  rangeValue.style.marginTop = top+"px";
});
}


