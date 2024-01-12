

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys


def welcome_message(name):
    return f"Welcome, {name}! We're glad to have you."

# Example usage:
user_name = input("Welcome to the best expert System for your Gym goals. What is your name?")
message = welcome_message(user_name)
print(message)
class GymExpertSystem:
    def __init__(self):
        self.user_data = {}

    def collect_user_data(self):
        print("We just need some details to begin with:")
        name = input("Name or Nickname: ")
        try:
         age = int(input("Age: "))
        except ValueError:
         print("Invalid input. Please enter a valid number in from 0 to 100 for your age.")
         sys.exit("Your session ends here")
        if age <= 14:
         print("Unfortunately, you can't work out yet. Please come back later.")
         sys.exit("Your session ends here")
        elif 15 <= age < 65:
            proceed = self.get_yes_no_input("Wonderful, now to better understand your goal, we will need to ask a few more questions. Would you like to proceed, yes/no")
            if proceed != 'yes':
             sys.exit("Your session ends here")      

        valid_current_level = ["beginner" , "intermediate" , "advanced"]
        while True:
            current_level = input(" What is your current level at the gym. beginner , intermediate , advanced:  ").strip()
            if current_level in valid_current_level:
                break
            else:
                print("Invalid level. Please choose a valid level.") 
        valid_goals = ["weight_loss" , "muscle_gain", "general_fitness"  , "hiit"]
        while True:
            goal = input("Fitness goal (weight_loss , muscle_gain, general_fitness  or hiit ): ").strip()
            if goal in valid_goals:
                break
            else:
                print("Invalid goal. Please choose a valid goal.")
        while True:
            try:
                weight = float(input("What is your weight in KG? "))
                if 40 <= weight <= 200:  
                    break
                else:
                    print("Invalid input. Please enter a weight between 40 and 200 KG.")
            except ValueError:
                 print("Invalid input. Please enter a valid number for your weight.")                
        body_injury = input("Do you have any serious injuries or recovering from previous conditions? ")
        if body_injury.lower() == "yes":
            print("It is strongly recommended that you contact your doctor or a physician before proceeding")
            sys.exi("you session ends here")
        elif body_injury.lower() == "no":
            print("Excellent news, we are working on your request. Bare with us")
        
               
   

        # Store collected data in user_data
        self.user_data = {
            'name': name,
            'age': age,
            'goal': goal,
            'weight': weight,
            'body_injury': body_injury,
            'current_level': current_level,
          
        }        

        print("Here are the details you have provided:", self.user_data)  
    
             
    def get_yes_no_input(self, prompt):
        while True:
            response = input(f"{prompt} (yes/no): ").lower()
            if response in ('yes', 'no'):
                return response
            else:
                print("Invalid response. Please enter 'yes' or 'no'.")   
    
    def suggest_exercises(self):
     age = self.user_data.get('age', 0)
     goal = self.user_data.get('goal', '').lower()
     weight = self.user_data.get('weight', 0)
     current_level = self.user_data.get('current_level', '').lower()
     body_injury = self.user_data.get('body_injury').lower()
     
     
     suggested_exercises = []
                
     print("Debug: current_level =", current_level)
     print("Debug: goal =", goal)
     print("Debug: weight =", weight)
     

   

     

     # Rule 1
     if current_level == "beginner" and weight <= 50.0 and goal == "weight_loss" and age <= 50 and body_injury == "no":
            suggested_exercises.append("Based on your answers, here are some suggestions: Focus on a combination of cardio exercises like running, cycling, and high-intensity interval training (HIIT). Additionally, incorporate bodyweight exercises like burpees, jumping jacks, and bodyweight squats.")
            suggested_exercises.append("Ensure to maintain a calorie deficit through a balanced diet to support your weight loss goals.")
            suggested_exercises.append("Consult with a fitness professional to create a personalized workout plan based on your specific goals and fitness level.")

        
   # Rule 2
     if current_level == "beginner" and weight >= 50.0 and goal == "weight_loss" and age > 50:
            suggested_exercises.append("Based on your answers, here are some suggestions: Cardio exercises like brisk walking, jogging, and cycling will help with overall calorie burn.")
            suggested_exercises.append("Ensure to maintain a balanced diet with adequate protein intake to support muscle growth.")
            suggested_exercises.append("Consult with a fitness professional to create a personalized workout plan based on your specific goals and fitness level.")

    # Rule 3
     if current_level == "beginner" and weight <= 50.0 and goal == "muscle_gain" and age <= 50:
           suggested_exercises.append("Based on your answers, here are some suggestions: Incorporate strength training for the upper body, including exercises like bench presses, rows, and overhead presses.")
           suggested_exercises.append("Listen to your body and progress gradually, especially if you are new to fitness.")
           suggested_exercises.append("Consult with a fitness professional to create a personalized workout plan based on your specific goals and fitness level.")
     
    # Rule 4 
     if current_level == "beginner" and weight >= 50 and goal == "muscle_gain" and age >= 50:
            suggested_exercises.append("Based on your answers, here are some suggestions: Incorporate strength training with compound exercises such as squats, deadlifts, and bench presses to build overall strength.")
            suggested_exercises.append("Ensure to include both upper and lower body exercises for a balanced approach.")
            suggested_exercises.append("Consult with a fitness professional to create a personalized workout plan based on your specific goals and fitness level.")
     
    # Rule 5
     if current_level == "beginner" and weight <= 50 and goal == "general_fitness" and age <= 50:
            suggested_exercises.append("Based on your answers, here are some suggestions: For general fitness, aim for a well-rounded workout routine that includes a mix of cardio, strength training, and flexibility exercises.")
            suggested_exercises.append("Cardio exercises like running, cycling, and swimming will improve cardiovascular health and endurance.")
            suggested_exercises.append("Consult with a fitness professional to create a personalized workout plan based on your specific goals and fitness level.")
     

    # Rule 6  
     if current_level == "beginner" and weight >= 50 and goal == "general_fitness" and age >= 50:
            suggested_exercises.append("Based on your answers, here are some suggestions: aim for a well-rounded workout routine that includes a mix of cardio, strength training, and flexibility exercises.")
            suggested_exercises.append("Include flexibility exercises like yoga or static stretches to improve range of motion and prevent injuries.")
            suggested_exercises.append("Consult with a fitness professional to create a personalized workout plan based on your specific goals and fitness level.")
     
    # Rule 7
     if current_level == "beginner" and weight <= 50 and goal == "hiit" and age <= 50:
            suggested_exercises.append("Based on your answers, here are some suggestions: Full-Body Circuit: Incorporate a mix of cardio and strength exercises in a circuit format.")
            suggested_exercises.append("Running or Jogging: Improves cardiovascular health and overall fitness.")
            suggested_exercises.append("Consult with a fitness professional to create a personalized workout plan based on your specific goals and fitness level.")


     # Rule 8
     if current_level == "beginner" and weight >= 50 and goal == "hiit" and age >= 50:
            suggested_exercises.append("Based on your answers, here are some suggestions: Start with walking and gradually incorporate jogging intervals.")
            suggested_exercises.append("Jump Rope: Great for cardiovascular conditioning and coordination.")
            suggested_exercises.append("Consult with a fitness professional to create a personalized workout plan based on your specific goals and fitness level.")

    # Rule 9
     if current_level == "intermediate" and weight <= 50 and goal == "weight_loss" and age <= 50:
            suggested_exercises.append("Based on your answers, here are some suggestions: Implement progressive overload by gradually increasing the weight lifted over time to challenge your muscles.")
            suggested_exercises.append("Experiment with different rep and set ranges, including hypertrophy-focused sets (8-12 reps).")
            suggested_exercises.append("Consult with a fitness professional to create a personalized workout plan based on your specific goals and fitness level.")
     
 
    # Rule 10
     if current_level == "intermediate" and weight >= 50 and goal == "weight_loss" and age >= 50:
            suggested_exercises.append("Based on your answers, here are some suggestions: Integrate intermediate strength training techniques, such as drop sets, supersets, and pyramid sets to increase intensity.")
            suggested_exercises.append("Experiment with different training splits, focusing on specific muscle groups on different days for optimal muscle development.")
            suggested_exercises.append("Consult with a fitness professional to create a personalized workout plan based on your specific goals and fitness level.")

 
   # Rule 11     
     if current_level == "intermediate" and weight <= 50 and goal == "muscle_gain" and age <= 50:
            suggested_exercises.append("Based on your answers, here are some suggestions: Prioritize compound movements with heavy weights, including exercises like squats, deadlifts, bench presses, and overhead presses.")
            suggested_exercises.append("Focus on progressive overload in your strength training routine to continually challenge your muscles.")
            suggested_exercises.append("Consult with a fitness professional to create a personalized workout plan based on your specific goals and fitness level.")

    # Rule 12
     if current_level == "intermediate" and weight >= 50 and goal == "muscle_gain" and age >= 50:
            suggested_exercises.append("Based on your answers, here are some suggestions: Incorporate strength training exercises focusing on compound movements like squats, deadlifts, bench presses, and rows to stimulate muscle growth.")
            suggested_exercises.append("Prioritize adequate rest and recovery to allow the body to heal and adapt.")
            suggested_exercises.append("Consult with a fitness professional to create a personalized workout plan based on your specific goals and fitness level.")
   
    # Rule 13           
     if current_level == "intermediate" and weight <= 50 and goal == "general_fitness" and age <= 50:
            suggested_exercises.append("Based on your answers, here are some suggestions: Box Jumps with Weights: Add resistance for an explosive body workout.")
            suggested_exercises.append("Battle Ropes Circuit: Dynamic exercises for upper body endurance.")
            suggested_exercises.append("Consult with a fitness professional to create a personalized workout plan based on your specific goals and fitness level.")

   
   # Rule 14     
     if current_level == "intermediate" and weight >= 50 and goal == "general_fitness" and age >= 50:
            suggested_exercises.append("Based on your answers, here are some suggestions: Focus on progressive overload in your strength training routine to continually challenge your target.")
            suggested_exercises.append("Prioritize adequate rest and recovery to allow the body to heal and adapt.")
            suggested_exercises.append("Consult with a fitness professional to create a personalized workout plan based on your specific goals and fitness level.")
     

    # Rule 15
     if current_level == "intermediate" and weight <= 50 and goal == "hiit" and age <= 50:
            suggested_exercises.append("Based on your answers, here are some suggestions: Sprint Intervals: High-speed sprints with short rest periods.")
            suggested_exercises.append("Bodyweight Exercises: Push-ups, squats, lunges, and planks for a full-body workout.")
            suggested_exercises.append("Consult with a fitness professional to create a personalized workout plan based on your specific goals and fitness level.")


    # Rule 16
     if current_level == "intermediate" and weight >= 50 and goal == "hiit" and age >= 50:
            suggested_exercises.append("Based on your answers, here are some suggestions: Full-Body Circuit: Incorporate a mix of cardio and strength exercises in a circuit format.")
            suggested_exercises.append("Running or Jogging: Improves cardiovascular health and overall fitness.")
            suggested_exercises.append("Consult with a fitness professional to create a personalized workout plan based on your specific goals and fitness level.")

 
    # Rule 17 
    # note that at this stage the weight was changed as advaced rule it is undestading that the user have more knolodged  
     if current_level == "advanced" and weight <= 70 and goal == "weight_loss" and age <= 50:
            suggested_exercises.append("Based on your answers, here are some suggestions: Gradually incorporate resistance training, starting with lighter weights and higher repetitions, and progressively increasing intensity based on professional advice.")
            suggested_exercises.append("Incorporate strength training exercises focusing on compound movements like squats, deadlifts, bench presses, and rows to stimulate muscle growth.")
            suggested_exercises.append("Consult with a fitness professional to create a personalized workout plan based on your specific goals and fitness level.")
     

    # Rule 18
     if current_level == "advanced" and weight >= 70 and goal == "weight_loss" and age >= 50:
            suggested_exercises.append("Based on your answers, here are some suggestions: Focus on exercise that will use your full pontetial, such as swimming or cycling.")
            suggested_exercises.append("Pay close attention to your body's signals and modify or avoid any exercises that cause discomfort or pain.")
            suggested_exercises.append("Consult with a fitness professional to create a personalized workout plan based on your specific goals and fitness level.")


    # Rule 19       
     if current_level == "advanced" and weight <= 70 and goal == "muscle_gain" and age <= 50:
            suggested_exercises.append("Based on your answers, here are some suggestions: Bench Press: Targets chest, shoulders, and triceps.")
            suggested_exercises.append("Bent Over Barbell Rows: Targets upper back and lats, and Bent Over Barbell Rows: Targets upper back and lats.")
            suggested_exercises.append("Consult with a fitness professional to create a personalized workout plan based on your specific goals and fitness level.")


    # Rule 20
     if current_level == "advanced" and weight >= 70 and goal == "muscle_gain" and age >= 50:
            suggested_exercises.append("Based on your answers, here are some suggestions: Squats: Targets quadriceps, hamstrings, and glutes:")
            suggested_exercises.append("Squats: Targets quadriceps, hamstrings, and glutes and Pull-Ups/Chin-Ups: Targets back and biceps.")
            suggested_exercises.append("Consult with a fitness professional to create a personalized workout plan based on your specific goals and fitness level.")


    # Rule 21
     if current_level == "advanced" and weight <= 70 and goal == "general_fitness" and age <= 50:
            suggested_exercises.append("Based on your answers, here are some suggestions: Full-Body Circuit: Incorporate a mix of cardio and strength exercises in a circuit format.")
            suggested_exercises.append("Bodyweight Exercises: Push-ups, squats, lunges, and planks for a full-body workout.")
            suggested_exercises.append("Consult with a fitness professional to create a personalized workout plan based on your specific goals and fitness level.")

    
   # Rule 22      
     if current_level == "advanced" and weight >= 70 and goal == "general_fitness" and age >= 50:
            suggested_exercises.append("Based on your answers, here are some suggestions: Full-Body Circuit: Incorporate a mix of cardio and strength exercises in a circuit format.")
            suggested_exercises.append("Running or Jogging: Improves cardiovascular health and overall fitness.")
            suggested_exercises.append("Consult with a fitness professional to create a personalized workout plan based on your specific goals and fitness level.")

    # Rule 23
     if current_level == "advanced" and weight <= 70 and goal == "hiit" and age <= 50:
            suggested_exercises.append("Based on your answers, here are some suggestions: Bodyweight Exercises: Push-ups, squats, lunges, and planks for a full-body workout.")
            suggested_exercises.append("Jump Rope: Great for cardiovascular conditioning and coordination.")
            suggested_exercises.append("Consult with a fitness professional to create a personalized workout plan based on your specific goals and fitness level.")


    # Rule 24
     if current_level == "advanced" and weight >= 70 and goal == "hiit" and age >= 50:
            suggested_exercises.append("Based on your answers, here are some suggestions: Full-Body Circuit: Incorporate a mix of cardio and strength exercises in a circuit format.")
            suggested_exercises.append("Running or Jogging: Improves cardiovascular health and overall fitness.")
            suggested_exercises.append("Consult with a fitness professional to create a personalized workout plan based on your specific goals and fitness level.")
     
     return suggested_exercises
    
    
    
    def run_expert_system(self):
        self.collect_user_data()
        suggested_exercises = self.suggest_exercises()
        print("\nExercise Suggestions:")
        for suggestion in suggested_exercises:
             print(f"- {suggestion}")


if __name__ == "__main__":
    gym_expert = GymExpertSystem()
    gym_expert.run_expert_system()

    




