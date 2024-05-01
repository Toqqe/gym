const group = document.getElementById('front-muscles');
if(group){
    const paths = group.querySelectorAll('path')
    paths.forEach( (part) =>{
        part.addEventListener('click', ()=>{
            let choosed_part = part.id
            fetch(`/part/${choosed_part}`)
            .then(response => response.text())
            .then(data => {
                
                $("#partModal").modal('show');
                document.getElementById("modalPlaceholder").innerHTML = data;
                addExercise();
                searchExercise();
           })
        });
    });
}   

$('#partModal').on('shown.bs.modal', async function () {
    // Call loadExercises() function when the modal is fully shown
    await loadExercises();
    
});