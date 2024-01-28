
let rowOne = document.querySelector('#row-one')
let rowTwo = document.querySelector('#row-two')
let rowThree = document.querySelector('#row-three')

function listProducts(){
  url = 'http://127.0.0.1:8000/api/productlist/'
  fetch(url)
  .then(response => response.json())
  .then(data => {
    for (let i = 0; i < data.length; i++){
    let snippet = `<div class="col-lg-3">
    <img class="thumbnail" src="${data[i].imageUrl}" alt="Product">
    <div class="box-element product">
      <h6><strong>${data[i].name}</strong></h6>
      <hr>
      <div class="flex-container">
        <h6>Price:</h6>
        <h6>Rs.${data[i].price}</h6>
      </div>
      <hr>
      <div class="flex-container">
        <button data-pId=${data[i].id} data-action="add" class="btn btn-outline-warning add-btn update-cart">Add To
          Cart</button>
        <a href="#" class="btn btn-outline-primary">View</a>
      </div>
    </div>
  </div>`;
  if (data[i].type == 'rc'){
    rowOne.innerHTML += snippet;
  }else if (data[i].type == 'cs'){
    rowTwo.innerHTML += snippet;
  }else if (data[i].type == 'sb'){
    rowThree.innerHTML += snippet;
  }
    }
  })
}

listProducts()

let addBtns = document.querySelectorAll('.add-btn')

addBtns.forEach(function(addBtn){
  addBtn.addEventListener('click',function(e){
    // console.log(this)
    // console.log(this.dataset.pId)
    // url = 'http://127.0.0.1:8000/api/product/'
    // fetch(url)
  })
})