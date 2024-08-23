import streamlit as st
import random

# Initialize the game board
if 'board' not in st.session_state:
    st.session_state.board = [['' for _ in range(3)] for _ in range(3)]
if 'current_player' not in st.session_state:
    st.session_state.current_player = 'X'
if 'winner' not in st.session_state:
    st.session_state.winner = None

def check_winner():
    board = st.session_state.board
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    return None

def make_move(row, col):
    if st.session_state.board[row][col] == '' and st.session_state.winner is None:
        st.session_state.board[row][col] = st.session_state.current_player
        st.session_state.winner = check_winner()
        if st.session_state.winner is None:
            st.session_state.current_player = 'O' if st.session_state.current_player == 'X' else 'X'
            if st.session_state.current_player == 'O':
                computer_move()

def computer_move():
    board = st.session_state.board
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == '']
    if available_moves:
        row, col = random.choice(available_moves)
        st.session_state.board[row][col] = 'O'
        st.session_state.winner = check_winner()
        if st.session_state.winner is None:
            st.session_state.current_player = 'X'

def reset_game():
    st.session_state.board = [['' for _ in range(3)] for _ in range(3)]
    st.session_state.current_player = 'X'
    st.session_state.winner = None

st.title("Tic Tac Toe")

# Display the game board
for row in range(3):
    cols = st.columns(3)
    for col in range(3):
        if cols[col].button(st.session_state.board[row][col] or " ", key=f"{row}-{col}"):
            make_move(row, col)

# Display the game status
if st.session_state.winner:
    st.success(f"Player {st.session_state.winner} wins!")
elif all(cell != '' for row in st.session_state.board for cell in row):
    st.warning("It's a draw!")
else:
    st.info(f"Current player: {st.session_state.current_player}")

# Reset button
if st.button("Reset Game"):
    reset_game()
