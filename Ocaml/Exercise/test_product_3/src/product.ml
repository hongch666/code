let rec product list = 
  match list with
  | [] -> 1
  | num::l -> num * product l;;