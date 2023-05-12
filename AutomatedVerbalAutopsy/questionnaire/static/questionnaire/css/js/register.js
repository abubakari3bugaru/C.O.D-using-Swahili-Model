const usernameField= document.querySelector('#usernameField');
usernameField.addEventListener('keyup',(e) =>{
    console.log("400",409);

    const usernameVal = e.target.value;
    
    if(usernameVal.length>0){
    fetch('/validate-username',{
        body:{username:usernameVal},
        method:'POST',
    }).then(res=>res.json()).then(data =>{
        console.log("data",data)
    });
}
});