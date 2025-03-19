import datetime

class Task:
    """
    Task class to store task details
    """
    def __init__(self, name, deadline, priority):
        self.name = name
        self.deadline = datetime.datetime.strptime(deadline, "%Y-%m-%d %H:%M:%S")
        self.priority = priority

    def __repr__(self):
        return f"Task({self.name}, {self.deadline.strftime('%Y-%m-%d %H:%M:%S')}, {self.priority})"


def priority_level(priority):
    """
    Function to get the priority level (higher is more important)
    """
    priority_map = {"high": 3, "medium": 2, "low": 1}
    return priority_map.get(priority.lower(), 0)


def get_deadline():
    """
    Function to handle the deadline input
    """
    while True:
        try:
            deadline = input("Enter the deadline (YYYY-MM-DD HH:MM:SS): ")
            datetime.datetime.strptime(deadline, "%Y-%m-%d %H:%M:%S")
            return deadline
        except ValueError:
            print("Error: Invalid date format. Please use YYYY-MM-DD HH:MM:SS.")


def get_priority():
    """
    Function to handle the priority input
    """
    while True:
        priority = input("Enter the priority (high, medium, low): ").lower()
        if priority in ['high', 'medium', 'low']:
            return priority
        else:
            print("Error: Invalid priority. Please enter 'high', 'medium', or 'low'.")


def input_tasks():
    """
    Input tasks function
    """
    tasks = []
    while True:
        name = input("Enter the task name (or 'exit' to finish): ")
        if name.lower() == 'exit':
            break
        
        deadline = get_deadline()
        priority = get_priority()
        
        # Create a Task object and add it to the list
        tasks.append(Task(name, deadline, priority))
    return tasks


def generate_schedule(tasks):
    """
    Function to generate a prioritized schedule.
    The function will sort based on deadline first, and if it is the same, then by priority.
    """
    tasks.sort(key=lambda task: (task.deadline, -priority_level(task.priority)))
    return tasks


def display_schedule(tasks):
    """
    Function to display the prioritized schedule
    """
    print("\nPrioritized Schedule:")
    for task in tasks:
        print(f"Task: {task.name}, Deadline: {task.deadline.strftime('%Y-%m-%d %H:%M:%S')}, Priority: {task.priority}")
    print("\n")


def main_task_prioritization():
    print("\nWelcome to the Task Prioritization Program!\n")
    tasks = input_tasks()
    sorted_tasks = generate_schedule(tasks)
    display_schedule(sorted_tasks)
    

def input_scores():
    subjects_scores = {}
    while True:
        subject = input("Enter the subject name (or 'exit' to finish): ")
        if subject.lower() == 'exit':
            break
        try:
            score = float(input(f"Enter the score for {subject}: "))
            if score < 0 or score > 100:
                print("Error: Score should be between 0 and 100.")
                continue
            subjects_scores[subject] = score
        except ValueError:
            print("Error: Please enter a valid number for the score.")
    return subjects_scores


def calculate_average(subjects_scores):
    """
    Function to calculate average score
    """
    total_score = sum(subjects_scores.values())
    num_subjects = len(subjects_scores)
    if num_subjects == 0:
        return 0
    return total_score / num_subjects


def provide_feedback(average_score):
    """
    Function to provide feedback based on the average score
    """
    if average_score >= 90:
        return "Excellent performance! Keep it up!"
    elif average_score >= 75:
        return "Good job! You're doing well, but there's room for improvement."
    elif average_score >= 50:
        return "Fair performance. Consider focusing more on your studies."
    else:
        return "Needs Improvement. It's time to focus more on your studies."
    
    
def suggest_subject_to_improve(subjects_scores):
    """
    Function to get the subject with lowest score for future improvement reference.
    """
    if not subjects_scores:
        return None
    lowest_subject = min(subjects_scores, key=subjects_scores.get)
    lowest_score = subjects_scores[lowest_subject]
    return lowest_subject, lowest_score


def main_performance_tracking():
    """
    Main function for the performance tracking task.
    """
    print("Welcome to the Performance Tracking Program!")
    subjects_scores = input_scores()
    
    if not subjects_scores:
        print("No subjects entered. Exiting the program.")
        return
    
    average_score = calculate_average(subjects_scores)
    print(f"\nYour average score is: {average_score:.2f}")
    
    feedback = provide_feedback(average_score)
    print(feedback)
    
    # Suggest the subject to improve only if average is below 90 where there is room for improvement
    if average_score < 90:
        subject_to_improve = suggest_subject_to_improve(subjects_scores)
        if subject_to_improve:
            subject, score = subject_to_improve
            print(f"\nYou might want to focus more on {subject} where you scored {score:.2f}. Consider reviewing the material or seeking additional help.")

    

def menu():
    """
    Main menu for the study helper.
    """
    while True:
        try:
            n = int(input("Welcome to your study helper! Choose the helper you want:\n1. Task Prioritization\n2. Performance Tracking\n3. Exit\n"))
            if n == 3:
                print("Exiting the study helper. Goodbye!\n")
                break 
        except ValueError as e:
            print(f"Error: {e}\n")
            continue 
        
        if n == 1:
            main_task_prioritization()
        elif n == 2:
            main_performance_tracking()
            

if __name__ == "__main__":
    menu()
