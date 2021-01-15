// from data.js
var tableData = data;
console.log(tableData);

//Populate table with data
//Refer to tbody in table
var tbody = d3.select('tbody');

//Add a row for each UFO sighting
tableData.forEach(function(ufoSighting) {
    //Append row
    var row = tbody.append('tr');

    Object.entries(ufoSighting).forEach(function([key, value]) {
        
        console.log(key, value);
        // Append a cell to the row for each value

        var cell = row.append("td");

        //Populate the cells with the value from data
        cell.text(value);
    });
});

//Button for filter by date
var button = d3.select("#filter-btn");
button.on('click', function() {

    tbody.html('')

    //select the input
    var inputDate = d3.select("#datetime");
    var inputCity = d3.select("#city");
    var inputState = d3.select("#state");
    var inputCountry = d3.select("#country");
    var inputShape = d3.select("#shape");

    //get the value property
    var valueDate = inputDate.property("value");
    var valueCity = inputCity.property("value");
    var valueState = inputState.property("value");
    var valueCountry = inputCountry.property("value");
    var valueShape = inputShape.property("value");

    //filter the data for sightings on that date
    var filteredData = tableData.filter(sighting => sighting.datetime === valueDate)
                                .filter(sighting => sighting.city === valueCity)
                                .filter(sighting => sighting.state === valueState)
                                .filter(sighting => sighting.country === valueCountry)
                                .filter(sighting => sighting.shape === valueShape)

    //Add the data to the table using a forEach
    filteredData.forEach(function(selections) {

        console.log(selections);
        // Append one table row `tr` for each UFO Sighting object
        var row = tbody.append("tr");

        // Use `Object.entries` to console.log each UFO Sighting value
        Object.entries(selections).forEach(function([key, value]) {
            console.log(key, value);

            // Append a cell to the row for each value
            var cell = row.append("td");
            cell.text(value);

        });
    });
});

