let fifth list = 
  try
    List.nth list 4
  with
  | Failure _ -> 0;;