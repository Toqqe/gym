let searchData = [];

async function loadExercises(){
    try{
        const bodyPart = JSON.parse(document.getElementById('body-part').textContent)
        const response = await fetch(`search/${bodyPart}`);
        if(!response.ok){
            throw new Error('Network reponse was not OK!')
        }
        searchData = await response.json();
        console.log(searchData.exercises)
    } catch(error){
        console.error('Error fetching data:', error);
    }
};

function searchExercise(){
    const inputExercise = document.getElementById('input-ex');
    inputExercise.addEventListener("input", (input) => {
        const searchText = input.target.value.toLowerCase();
        inputExercise.style.borderColor = '#dee2e6';
        if(searchText === ''){
            clearResults();
            return;
        }

        const filteredData = searchData.exercises.filter(item => {
            return item.toLowerCase().includes(searchText);
        })
        displayResults(filteredData);
    });
};

function displayResults(results) {
    const resultsContainer = document.getElementById('search-result');

    resultsContainer.innerHTML = '';

    results.forEach(result => {
        const resultElement = document.createElement('li');
        resultElement.classList.add('list-group-item', 'p-2'); //, 'p-2', 'bg-light', 'border', 'rounded');

        resultElement.textContent = result;
        resultsContainer.appendChild(resultElement);
    });
    exercisesHandler();
};

function clearResults() {
    const resultsContainer = document.getElementById('search-result');
    resultsContainer.innerHTML = ''; // Clear the results container
};


function exercisesHandler(){
    const liItemsList = document.querySelectorAll('.list-group-item');
    
    liItemsList.forEach( (item) => {
        item.addEventListener('click', ()=>{
            let inputExercise = document.getElementById('input-ex');
            inputExercise.value = item.textContent;
            clearResults();
        });
    });


};