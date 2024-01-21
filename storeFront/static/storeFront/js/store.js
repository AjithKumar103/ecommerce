
let rowOne = document.querySelector('#row-one')
p_name = 'rice'
p_price = 48.76
id = 1
for (let i = 0; i < 8; i++){

  rowOne.innerHTML += `<div class="col-lg-3">
  <img class="thumbnail" src="" alt="Product">
  <div class="box-element product">
    <h6><strong>${p_name}</strong></h6>
    <hr>
    <div class="flex-container">
      <h6>Price:</h6>
      <h6>Rs.${p_price}</h6>
    </div>
    <hr>
    <div class="flex-container">
      <button data-product=${id} data-action="add" class="btn btn-outline-warning add-btn update-cart">Add To
        Cart</button>
      <a href="#" class="btn btn-outline-primary">View</a>
    </div>
  </div>
</div>`;
}
