import random

class GameState:
    def __init__(self):
        self.current_score = 0
        self.total_questions = 0
        self.games_played = 0
        self.total_score = 0
        self.current_question_index = 0
        self.shuffled_questions = []
        
    def shuffle_options(self, question):
        options = [(opt, opt == question['correct_answer']) for opt in question['options']]
        random.shuffle(options)
        
        shuffled_options = [opt[0] for opt in options]
        correct_index = next(i for i, opt in enumerate(options) if opt[1])
        
        return {
            'question': question['question'],
            'options': shuffled_options,
            'answer': chr(97 + correct_index)
        }
        
    def prepare_questions(self, questions, num_questions=20):
        selected_questions = random.sample(
            questions,
            min(num_questions, len(questions))
        )
        self.total_questions = len(selected_questions)
        self.shuffled_questions = [self.shuffle_options(q) for q in selected_questions]
        self.current_question_index = 0
        self.current_score = 0
        
    def get_current_question(self):
        if self.current_question_index < len(self.shuffled_questions):
            return self.shuffled_questions[self.current_question_index]
        return None
        
    def check_answer(self, user_answer):
        current_question = self.get_current_question()
        if current_question and user_answer == current_question['answer']:
            self.current_score += 1
            return True
        return False
        
    def next_question(self):
        self.current_question_index += 1
        
    def is_game_over(self):
        return self.current_question_index >= len(self.shuffled_questions)
        
    def finish_game(self):
        self.games_played += 1
        self.total_score += self.current_score