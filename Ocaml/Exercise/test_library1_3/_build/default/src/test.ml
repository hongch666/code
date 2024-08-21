open OUnit2
open Sorted_desc

let string_of_int_list l =
  List.map string_of_int l |> String.concat " "

let tests = "test suite for sort_desc" >::: [
  "empty list" >:: (fun _ -> 
    assert_equal [] (sort_desc []) ~printer:string_of_int_list);
  "singleton list" >:: (fun _ ->
    assert_equal [1] (sort_desc [1]) ~printer:string_of_int_list);
  "two_elements list" >:: (fun _ ->
    assert_equal [3; 2; 1] (sort_desc [1; 3; 2]) ~printer:string_of_int_list);
  "larger list" >:: (fun _ ->
    assert_equal [8; 5; 4; 2; 1] (sort_desc [5; 1; 4; 2; 8]) ~printer:string_of_int_list);
]

let _ = run_test_tt_main tests
(* 测试函数 *)
(* let test  =
  assert (sort_desc [1; 3; 2] = [3; 2; 1]);
  assert (sort_desc [5; 1; 4; 2; 8] = [8; 5; 4; 2; 1]);
  assert (sort_desc [] = []);
  assert (sort_desc [3] = [3]);

let _ = run_test_tt_main test *)