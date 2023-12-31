let updateBtns = document.querySelectorAll(".update-cart");

for (let i=0; i < updateBtns.length; i++){
  updateBtns[i].addEventListener('click',function(){
    let productId = this.dataset.product;
    let action = this.dataset.action;
    if(user == 'AnonymousUser'){
      addCookieItem(productId,action);
    }else{
      updateUserOrder(productId,action);
    }
  })
}

function addCookieItem(productId,action){
  if (action == 'add'){
    if (cart[productId] == undefined){
      cart[productId] = {'quantity':1}
    }else{
      cart[productId]['quantity'] += 1
    }
  }
  if (action == 'remove'){
    cart[productId]['quantity'] -= 1
    if (cart[productId]['quantity'] <= 0){
      delete cart[productId]
    }
  }
  console.log(cart)
  document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
  location.reload()
}

function updateUserOrder(productId,action){
  console.log("user is logged sending data")
  let url = '/update_item/'
  fetch(url,{
    method:"POST",
    headers:{
      "Content-Type":"application/json",
      "X-CSRFToken":csrftoken},
    body:JSON.stringify({'productId':productId,'action':action})
  })
  .then(response => response.json())
  .then(data => {
    console.log('data',data['response']);
    window.location.reload()
  })
}