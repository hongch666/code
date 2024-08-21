let sort_desc list = 
  let sorted_list = List.sort Stdlib.compare list in
  List.rev sorted_list;;