(* Exercise: values *)
let x = 7 * (1 + 2 + 3);; (*int*)
let y = "CS " ^ string_of_int 3110;; (*string*)

(* Exercise: operators *)
let a = 42 * 10;;
let b = 3.14 *. 2.0;; (* 浮点数乘法要用*. *)
let c = 4.2 *. 4.2 *. 4.2 *. 4.2 *. 4.2 *. 4.2 *. 4.2;;

(* Exercise: equality *)
let h = 42 = 42;;
let i = ("hi" = "hi");; (*true,这个是structural equality，判断值是否相等*)
let j = ("hi" == "hi");; (*false，这个是physical equality，判断是否是同一个对象，即在内存中是否使用了相同的地址*)

(* Exercise: assert *)
assert true;; (*输出：unit = ()*)
assert false;; (*输出：Exception: Assert_failure ("//toplevel//", 1, 0).*)
assert (2110 = 3110);;

(* Exercise: if *)
let m = if 2 > 1 then 42 else 7;;

(* Exercise: double fun *)
let double x = x * 2;;
assert (double(7) = 14);;

(* Exercise: more fun *)
let cube_float x = x *. x *. x;;
let sign x = if x > 0 then 1 else (if x < 0 then -1 else 0);;
let area_circle x = 3.14 *. x *. x;;
assert (abs_float(area_circle(2.) -. 12.56) < 1e-5);;

(* Exercise: RMS *)
let root_mean_square x y = sqrt ((x *. x +. y *. y) /. 2.);;
assert ((root_mean_square 2. 4. -. 3.1622776) < 1e-5);;

(* Exercise: date fun *)
let judge_date d m = 
  match m with 
  | "Jan" | "Mar" | "May" | "Jul" | "Aug" | "Oct" | "Dec" -> if  d >= 1 && d <= 31 then true else false
  | "Feb" -> if d >= 1 && d <= 28 then true else false
  | "Apr" | "Jun" | "Sept" | "Nov" -> if d >= 1 && d <= 30 then true else false
  | _ -> false;;

(* Exercise: fib *)
let rec fib x = 
  match x with 
  | 1 -> 1
  | 2 -> 1
  | _ -> fib(x-1) + fib(x-2);;

(* Exercise: fib fast *)
let fib_fast n =
  let rec h n pp p =
    if n = 1 then p
    else h (n - 1) p (pp + p)
  in
  if n <= 0 then invalid_arg "n must be greater than 0"
  else h n 0 1;; (*为负的一个正整数n为122*)

(* Exercise: poly types *)
let f x = if x then x else x;; (*val f : bool -> bool = <fun>*)
let g x y = if y then x else x;; (*val g : 'a -> bool -> 'a = <fun>*)
let h x y z = if x then y else z;; (*let h x y z = if x then y else z;;*)
let i x y z = if x then y else y;; (*val i : bool -> 'a -> 'b -> 'a = <fun>*)

(* Exercise: divide *)
let divide ~numerator ~denominator =
  if denominator = 0.0 then
    failwith "Division by zero"
  else
    numerator /. denominator;;

(* Exercise: associativity *)
let add x y = x + y;;
let a1 = add 5 1;; (*int = 6*)
let a2 = add 5;; (*int -> int = <fun>*)
let a3 = (add 5) 1;; (*int = 6*)
(* let a4 = add (5 1);; (*ERROR*) *)

(* Exercise: average *)
let (+/.) x y = (x +. y) /. 2.;;

(* Exercise: hello world *)
print_endline "Hello world!";; (*有换行*)
print_string "Hello world!";; (*无换行*)