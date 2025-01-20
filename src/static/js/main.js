const btndelete = document.querySelectorAll('.btn-delete')

if (btndelete){
    const btnArray = Array.from(btndelete)
    btnArray.forEach(btn =>{
        btn.addEnventListener('click', (e)=>{
            if (!confirm('Are you sure you want to delete it?')){
                    e.prevemteDefalut()
            }
        })
    })
}