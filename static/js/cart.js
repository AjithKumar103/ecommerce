let updateBtns = document.querySelectorAll(".update-cart")

for (let i=0; i < updateBtns.length; i++){
  updateBtns[i].addEventListener('click',function(){
    let productId = this.dataset.product;
    let action = this.dataset.action;
    if(user == 'Anonymoususer'){
      console.log("User is not logged")
    }else{
      console.log({'productId':productId,'action':action})
      updateUserOrder(productId,action);
    }
  })
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
    console.log('data',data);
    window.location.reload()
  })
}