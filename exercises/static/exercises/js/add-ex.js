


function addExercise(){
const submitButton = document.getElementById('add-ex');

submitButton.addEventListener('click', ()=>{

    const bodyPart = JSON.parse(document.getElementById('body-part').textContent)
    const inputExercise = document.getElementById('input-ex');
    const inputReps = document.getElementById('input-reps');
    const inputSets = document.getElementById('input-sets');
    const inputKG = document.getElementById('input-kg');


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
                let rows = exercisesTab.rows.length;

                newListItem.innerHTML = `
                    <th scope="row">${rows+1}</th>
                    <td>${inputExercise.value}</td>
                    <td>${inputReps.value}</td>
                    <td>${inputSets.value}</td>
                    <td>${inputKG.value}</td>
                `;
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
