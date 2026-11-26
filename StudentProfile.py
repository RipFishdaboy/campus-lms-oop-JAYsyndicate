class StudentProfile:
    def __init__(self, student_name, student_id, max_points = 100):
        self.student_name = student_name
        self.student_id = student_id
        self.__total_score = 0 
        self.__max_points = max_points 
        
    def add_points(self, points_earned):
        if points_earned < 0:
            raise ValueError("Cannot add negative points!")
        if self.__total_score + points_earned > self.__max_points:
            raise ValueError("Cannot exceed the maximum allowed points!")
        self.__total_score += points_earned

    def get_current_score(self):
        return self.__total_score