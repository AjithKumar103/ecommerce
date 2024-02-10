
let rowOne = document.querySelector('#row-one')
let rowTwo = document.querySelector('#row-two')
let rowThree = document.querySelector('#row-three')

listProducts()

function listProducts(){
  url = 'http://127.0.0.1:8000/api/product-list/'
  fetch(url)
  .then(response => response.json())
  .then(data => {
    for (let i = 0; i < data.length; i++){
      let snippet = `
      <div class="col-lg-3">
        <img class="thumbnail" src="${data[i].imageUrl}" alt="Product">
        <div id="sample" class="box-element product">
          <h6><strong>${data[i].name}</strong></h6>
          <hr>
          <div class="flex-container">
            <h6>Price:</h6>
            <h6>Rs.${data[i].price}</h6>
          </div>
          <hr>
          <div class="flex-container">
            <button data-pid=${data[i].id} data-action="add" class="btn btn-outline-warning add-to-cart">Add To
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
    const addToCartBtns = document.querySelectorAll('.add-to-cart');
    addToCartBtns.forEach(
      addBtn => addBtn.addEventListener('click',function() {
        url = 'http://127.0.0.1:8000/api/add-to-cart/'
        fetch(url,{
          method:'POST',
          headers:{
            'Content-Type':"application/json"
          },
          body:JSON.stringify({pid:this.dataset.pid,action:'add'}),
        })
        .then(response => {
          if (response.status == 200){
            console.log("OK")
          }else{
            console.log("NO")
          }
        })
      }
      )
    )
  })
}