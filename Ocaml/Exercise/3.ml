(* Exercise: list expressions *)
let l1 = [1;2;3;4;5];;
let l2 = 1::2::3::4::5::[];;
let l3 = [1]@[2;3;4]@[5];;

(* Exercise: product *)
let rec product list = 
  match list with
  | [] -> 1
  | num::l -> num * product l;;

(* Exercise: concat *)
let rec concat list = 
  match list with
  | [] -> ""
  | s::l -> s ^ concat l;;

(* Exercise: product test *)
(* In the folder test_product_3. *)

(* Exercise: patterns *)
let function1 list = 
  match list with 
  | "bigred"::_ -> true
  | _ -> false;;

let function2 list =
  match list with
  | _::_::[] -> true
  | _::_::_::_::[] -> true
  | _ -> false;;

let function3 list =
  match list with
  | x::y::_ when x = y -> true
  |_ -> false;;

(* Exercise: library *)
let fifth list = 
  try
    List.nth list 4
  with
  | Failure _ -> 0;;

let sort_desc list = 
  let sorted_list = List.sort Stdlib.compare list in
  List.rev sorted_list;;

(* Exercise: library test *)
(* In the folder test_library_3 and test_library1_3. *)

(* Exercise: library puzzle *)
let last_element lst =
  List.hd (List.rev lst)

let any_zeros lst =
  List.exists (fun x -> x = 0) lst;;

(* Exercise: take drop *)
let rec take n list = 
  match n,list with
  | 0,_ -> []
  | _,[] -> []
  | _,x::l -> x::take(n-1) l;;

let rec drop n list = 
  match n,list with
  | 0,_ -> list
  | _,[] -> []
  | _,x::l -> drop(n-1) l;;

(* Exercise: take drop tail *)
let rec take_tail n list acc =
  match n, list with
  | 0, _ -> acc
  | _, [] -> acc
  | _, x::l -> take_tail (n-1) l (x::acc)
;;

let rec drop n list = 
  match n,list with
  | 0,_ -> list
  | _,[] -> []
  | _,x::l -> drop(n-1) l;;

(* Exercise: unimodal *)
(* Helper function to determine if the list is strictly increasing *)
  let rec is_increasing = function
| [] | [_] -> true
| a1 :: (a2 :: _ as tl) when a1 <= a2 -> is_increasing tl
| _ -> false

(* Helper function to determine if the list is strictly decreasing *)
let rec is_decreasing = function
| [] | [_] -> true
| a1 :: (a2 :: _ as tl) when a1 >= a2 -> is_decreasing tl
| _ -> false

(* Function to check if a list is unimodal *)
let is_unimodal lst =
let rec split_increasing_decreasing = function
  | [] | [_] as l -> l, []
  | x1 :: (x2 :: _ as tl) when x1 <= x2 ->
      let inc, dec = split_increasing_decreasing tl in
      (x1 :: inc), dec
  | rest -> [], rest
in
let inc, dec = split_increasing_decreasing lst in
(* Check if the remaining list is strictly decreasing *)
is_decreasing dec

(* Test cases *)
let () =
  assert (is_unimodal [] = true); (* Empty list *)
  assert (is_unimodal [1] = true); (* Single element list *)
  assert (is_unimodal [1; 2; 3] = true); (* Strictly increasing *)
  assert (is_unimodal [3; 2; 1] = true); (* Strictly decreasing *)
  assert (is_unimodal [1; 2; 3; 2; 1] = true); (* Unimodal with peak *)
  assert (is_unimodal [1; 2; 3; 2; 1; 0] = true); (* Unimodal with peak and flat end *)
  assert (is_unimodal [3; 3; 2; 2; 1] = true); (* Flat peak *)
  assert (is_unimodal [1; 1; 1; 1] = true); (* Constant list *)
  assert (is_unimodal [1; 3; 3; 3; 2; 1] = true); (* Peak with flat sections *)
  assert (is_unimodal [1; 2; 3; 4; 5] = true); (* Strictly increasing (no decreasing part) *)
  assert (is_unimodal [5; 4; 3; 2; 1] = true); (* Strictly decreasing (no increasing part) *)
  assert (is_unimodal [1; 2; 3; 4; 3; 2; 1; 0] = true); (* Complex unimodal list *)
  assert (is_unimodal [1; 2; 3; 4; 3; 2; 3; 1; 0] = false); (* Invalid unimodal list *)

  print_endline "All test cases passed!"

(* Exercise: powerset *)
let rec powerset = function
| [] -> [[]] (* 空集的幂集仅包含一个空集 *)
| x :: xs ->
  let p = powerset xs in
  let add_x_to_subsets subset = x :: subset in
  let with_x = List.map add_x_to_subsets p in
  p @ with_x (* 合并不包含x的子集和包含x的子集 *);;

(* Exercise: print int list rec *)
let rec print_int_list = function
| [] -> ()
| h :: t -> print_endline (string_of_int h); print_int_list t;;

(* Exercise: print int list iter *)
let print_int_list' lst =
  List.iter (fun x -> print_endline (string_of_int x)) lst;;

(* Exercise: student *)
type student = { first_name : string; last_name : string; gpa : float };;

let get_name student = student.first_name, student.last_name;;

let student_new first last gpa = { first_name = first; last_name = last; gpa = gpa};;

(* Exercise: pokerecord *)
type poketype = Normal | Fire | Water;;

type pokemon = { name : string; hp : int; ptype : poketype };;

let charizard = { name = "charizard"; hp = 78; ptype = Fire };;
let squirtle = { name = "squirtle"; hp = 44; ptype = Water };;

(* Exercise: safe hd and tl *)
let safe_hd list =
  match list with
  | [] -> None
  | x::l -> Some(x);;

let safe_tl list =
  match list with
  | [] -> None
  | _ -> Some(List.hd (List.rev list));;

(* Exercise: pokefun *)
let pokefun list = 
  match list with
  | [] -> None
  | _ -> Some(List.fold_left (fun max_rec r ->
    if r.hp>max_rec.hp then r else max_rec
    ){ hp = -1;name="";ptype=Fire} list);;

(* Exercise: date before *)
let is_before (y1, m1, d1) (y2, m2, d2) =
  if y1 < y2 then true
  else if y1 = y2 && m1 < m2 then true
  else if y1 = y2 && m1 = m2 && d1 < d2 then true
  else false;;

(* Exercise: earliest date *)
let earliest dates =
  match dates with
  | [] -> None
  | d :: ds ->
    let rec find_earliest current_earliest = function
      | [] -> Some current_earliest
      | h :: t ->
        if is_before h current_earliest then
          find_earliest h t
        else
          find_earliest current_earliest t
    in
    find_earliest d ds
;;

(* Exercise: assoc list *)
(** [insert k v lst] is an association list that binds key [k] to value [v]
    and otherwise is the same as [lst] *)
let insert k v lst = (k, v) :: lst;;

(** [lookup k lst] is [Some v] if association list [lst] binds key [k] to
    value [v]; and is [None] if [lst] does not bind [k]. *)
let rec lookup k = function
  | [] -> None
  | (k', v) :: t -> if k = k' then Some v else lookup k t;;

let d = [("rectangle", 4); ("nonagon", 9); ("icosagon", 20)];;

insert (("haha",3),d);;
lookup "haha" d;;

(* Exercise: cards *)
(* 定义四种花色 *)
type suit = Club | Diamond | Heart | Spade;;

(* 定义牌的等级，这里使用variant类型 *)
type rank = 
  | Two
  | Three
  | Four
  | Five
  | Six
  | Seven
  | Eight
  | Nine
  | Ten
  | Jack
  | Queen
  | King
  | Ace;;

(* 定义一张卡片，使用record类型存储花色和等级 *)
type card = { suit : suit; rank : rank };;

(* 定义几张牌的实例 *)
let ace_of_clubs = { suit = Club; rank = Ace };;
let queen_of_hearts = { suit = Heart; rank = Queen };;
let two_of_diamonds = { suit = Diamond; rank = Two };;
let seven_of_spades = { suit = Spade; rank = Seven };;

(* Exercise: matching *)
[None; Some 1; Some 2];;
[Some 1234; None];;
[None];;
[Some 1];;
(* 这个没有不匹配的非空列表 *)

(* Exercise: quadrant *)
type quad = I | II | III | IV;;
type sign = Neg | Zero | Pos;;

let sign (x:int) : sign =
  if x>0 then Pos else if x<0 then Neg else Zero;;

let quadrant : int*int -> quad option = fun (x,y) ->
  match sign(x),sign(y) with
    | Pos,Pos -> Some I
    | Neg,Pos -> Some II
    | Neg,Neg -> Some III
    | Pos,Neg -> Some IV
    | _ -> None;;

(* Exercise: quadrant when *)
let quadrant_when : int*int -> quad option = fun (x,y) ->
  match (x,y) with
    | (x,y) when sign(x)=Pos && sign(y)=Pos -> Some I
    | (x,y) when sign(x)=Neg && sign(y)=Pos -> Some II
    | (x,y) when sign(x)=Neg && sign(y)=Neg -> Some III
    | (x,y) when sign(x)=Pos && sign(y)=Neg -> Some IV
    | _ -> None;;

(* Exercise: depth *)
type 'a tree =
| Leaf
| Node of 'a * 'a tree * 'a tree;;

let rec depth : 'a tree -> int = function
  | Leaf -> 0
  | Node(_, left, right) ->
    1 + max (depth left) (depth right);;

let rec same_shape (t1 : 'a tree) (t2 : 'b tree) : bool =
  match t1, t2 with
  | Leaf, Leaf -> true
  | Node (_, l1, r1), Node (_, l2, r2) -> same_shape l1 l2 && same_shape r1 r2
  | _, _ -> false;;

(* Exercise: list max exn *)
let list_max lst =
  try
    List.fold_left max (List.hd lst) (List.tl lst)
  with
  | Failure _ -> raise (Failure "list_max");;

(* Exercise: list max exn string *)
let list_max lst =
  try
    string_of_int (List.fold_left max (List.hd lst) (List.tl lst))
  with
  | Failure _ -> "empty";;

(* Exercise: is_bst *)
(* 定义树的结构 *)
type ('a, 'b) tree =
  | Empty
  | Node of ('a * 'b) * ('a, 'b) tree * ('a, 'b) tree

(* 定义辅助函数的返回类型 *)
type 'a bst_result =
  | BstEmpty
  | Valid of 'a * 'a
  | Invalid

(* 辅助函数：检查是否为有效的BST，并返回最小和最大值 *)
let rec check_bst = function
  | Empty -> BstEmpty
  | Node ((key, _), left, right) ->
      match check_bst left, check_bst right with
      | Invalid, _ | _, Invalid -> Invalid
      | BstEmpty, BstEmpty -> Valid (key, key)
      | Valid (lmin, lmax), BstEmpty when lmax <= key -> Valid (lmin, key)
      | BstEmpty, Valid (rmin, rmax) when key <= rmin -> Valid (key, rmax)
      | Valid (lmin, lmax), Valid (rmin, rmax) when lmax <= key && key <= rmin ->
          Valid (lmin, rmax)
      | _ -> Invalid

(* 主函数：检查是否为BST *)
let is_bst tree =
  match check_bst tree with
  | Invalid -> false
  | _ -> true

(* Exercise: quadrant poly *)
type 'a quadrant =
  | Origin
  | Q1 of 'a * 'a
  | Q2 of 'a * 'a
  | Q3 of 'a * 'a
  | Q4 of 'a * 'a

let quadrant_of_point (x, y) =
  match x, y with
  | 0, 0 -> Origin
  | x, y when x > 0 && y > 0 -> Q1 (x, y)
  | x, y when x < 0 && y > 0 -> Q2 (x, y)
  | x, y when x < 0 && y < 0 -> Q3 (x, y)
  | x, y when x > 0 && y < 0 -> Q4 (x, y)
  | _ -> failwith "Unexpected point on axis"
;;

type 'a quad =
  | I : 'a quad
  | II : 'a quad
  | III : 'a quad
  | IV : 'a quad

type 'a sign =
  | Neg : 'a sign
  | Zero : 'a sign
  | Pos : 'a sign

let sign (x:'a) : 'a sign =
  if x > 0 then Pos else if x < 0 then Neg else Zero;;

let quadrant : 'a*'a -> 'a quad option = fun (x,y) ->
  match sign x, sign y with
    | Pos, Pos -> Some I
    | Neg, Pos -> Some II
    | Neg, Neg -> Some III
    | Pos, Neg -> Some IV
    | _ -> None;;