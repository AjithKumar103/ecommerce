const cartBox = document.getElementById('cart-box')

function showCartItems(){
  const url = 'http://127.0.0.1:8000/api/cart-list/'
  fetch(url)
  .then( response => response.json())
  .then( data => {
    cartItems = data.order_items
    for (let i = 0; i < data.order_items.length; i++){
      cartBox.innerHTML += `
      <div class="cart-row">
        <div style="flex:2"><img class="row-image" src="${cartItems[i].product_item.imageUrl}"></div>
        <div style="flex:2">
          <p>${cartItems[i].product_item.name}</p>
        </div>
        <div style="flex:1">
          <p>Rs.${cartItems[i].product_item.price}</p>
        </div>
        <div style="flex:1">
          <p class="quantity">${cartItems[i].quantity}</p>
          <div class="quantity">
            <img data-product=${cartItems[i].id} data-action="add" class="chg-quantity update-cart"
              src="/media/images/arrow-up.png">
      
            <img data-product=${cartItems[i].id} data-action="remove" class="chg-quantity update-cart"
              src="/media/images/arrow-down.png">
          </div>
        </div>
        <div style="flex:1">
          <p>Rs.${cartItems[i].get_total}</p>
        </div>
      </div>`
    }
  })
}

showCartItems()
