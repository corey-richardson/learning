x = categorical(["medium" "large" "large" "red" "small" "red" "medium"])

%% Task 1

% Find the categories in x and assign them to a variable named c.
% cats = categories(variableName);

c = categories(x)

%% Task 2

% Remove the category "red" from c and store the result in sz.
% The output should be a string.

% the setdiff function performs the set difference between the first and the second input.
% d = setdiff(a,b)

sz = setdiff(c,"red")

%% Task 3

% You can merge different categories in a categorical array.
% For example, the following command will merge the categories
% q1, q2, and q3 to a single category, q

% Merge the categories "small", "medium", and "large" that are
% contained in the variable x into a single category, size.
% Store the result back into the variable x.

% a = mergecats(a,["q1" "q2" "q3"],"q")

x = mergecats(x,["small","medium","large"],"size")

