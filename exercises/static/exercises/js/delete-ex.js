
function deleteExercise(){

    let exercisesList = document.querySelectorAll('#delete-record');

    exercisesList.forEach((exercise) => {
        exercise.addEventListener('click', ()=> {
            let idExercise = exercise.dataset.value // Id of chosen EX
            let recordTR = exercise.closest('tr'); // Whole exercise record
            const toastLiveExample = document.getElementById('liveToast')
            let exerciseName = recordTR.querySelector("#exercise").textContent
            fetch('/exercise/delete/', {
                method:'POST',
                headers:{
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    idExercise : idExercise,
                })
            })
            .then(reponse => reponse.json())
            .then(data => {
                

                if(data.success){
                    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
                    let toastBody = document.querySelector('#toast-res')
                    toastBody.textContent = exerciseName
                    recordTR.remove();

                    toastBootstrap.show()
                }else{

                }
            })

        });
    });    
};
deleteExercise();