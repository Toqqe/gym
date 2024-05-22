


function addExercise(){
const submitButton = document.getElementById('add-ex');

submitButton.addEventListener('click', ()=>{

    let inputValues = getInputValues();
    let bodyPart = inputValues.bodyPart;
    let inputExercise = inputValues.inputExercise;
    let inputReps = inputValues.inputReps;
    let inputSets = inputValues.inputSets;
    let inputKG = inputValues.inputKG;
    
    let emptyString = document.getElementById('placeholder');
    if (inputExercise == ''){
        alert('Empty exercise!')
    }else{
        if(inputReps == '') inputReps = 0;
        if(inputSets == '') inputSets = 0;
        if(inputKG == '') inputKG = 0;

        fetch('part/add-exercise/', {
            method:'POST',
            headers:{
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                inputExercise : inputExercise,
                bodyPart : bodyPart,   
                inputReps : inputReps,                     
                inputSets : inputSets,                     
                inputKG : inputKG,                     
            })
        })
        .then(response => response.json())
        .then(data => {

            if(data.success){
                let exercisesTab = document.querySelector('tbody');
                let newListItem = document.createElement('tr');
                newListItem.classList.add("align-middle");

                if(emptyString != null){
                    emptyString.style.display = 'none';
                }

                newListItem.innerHTML = `
                    <td id="exercise">${inputExercise}</td>
                    <td id="reps">${inputReps}</td>
                    <td id="sets">${inputSets}</td>
                    <td id="kgs">${inputKG}kg</td>
                    <td>
                        <div class="dropdown">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-three-dots" viewBox="0 0 16 16" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                                <path d="M3 9.5a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3m5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3m5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3"/>
                            </svg>
                            <ul class="dropdown-menu">
                                <li class="dropdown-item" id="edit-record" data-value="${data.exercise_id}">Edit</li>
                                <li class="dropdown-item" id="delete-record" data-value="${data.exercise_id}">Delete</li>
                            </ul>
                        </div>
                    </td>`;

                exercisesTab.appendChild(newListItem)
                $(function () {
                    $('#partModal').modal('toggle');
                 });
                clearResults();
                deleteExercise();
            }
            else{
                alert(data.message)
                inputExercise.style.borderColor = "red"
                clearResults();
            }

        });
    }
})};
