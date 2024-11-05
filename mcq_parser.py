import re

def parse_questions(text):
    questions = []
    question_blocks = re.split(r'\n\n+', text)
    
    for block in question_blocks:
        lines = block.strip().split('\n')
        if len(lines) >= 6:  # Question + 4 options + Answer
            question = lines[0].strip()
            options = []
            answer_text = None
            
            # Get options
            for line in lines[1:5]:
                if line.startswith(('a)', 'b)', 'c)', 'd)')):
                    option = line[3:].strip()
                    options.append(option)
            
            # Get answer
            for line in lines:
                if line.startswith('Answer:'):
                    answer_text = line[8:].strip()
                    break
            
            if question and len(options) == 4 and answer_text:
                # Store the correct answer text instead of just the letter
                correct_answer = options[ord(answer_text[0].lower()) - ord('a')]
                questions.append({
                    'question': question,
                    'options': options,
                    'correct_answer': correct_answer
                })
    
    return questions