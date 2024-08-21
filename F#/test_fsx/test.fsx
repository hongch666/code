// Define a type to represent a financial transaction
type Transaction = {
    Description: string
    Amount: decimal
    Date: System.DateTime
}

// Define a module for budget management
module BudgetManager =

    // Function to calculate the total amount of transactions
    let calculateTotal (transactions: Transaction list) =
        transactions
        |> List.sumBy (fun t -> t.Amount)

    // Function to filter transactions by month
    let filterByMonth (month: int) (transactions: Transaction list) =
        transactions
        |> List.filter (fun t -> t.Date.Month = month)

    // Function to display transactions
    let displayTransactions (transactions: Transaction list) =
        transactions
        |> List.iter (fun t -> printfn "%s: %M on %s" t.Description t.Amount (t.Date.ToShortDateString()))

// Create a list of sample transactions
let transactions = [
    { Description = "Salary"; Amount = 3000m; Date = System.DateTime(2024, 7, 1) }
    { Description = "Groceries"; Amount = -150m; Date = System.DateTime(2024, 7, 5) }
    { Description = "Rent"; Amount = -1200m; Date = System.DateTime(2024, 7, 10) }
    { Description = "Electricity Bill"; Amount = -100m; Date = System.DateTime(2024, 7, 15) }
    { Description = "Gym Membership"; Amount = -50m; Date = System.DateTime(2024, 7, 20) }
]

// Calculate total expenses
let total = BudgetManager.calculateTotal transactions
printfn "Total amount: %M" total

// Filter and display transactions for the month of July
printfn "Transactions for July:"
let julyTransactions = BudgetManager.filterByMonth 7 transactions
BudgetManager.displayTransactions julyTransactions
