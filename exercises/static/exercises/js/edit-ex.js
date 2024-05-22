let exercisesList = document.querySelectorAll('#edit-record');

exercisesList.forEach((exercise) => {
    exercise.addEventListener('click', ()=> {
        let idExercise = exercise.dataset.value // Id of chosen EX
        var recordTR = exercise.closest('tr'); 
        fetch(`/exercise/edit/${idExercise}`)
        .then(reponse => reponse.text())
        .then(data => {

            $("#editModal").modal('show');
            document.getElementById("editModalPlaceholder").innerHTML = data;
            editExercise(idExercise, recordTR);
        })

    });
});
$('#editModal').on('shown.bs.modal', async function () {
    await loadExercises();
});


function editExercise(idExercise, recordTR){
    const saveButton = document.getElementById('edit-ex');

    saveButton.addEventListener('click', () => {

        let inputValues = getInputValues();

        let inputReps = inputValues.inputReps;
        let inputSets = inputValues.inputSets;
        let inputKG = inputValues.inputKG;

        fetch('/exercise/edit/', {
            method:'POST',
            headers:{
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                idExercise : idExercise,
                inputReps : inputReps,
                inputSets : inputSets,
                inputKG : inputKG,
            })
        })
        .then(reponse => reponse.json())
        .then(data => {
            
            if(data.success){
                setInputValues(recordTR, inputReps, inputSets, inputKG);
                $("#editModal").modal('toggle');
            }
        });
    });
};
