import random

def objective_func (x):
   return -(x**2)

def hill_function(function,start_point,step_size=0.1 ,iterration=100):
   current_point =start_point
   current_val = function(current_point)

   for i in range (iterration):
      new_point=current_point+ random.uniform(-step_size,step_size)
      new_value=function(new_point)

      if(abs(new_value)<abs(current_val)):
         current_point,current_val= new_point,new_value
         print(current_point,current_val)
   
   return( current_point,current_val)

start_point=random.uniform(-5,5)


best_point ,best_value =hill_function(objective_func,start_point)

