using InteractiveUtils

function showTypeTree(T, level=0)
    println("\t"^level, T)
    for t in subtypes(T)
        if t != Any
            showTypeTree(t, level + 1)
        end
    end
end

showTypeTree(Real)