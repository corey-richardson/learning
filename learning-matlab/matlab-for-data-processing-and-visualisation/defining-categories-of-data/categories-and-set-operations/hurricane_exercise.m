load hurricanes
data.Country = categorical(data.Country);
head(data)

%% Task 1
% Every measurement that was taken over land has been labeled with a country name (not "N/A").
% Find all the valid country names in the variable Country of the table data (values excluding
% "N/A"). Save them in the variable countryNames.
c = categories(data.Country)
countryNames = setdiff(c,"N/A")

%% Task 2
% Now that you have a list of the country names, you want to label them with the category Land.
% Merge all of the countries in data.Country to create a new category named "Land". Assign the
% result to a new variable Location in the table data.
data.Location = mergecats(data.Country,countryNames,"Land")

%% Task 3
% You can rename categories using the renamecats function.
% A = renamecats(A,oldNames,newNames)
data.Location = renamecats(data.Location,"N/A","Sea")

%% Task 4
% Create a variable, onLand that is the same size as data.Location and true everywhere the
% measurement was taken over land.
% Create a variable, onSea that is the same size as data.Location and true everywhere the
% measurement was taken over sea.
onLand = data.Location == "Land" % onland set to (is data.Location equal to "Land"
onSea = data.Location == "Sea"

%% Further Practice
scatter(data.Windspeed(onSea),data.Pressure(onSea),"b","filled");
hold on
scatter(data.Windspeed(onLand),data.Pressure(onLand),"r","filled");
hold off
xlabel("Wind Speed")
ylabel("Pressure")
legend("Sea","Land")