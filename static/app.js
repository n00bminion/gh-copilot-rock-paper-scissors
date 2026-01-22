const choices = {
    rock: '✊',
    paper: '✋',
    scissors: '✌️',
    lizard: '🦎',
    spock: '🖖'
};

let stats = {
    wins: 0,
    losses: 0,
    ties: 0
};

// Load stats from localStorage
function loadStats() {
    const savedStats = localStorage.getItem('rpsls-stats');
    if (savedStats) {
        stats = JSON.parse(savedStats);
        updateStatsDisplay();
    }
}

// Save stats to localStorage
function saveStats() {
    localStorage.setItem('rpsls-stats', JSON.stringify(stats));
}

// Update stats display
function updateStatsDisplay() {
    document.getElementById('wins').textContent = stats.wins;
    document.getElementById('losses').textContent = stats.losses;
    document.getElementById('ties').textContent = stats.ties;
}

// Play the game
async function play(userChoice) {
    const resultArea = document.getElementById('result-area');
    const loading = document.getElementById('loading');
    
    // Show loading
    loading.classList.add('show');
    resultArea.classList.remove('show');
    
    try {
        const response = await fetch('/play', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ choice: userChoice })
        });
        
        const data = await response.json();
        
        // Hide loading
        loading.classList.remove('show');
        
        // Display result
        displayResult(data);
        
        // Update stats
        if (data.result === 'user') {
            stats.wins++;
        } else if (data.result === 'computer') {
            stats.losses++;
        } else {
            stats.ties++;
        }
        
        saveStats();
        updateStatsDisplay();
        
    } catch (error) {
        loading.classList.remove('show');
        alert('Error connecting to the server. Please make sure the API is running.');
        console.error('Error:', error);
    }
}

// Display the result
function displayResult(data) {
    const resultArea = document.getElementById('result-area');
    
    // Update player choices
    document.getElementById('user-emoji').textContent = choices[data.user_choice];
    document.getElementById('user-name').textContent = data.user_choice;
    document.getElementById('computer-emoji').textContent = choices[data.computer_choice];
    document.getElementById('computer-name').textContent = data.computer_choice;
    
    // Update result message
    const resultMessage = document.getElementById('result-message');
    resultMessage.textContent = data.message;
    
    // Remove previous result classes
    resultMessage.classList.remove('win', 'lose', 'tie');
    
    // Add appropriate class
    if (data.result === 'user') {
        resultMessage.classList.add('win');
    } else if (data.result === 'computer') {
        resultMessage.classList.add('lose');
    } else {
        resultMessage.classList.add('tie');
    }
    
    // Show result area
    resultArea.classList.add('show');
}

// Initialize the game
document.addEventListener('DOMContentLoaded', () => {
    loadStats();
    
    // Add click handlers to choice buttons
    document.querySelectorAll('.choice-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const choice = btn.dataset.choice;
            play(choice);
        });
    });
});

// Reset stats
function resetStats() {
    if (confirm('Are you sure you want to reset your statistics?')) {
        stats = { wins: 0, losses: 0, ties: 0 };
        saveStats();
        updateStatsDisplay();
    }
}
