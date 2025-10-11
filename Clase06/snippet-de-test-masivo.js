['#user-name','#password','#login-button'].forEach(selector=>{
    const elemento=document.querySelector(selector);
    if (elemento) elemento.style.background='red';
});