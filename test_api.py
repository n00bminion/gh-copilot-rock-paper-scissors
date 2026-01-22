"""
Unit tests for the Rock, Paper, Scissors, Lizard, Spock REST API.
"""
import pytest
import json
from app import app
from main import CHOICES


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestPlayEndpointWithJSON:
    """Test the /play endpoint with JSON payload."""
    
    def test_play_with_valid_choice_rock(self, client):
        response = client.post('/play',
                              data=json.dumps({'choice': 'rock'}),
                              content_type='application/json')
        assert response.status_code == 200
        data = response.get_json()
        assert data['user_choice'] == 'rock'
        assert data['computer_choice'] in CHOICES
        assert data['result'] in ['user', 'computer', 'tie']
        assert 'message' in data
    
    def test_play_with_valid_choice_paper(self, client):
        response = client.post('/play',
                              data=json.dumps({'choice': 'paper'}),
                              content_type='application/json')
        assert response.status_code == 200
        data = response.get_json()
        assert data['user_choice'] == 'paper'
    
    def test_play_with_valid_choice_scissors(self, client):
        response = client.post('/play',
                              data=json.dumps({'choice': 'scissors'}),
                              content_type='application/json')
        assert response.status_code == 200
        data = response.get_json()
        assert data['user_choice'] == 'scissors'
    
    def test_play_with_valid_choice_lizard(self, client):
        response = client.post('/play',
                              data=json.dumps({'choice': 'lizard'}),
                              content_type='application/json')
        assert response.status_code == 200
        data = response.get_json()
        assert data['user_choice'] == 'lizard'
    
    def test_play_with_valid_choice_spock(self, client):
        response = client.post('/play',
                              data=json.dumps({'choice': 'spock'}),
                              content_type='application/json')
        assert response.status_code == 200
        data = response.get_json()
        assert data['user_choice'] == 'spock'
    
    def test_play_with_uppercase_choice(self, client):
        response = client.post('/play',
                              data=json.dumps({'choice': 'ROCK'}),
                              content_type='application/json')
        assert response.status_code == 200
        data = response.get_json()
        assert data['user_choice'] == 'rock'
    
    def test_play_with_mixed_case_choice(self, client):
        response = client.post('/play',
                              data=json.dumps({'choice': 'RoCk'}),
                              content_type='application/json')
        assert response.status_code == 200
        data = response.get_json()
        assert data['user_choice'] == 'rock'
    
    def test_play_with_invalid_choice(self, client):
        response = client.post('/play',
                              data=json.dumps({'choice': 'banana'}),
                              content_type='application/json')
        assert response.status_code == 400
        data = response.get_json()
        assert 'error' in data
        assert data['error'] == 'Invalid choice'
        assert 'valid_choices' in data
    
    def test_play_with_missing_choice(self, client):
        response = client.post('/play',
                              data=json.dumps({}),
                              content_type='application/json')
        assert response.status_code == 400
        data = response.get_json()
        assert 'error' in data
        assert 'Missing choice' in data['error']
    
    def test_play_with_empty_body(self, client):
        response = client.post('/play',
                              data='',
                              content_type='application/json')
        assert response.status_code == 400
    
    def test_play_with_invalid_json(self, client):
        response = client.post('/play',
                              data='invalid json',
                              content_type='application/json')
        assert response.status_code == 400


class TestPlayEndpointWithPath:
    """Test the /play/<choice> endpoint."""
    
    def test_play_with_path_rock(self, client):
        response = client.post('/play/rock')
        assert response.status_code == 200
        data = response.get_json()
        assert data['user_choice'] == 'rock'
        assert data['computer_choice'] in CHOICES
        assert data['result'] in ['user', 'computer', 'tie']
        assert 'message' in data
    
    def test_play_with_path_paper(self, client):
        response = client.post('/play/paper')
        assert response.status_code == 200
        data = response.get_json()
        assert data['user_choice'] == 'paper'
    
    def test_play_with_path_scissors(self, client):
        response = client.post('/play/scissors')
        assert response.status_code == 200
        data = response.get_json()
        assert data['user_choice'] == 'scissors'
    
    def test_play_with_path_lizard(self, client):
        response = client.post('/play/lizard')
        assert response.status_code == 200
        data = response.get_json()
        assert data['user_choice'] == 'lizard'
    
    def test_play_with_path_spock(self, client):
        response = client.post('/play/spock')
        assert response.status_code == 200
        data = response.get_json()
        assert data['user_choice'] == 'spock'
    
    def test_play_with_path_uppercase(self, client):
        response = client.post('/play/ROCK')
        assert response.status_code == 200
        data = response.get_json()
        assert data['user_choice'] == 'rock'
    
    def test_play_with_path_invalid_choice(self, client):
        response = client.post('/play/banana')
        assert response.status_code == 400
        data = response.get_json()
        assert 'error' in data
        assert data['error'] == 'Invalid choice'


class TestChoicesEndpoint:
    """Test the /choices endpoint."""
    
    def test_get_choices(self, client):
        response = client.get('/choices')
        assert response.status_code == 200
        data = response.get_json()
        assert 'choices' in data
        assert len(data['choices']) == 5
        assert set(data['choices']) == set(CHOICES)


class TestHealthEndpoint:
    """Test the /health endpoint."""
    
    def test_health_check(self, client):
        response = client.get('/health')
        assert response.status_code == 200
        data = response.get_json()
        assert data['status'] == 'ok'


class TestErrorHandling:
    """Test error handling."""
    
    def test_404_not_found(self, client):
        response = client.get('/nonexistent')
        assert response.status_code == 404
        data = response.get_json()
        assert 'error' in data
        assert data['error'] == 'Endpoint not found'
        assert 'available_endpoints' in data
    
    def test_method_not_allowed_get_on_play(self, client):
        response = client.get('/play')
        assert response.status_code == 405
        data = response.get_json()
        assert 'error' in data
        assert data['error'] == 'Method not allowed'
    
    def test_method_not_allowed_delete_on_play(self, client):
        response = client.delete('/play')
        assert response.status_code == 405


class TestResponseStructure:
    """Test the structure of API responses."""
    
    def test_play_response_has_all_fields(self, client):
        response = client.post('/play',
                              data=json.dumps({'choice': 'rock'}),
                              content_type='application/json')
        data = response.get_json()
        assert 'user_choice' in data
        assert 'computer_choice' in data
        assert 'result' in data
        assert 'message' in data
    
    def test_play_result_messages(self, client):
        # Test multiple times to potentially get all result types
        messages_seen = set()
        for _ in range(50):
            response = client.post('/play',
                                  data=json.dumps({'choice': 'rock'}),
                                  content_type='application/json')
            data = response.get_json()
            messages_seen.add(data['message'])
        
        # We should see at least one type of message
        assert len(messages_seen) > 0
        # All messages should be valid
        valid_messages = {'You win!', 'Computer wins!', "It's a tie!"}
        assert messages_seen.issubset(valid_messages)


class TestMultipleRequests:
    """Test multiple sequential requests."""
    
    def test_multiple_plays_are_independent(self, client):
        results = []
        for _ in range(10):
            response = client.post('/play',
                                  data=json.dumps({'choice': 'rock'}),
                                  content_type='application/json')
            data = response.get_json()
            results.append(data['computer_choice'])
        
        # All responses should be valid
        assert all(choice in CHOICES for choice in results)
    
    def test_different_choices_in_sequence(self, client):
        for choice in CHOICES:
            response = client.post('/play',
                                  data=json.dumps({'choice': choice}),
                                  content_type='application/json')
            assert response.status_code == 200
            data = response.get_json()
            assert data['user_choice'] == choice
