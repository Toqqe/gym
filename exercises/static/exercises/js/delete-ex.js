let exercisesList = document.querySelectorAll('#delete-record');

exercisesList.forEach((exercise) => {
    exercise.addEventListener('click', ()=> {
        console.log(exercise);
    });
});