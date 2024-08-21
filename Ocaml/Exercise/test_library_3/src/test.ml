open OUnit2
open Fifth

let tests = "test suite for sum" >::: [
  "empty" >:: (fun _ -> assert_equal 0 (fifth []) ~printer:string_of_int);
  "singleton" >:: (fun _ -> assert_equal 5 (fifth [1;2;3;4;5]) ~printer:string_of_int);
  "two_elements" >:: (fun _ -> assert_equal 6 (fifth [2;3;4;1;6;3]) ~printer:string_of_int);
]

let _ = run_test_tt_main tests