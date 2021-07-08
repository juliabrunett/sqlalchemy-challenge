// Select the form 
var form = d3.select("#form");

// Select the date button
var start_date_button = d3.select("#start-filter-button");
var end_date_button = d3.select("#end-filter-button");
// var search_button = d3.select("search-button");

// Create event handlers for clicking the buttons & submitting the form
start_date_button.on("click", runEnter);
end_date_button.on("click", runEnter);
// form.on("submit", runEnter);
// search_button.on("click", runSearch);

function runEnter() {
    // Keep the page from refreshing
    d3.event.preventDefault();

    // Select the input datetime
    var inputEndDatetime = d3.select("#endDatetime").property("value");
    var inputStartDatetime = d3.select("#startDatetime").property("value");

    // Printing Dates on Page & In console if both are selected
    if (inputEndDatetime === "") {
        d3.select("#end-date-selection").html(`<br>Select an End Date`);
    }
    else if (inputStartDatetime === "") {
        d3.select("#start-date-selection").html(`<br>Select a Start Date`);
    }
    else {
        // Print the input date in the console
        console.log("Start Date: ", inputStartDatetime);
        console.log("End Date: ", inputEndDatetime);

        // Add chosen input date (on page)
        d3.select("#end-date-selection").text(`${inputEndDatetime}`);
        d3.select("#start-date-selection").text(`${inputStartDatetime}`);

        full_date_url = createFullEndPoint(inputStartDatetime, inputEndDatetime);
        runSearch(full_date_url);
    }

    
    start_date_url = createStartEndPoint(inputStartDatetime);

    
    console.log(full_date_url);
    return (full_date_url);
    
};

function createFullEndPoint(startDate, endDate) {
    full_date_url = `/api/v1.0/${startDate}/${endDate}`;

    return full_date_url;
};

function createStartEndPoint(startDate) {
    start_date_url = `/api/v1.0/${startDate}`;

    return start_date_url;
};

function runSearch(full_date_url) {
    location.href = full_date_url;
}