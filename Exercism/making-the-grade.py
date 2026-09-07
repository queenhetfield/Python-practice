"""Functions for organizing and calculating student exam scores."""

def round_scores(student_scores):
    """Round all provided student scores."""
    rounded_scores = []
    for score in student_scores:
        rounded_scores.append(round(score))
    return rounded_scores

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided."""
    failed = 0
    for score in student_scores:
        if score <= 40:
            failed += 1
    return failed

def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold."""
    best_scores = []
    for score in student_scores:
        if score >= threshold:
            best_scores.append(score)
    return best_scores

def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade."""
    step = (highest - 40)/4
    lower_threshold = []
    threshold = highest + 1
    while threshold - step > 40:
        threshold = threshold - step
        lower_threshold.append(int(threshold))
    lower_threshold.sort()
    return lower_threshold
    
def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order."""
    ranks = []
    for index, student in enumerate(student_names):
        combined = f"{index + 1}. {student}: {student_scores[index]}"
        ranks.append(combined)
    return ranks


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam."""
    perfect_student = []
    for student in student_info:
        if student[1] == 100:
            perfect_student = student
            break
    return perfect_student
