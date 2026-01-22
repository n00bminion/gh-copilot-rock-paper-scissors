# Rock, Paper, Scissors, Lizard, Spock - REST API

A Flask-based REST API for playing Rock, Paper, Scissors, Lizard, Spock.

## Quick Start

### Run the API Server

```bash
python app.py
```

The server will start on `http://localhost:5000`

### Run Tests

```bash
# Run all tests
pytest

# Run only API tests
pytest test_api.py -v

# Run only game logic tests
pytest test_main.py -v
```

## API Endpoints

### 1. Play with JSON Payload

**POST** `/play`

**Request Body:**
```json
{
  "choice": "rock"
}
```

**Response (200 OK):**
```json
{
  "user_choice": "rock",
  "computer_choice": "scissors",
  "result": "user",
  "message": "You win!"
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/play \
  -H "Content-Type: application/json" \
  -d '{"choice": "rock"}'
```

### 2. Play with URL Path

**POST** `/play/<choice>`

**Response (200 OK):**
```json
{
  "user_choice": "rock",
  "computer_choice": "paper",
  "result": "computer",
  "message": "Computer wins!"
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/play/rock
```

### 3. Get Valid Choices

**GET** `/choices`

**Response (200 OK):**
```json
{
  "choices": ["rock", "paper", "scissors", "lizard", "spock"]
}
```

**Example:**
```bash
curl http://localhost:5000/choices
```

### 4. Health Check

**GET** `/health`

**Response (200 OK):**
```json
{
  "status": "ok"
}
```

**Example:**
```bash
curl http://localhost:5000/health
```

## Valid Choices

- `rock` - Crushes scissors and lizard
- `paper` - Covers rock and disproves Spock
- `scissors` - Cuts paper and decapitates lizard
- `lizard` - Eats paper and poisons Spock
- `spock` - Vaporizes rock and smashes scissors

## Response Fields

### Successful Play Response

| Field | Type | Description |
|-------|------|-------------|
| `user_choice` | string | The choice you made |
| `computer_choice` | string | The computer's random choice |
| `result` | string | One of: `user`, `computer`, `tie` |
| `message` | string | Human-readable result message |

### Error Response

| Field | Type | Description |
|-------|------|-------------|
| `error` | string | Error description |
| `valid_choices` | array | List of valid choices (when applicable) |

## Error Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 400 | Bad Request (invalid choice or missing data) |
| 404 | Not Found (invalid endpoint) |
| 405 | Method Not Allowed |

## Examples

### Play Rock

```bash
curl -X POST http://localhost:5000/play \
  -H "Content-Type: application/json" \
  -d '{"choice": "rock"}'
```

### Play Spock (URL path)

```bash
curl -X POST http://localhost:5000/play/spock
```

### Invalid Choice

```bash
curl -X POST http://localhost:5000/play \
  -H "Content-Type: application/json" \
  -d '{"choice": "banana"}'
```

Response:
```json
{
  "error": "Invalid choice",
  "valid_choices": ["rock", "paper", "scissors", "lizard", "spock"]
}
```

## CLI Version

To play the game in the terminal:

```bash
python main.py
```

## Project Structure

```
.
├── app.py           # Flask REST API
├── main.py          # CLI game and core logic
├── test_api.py      # API tests (27 tests)
├── test_main.py     # Game logic tests (68 tests)
└── API_README.md    # This file
```

## Development

The game logic is separated into reusable functions in `main.py`:

- `determine_winner(user_choice, computer_choice)` - Determines the winner
- `is_valid_choice(choice)` - Validates a choice
- `get_computer_choice()` - Returns a random computer choice
- `CHOICES` - List of valid choices
- `WINS` - Dictionary mapping each choice to what it beats

This separation allows both the CLI and API to use the same tested game logic.
