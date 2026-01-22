"""
Unit tests for the Rock, Paper, Scissors, Lizard, Spock game.
"""
import pytest
from main import determine_winner, is_valid_choice, get_computer_choice, CHOICES, WINS


class TestDetermineWinner:
    """Test the determine_winner function."""
    
    # Test all tie cases
    def test_tie_rock(self):
        assert determine_winner('rock', 'rock') == 'tie'
    
    def test_tie_paper(self):
        assert determine_winner('paper', 'paper') == 'tie'
    
    def test_tie_scissors(self):
        assert determine_winner('scissors', 'scissors') == 'tie'
    
    def test_tie_lizard(self):
        assert determine_winner('lizard', 'lizard') == 'tie'
    
    def test_tie_spock(self):
        assert determine_winner('spock', 'spock') == 'tie'
    
    # Test rock wins
    def test_rock_beats_scissors(self):
        assert determine_winner('rock', 'scissors') == 'user'
    
    def test_rock_beats_lizard(self):
        assert determine_winner('rock', 'lizard') == 'user'
    
    # Test rock loses
    def test_rock_loses_to_paper(self):
        assert determine_winner('rock', 'paper') == 'computer'
    
    def test_rock_loses_to_spock(self):
        assert determine_winner('rock', 'spock') == 'computer'
    
    # Test paper wins
    def test_paper_beats_rock(self):
        assert determine_winner('paper', 'rock') == 'user'
    
    def test_paper_beats_spock(self):
        assert determine_winner('paper', 'spock') == 'user'
    
    # Test paper loses
    def test_paper_loses_to_scissors(self):
        assert determine_winner('paper', 'scissors') == 'computer'
    
    def test_paper_loses_to_lizard(self):
        assert determine_winner('paper', 'lizard') == 'computer'
    
    # Test scissors wins
    def test_scissors_beats_paper(self):
        assert determine_winner('scissors', 'paper') == 'user'
    
    def test_scissors_beats_lizard(self):
        assert determine_winner('scissors', 'lizard') == 'user'
    
    # Test scissors loses
    def test_scissors_loses_to_rock(self):
        assert determine_winner('scissors', 'rock') == 'computer'
    
    def test_scissors_loses_to_spock(self):
        assert determine_winner('scissors', 'spock') == 'computer'
    
    # Test lizard wins
    def test_lizard_beats_paper(self):
        assert determine_winner('lizard', 'paper') == 'user'
    
    def test_lizard_beats_spock(self):
        assert determine_winner('lizard', 'spock') == 'user'
    
    # Test lizard loses
    def test_lizard_loses_to_rock(self):
        assert determine_winner('lizard', 'rock') == 'computer'
    
    def test_lizard_loses_to_scissors(self):
        assert determine_winner('lizard', 'scissors') == 'computer'
    
    # Test spock wins
    def test_spock_beats_rock(self):
        assert determine_winner('spock', 'rock') == 'user'
    
    def test_spock_beats_scissors(self):
        assert determine_winner('spock', 'scissors') == 'user'
    
    # Test spock loses
    def test_spock_loses_to_paper(self):
        assert determine_winner('spock', 'paper') == 'computer'
    
    def test_spock_loses_to_lizard(self):
        assert determine_winner('spock', 'lizard') == 'computer'


class TestIsValidChoice:
    """Test the is_valid_choice function."""
    
    def test_valid_rock(self):
        assert is_valid_choice('rock') is True
    
    def test_valid_paper(self):
        assert is_valid_choice('paper') is True
    
    def test_valid_scissors(self):
        assert is_valid_choice('scissors') is True
    
    def test_valid_lizard(self):
        assert is_valid_choice('lizard') is True
    
    def test_valid_spock(self):
        assert is_valid_choice('spock') is True
    
    def test_invalid_choice_empty_string(self):
        assert is_valid_choice('') is False
    
    def test_invalid_choice_random_word(self):
        assert is_valid_choice('banana') is False
    
    def test_invalid_choice_uppercase(self):
        assert is_valid_choice('ROCK') is False
    
    def test_invalid_choice_mixed_case(self):
        assert is_valid_choice('Rock') is False
    
    def test_invalid_choice_number(self):
        assert is_valid_choice('123') is False
    
    def test_invalid_choice_special_chars(self):
        assert is_valid_choice('rock!') is False
    
    def test_invalid_choice_with_spaces(self):
        assert is_valid_choice('rock ') is False
    
    def test_invalid_choice_with_leading_spaces(self):
        assert is_valid_choice(' rock') is False
    
    def test_invalid_choice_quit(self):
        assert is_valid_choice('quit') is False
    
    def test_invalid_choice_partial_match(self):
        assert is_valid_choice('roc') is False


class TestGetComputerChoice:
    """Test the get_computer_choice function."""
    
    def test_returns_valid_choice(self):
        """Test that computer choice is always valid."""
        for _ in range(100):  # Test multiple times due to randomness
            choice = get_computer_choice()
            assert choice in CHOICES
    
    def test_returns_string(self):
        """Test that computer choice returns a string."""
        choice = get_computer_choice()
        assert isinstance(choice, str)
    
    def test_randomness(self):
        """Test that computer choice is somewhat random (not always the same)."""
        choices = set()
        for _ in range(100):
            choices.add(get_computer_choice())
        # With 100 random choices from 5 options, we should get at least 3 different ones
        assert len(choices) >= 3


class TestGameConfiguration:
    """Test the game configuration constants."""
    
    def test_choices_has_five_elements(self):
        assert len(CHOICES) == 5
    
    def test_choices_contains_expected_values(self):
        expected = {'rock', 'paper', 'scissors', 'lizard', 'spock'}
        assert set(CHOICES) == expected
    
    def test_wins_has_all_choices_as_keys(self):
        assert set(WINS.keys()) == set(CHOICES)
    
    def test_each_choice_beats_exactly_two_others(self):
        for choice, beats in WINS.items():
            assert len(beats) == 2, f"{choice} should beat exactly 2 choices"
    
    def test_no_choice_beats_itself(self):
        for choice, beats in WINS.items():
            assert choice not in beats, f"{choice} should not beat itself"
    
    def test_win_relationships_are_valid(self):
        """Test that all win relationships reference valid choices."""
        for choice, beats in WINS.items():
            for beaten in beats:
                assert beaten in CHOICES, f"{beaten} is not a valid choice"
    
    def test_symmetry_of_wins(self):
        """Test that if A beats B, then B does not beat A."""
        for choice_a, beats_a in WINS.items():
            for choice_b in beats_a:
                assert choice_a not in WINS[choice_b], \
                    f"Invalid symmetry: {choice_a} beats {choice_b} and vice versa"


class TestEdgeCases:
    """Test edge cases and special scenarios."""
    
    def test_determine_winner_with_same_choices_multiple_times(self):
        """Test that ties work consistently."""
        for choice in CHOICES:
            assert determine_winner(choice, choice) == 'tie'
    
    def test_comprehensive_win_matrix(self):
        """Test all possible combinations to ensure completeness."""
        results_count = {'user': 0, 'computer': 0, 'tie': 0}
        
        for user_choice in CHOICES:
            for computer_choice in CHOICES:
                result = determine_winner(user_choice, computer_choice)
                assert result in ['user', 'computer', 'tie']
                results_count[result] += 1
        
        # With 5 choices, we have 25 total combinations
        # 5 should be ties (same choice)
        # 10 should be user wins (each choice beats 2 others)
        # 10 should be computer wins (each choice loses to 2 others)
        assert results_count['tie'] == 5
        assert results_count['user'] == 10
        assert results_count['computer'] == 10
    
    @pytest.mark.parametrize("choice", CHOICES)
    def test_each_choice_wins_and_loses(self, choice):
        """Test that each choice can both win and lose."""
        wins = 0
        losses = 0
        ties = 0
        
        for opponent in CHOICES:
            result = determine_winner(choice, opponent)
            if result == 'user':
                wins += 1
            elif result == 'computer':
                losses += 1
            else:
                ties += 1
        
        assert wins == 2, f"{choice} should win against exactly 2 choices"
        assert losses == 2, f"{choice} should lose against exactly 2 choices"
        assert ties == 1, f"{choice} should tie against exactly 1 choice (itself)"
    
    def test_determine_winner_consistency(self):
        """Test that same inputs always produce same output."""
        # Test multiple times to ensure consistency
        for _ in range(10):
            assert determine_winner('rock', 'scissors') == 'user'
            assert determine_winner('scissors', 'rock') == 'computer'
            assert determine_winner('paper', 'paper') == 'tie'


class TestWinLogic:
    """Test specific win logic scenarios based on the game rules."""
    
    def test_rock_crushes_scissors(self):
        """Rock crushes scissors."""
        assert determine_winner('rock', 'scissors') == 'user'
        assert determine_winner('scissors', 'rock') == 'computer'
    
    def test_rock_crushes_lizard(self):
        """Rock crushes lizard."""
        assert determine_winner('rock', 'lizard') == 'user'
        assert determine_winner('lizard', 'rock') == 'computer'
    
    def test_paper_covers_rock(self):
        """Paper covers rock."""
        assert determine_winner('paper', 'rock') == 'user'
        assert determine_winner('rock', 'paper') == 'computer'
    
    def test_paper_disproves_spock(self):
        """Paper disproves Spock."""
        assert determine_winner('paper', 'spock') == 'user'
        assert determine_winner('spock', 'paper') == 'computer'
    
    def test_scissors_cuts_paper(self):
        """Scissors cuts paper."""
        assert determine_winner('scissors', 'paper') == 'user'
        assert determine_winner('paper', 'scissors') == 'computer'
    
    def test_scissors_decapitates_lizard(self):
        """Scissors decapitates lizard."""
        assert determine_winner('scissors', 'lizard') == 'user'
        assert determine_winner('lizard', 'scissors') == 'computer'
    
    def test_lizard_eats_paper(self):
        """Lizard eats paper."""
        assert determine_winner('lizard', 'paper') == 'user'
        assert determine_winner('paper', 'lizard') == 'computer'
    
    def test_lizard_poisons_spock(self):
        """Lizard poisons Spock."""
        assert determine_winner('lizard', 'spock') == 'user'
        assert determine_winner('spock', 'lizard') == 'computer'
    
    def test_spock_vaporizes_rock(self):
        """Spock vaporizes rock."""
        assert determine_winner('spock', 'rock') == 'user'
        assert determine_winner('rock', 'spock') == 'computer'
    
    def test_spock_smashes_scissors(self):
        """Spock smashes scissors."""
        assert determine_winner('spock', 'scissors') == 'user'
        assert determine_winner('scissors', 'spock') == 'computer'
