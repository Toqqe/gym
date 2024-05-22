function getInputValues(){
    const bodyPart = JSON.parse(document.getElementById('body-part').textContent)
    const inputExercise = document.getElementById('input-ex');
    const inputReps = document.getElementById('input-reps');
    const inputSets = document.getElementById('input-sets');
    const inputKG = document.getElementById('input-kg');

    return ({
        "bodyPart":bodyPart, 
        "inputExercise": inputExercise.value, 
        "inputReps": inputReps.value, 
        "inputSets":inputSets.value, 
        "inputKG":inputKG.value})
}

function setInputValues(recordTR, newReps, newSets, newKG){
    recordTR.querySelector('#sets').textContent = newSets;
    recordTR.querySelector('#reps').textContent = newReps;
    recordTR.querySelector('#kgs').textContent = newKG+'kg';

}