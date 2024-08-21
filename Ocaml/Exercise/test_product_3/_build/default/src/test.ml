open OUnit2
open Product

let tests = "test suite for sum" >::: [
  "empty" >:: (fun _ -> assert_equal 1 (product []) ~printer:string_of_int);
  "singleton" >:: (fun _ -> assert_equal 2 (product [2]) ~printer:string_of_int);
  "two_elements" >:: (fun _ -> assert_equal 6 (product [2; 3]) ~printer:string_of_int);
]

let _ = run_test_tt_main tests