


function addExercise(){
const submitButton = document.getElementById('add-ex');

submitButton.addEventListener('click', ()=>{

    const bodyPart = JSON.parse(document.getElementById('body-part').textContent)
    const inputExercise = document.getElementById('input-ex');
    const inputReps = document.getElementById('input-reps');
    const inputSets = document.getElementById('input-sets');
    const inputKG = document.getElementById('input-kg');
    let emptyString = document.getElementById('placeholder');

    if (inputExercise.value == ''){
        alert('Empty exercise!')
    }else{
        if(inputReps.value == '') inputReps.value = 0;
        if(inputSets.value == '') inputSets.value = 0;
        if(inputKG.value == '') inputKG.value = 0;

        fetch('part/add-exercise/', {
            method:'POST',
            headers:{
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                inputExercise : inputExercise.value,
                bodyPart : bodyPart,   
                inputReps : inputReps.value,                     
                inputSets : inputSets.value,                     
                inputKG : inputKG.value,                     
            })
        })
        .then(response => response.json())
        .then(data => {

            if(data.success){
                let exercisesTab = document.querySelector('tbody');
                let newListItem = document.createElement('tr');

                if(emptyString.style.display != 'none'){
                    emptyString.style.display = 'none';
                }

                newListItem.innerHTML = `
                    <td>${inputExercise.value}</td>
                    <td>${inputReps.value}</td>
                    <td>${inputSets.value}</td>
                    <td>${inputKG.value}</td>
                    <td>
                        <div class="dropdown">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-three-dots" viewBox="0 0 16 16" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                                <path d="M3 9.5a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3m5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3m5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3"/>
                            </svg>
                            <ul class="dropdown-menu">
                            <li id="edit-record" data-value="${data.exercise_id}">Edit</li>
                            <li id="delete-record" data-value="${data.exercise_id}">Delete</li>
                            </ul>
                        </div>
                    </td>`;

                exercisesTab.appendChild(newListItem)
                clearResults();
            }
            else{
                alert(data.message)
                inputExercise.style.borderColor = "red"
                clearResults();
            }

        });
    }
})};
