"""
REST API for Rock, Paper, Scissors, Lizard, Spock game.
"""
from flask import Flask, request, jsonify, render_template
from main import determine_winner, is_valid_choice, get_computer_choice, CHOICES

app = Flask(__name__)


@app.route('/')
def index():
    """
    Serve the frontend web application.
    """
    return render_template('index.html')


@app.route('/play', methods=['POST'])
def play_game():
    """
    Play the game with a JSON payload.
    
    Expected JSON: {"choice": "rock"}
    Returns: {"user_choice": "rock", "computer_choice": "scissors", "result": "user", "message": "You win!"}
    """
    data = request.get_json()
    
    if not data or 'choice' not in data:
        return jsonify({
            'error': 'Missing choice in request body',
            'valid_choices': CHOICES
        }), 400
    
    user_choice = data['choice'].lower()
    
    if not is_valid_choice(user_choice):
        return jsonify({
            'error': 'Invalid choice',
            'valid_choices': CHOICES
        }), 400
    
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    
    message_map = {
        'user': 'You win!',
        'computer': 'Computer wins!',
        'tie': "It's a tie!"
    }
    
    return jsonify({
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'result': result,
        'message': message_map[result]
    }), 200


@app.route('/play/<choice>', methods=['POST'])
def play_game_with_path(choice):
    """
    Play the game with choice in URL path.
    
    POST /play/rock
    Returns: {"user_choice": "rock", "computer_choice": "scissors", "result": "user", "message": "You win!"}
    """
    user_choice = choice.lower()
    
    if not is_valid_choice(user_choice):
        return jsonify({
            'error': 'Invalid choice',
            'valid_choices': CHOICES
        }), 400
    
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    
    message_map = {
        'user': 'You win!',
        'computer': 'Computer wins!',
        'tie': "It's a tie!"
    }
    
    return jsonify({
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'result': result,
        'message': message_map[result]
    }), 200


@app.route('/choices', methods=['GET'])
def get_choices():
    """
    Get all valid choices.
    
    Returns: {"choices": ["rock", "paper", "scissors", "lizard", "spock"]}
    """
    return jsonify({
        'choices': CHOICES
    }), 200


@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint.
    
    Returns: {"status": "ok"}
    """
    return jsonify({
        'status': 'ok'
    }), 200


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({
        'error': 'Endpoint not found',
        'available_endpoints': {
            'POST /play': 'Play with JSON body: {"choice": "rock"}',
            'POST /play/<choice>': 'Play with URL path: /play/rock',
            'GET /choices': 'Get all valid choices',
            'GET /health': 'Health check'
        }
    }), 404


@app.errorhandler(405)
def method_not_allowed(error):
    """Handle 405 errors."""
    return jsonify({
        'error': 'Method not allowed'
    }), 405


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
