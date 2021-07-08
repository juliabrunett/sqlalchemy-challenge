// Select the form 
var form = d3.select("#form");

// Select the date button
var start_date_button_1 = d3.select("#start-filter-button-1");
var start_date_button_2 = d3.select("#start-filter-button-2");
var end_date_button = d3.select("#end-filter-button");


// Create event handlers for clicking the buttons & submitting the form
start_date_button_1.on("click", runEnterStart);
start_date_button_2.on("click", runEnterStartEnd);
end_date_button.on("click", runEnterStartEnd);
// form.on("submit", runEnter);

function runEnterStart() {
    // Keep the page from refreshing
    d3.event.preventDefault();

    // Select the input datetime
    var inputStartDatetime_1 = d3.select("#startDatetime-1").property("value");

    console.log(inputStartDatetime_1);
    
    // Printing Dates on Page & In console 
        console.log("Start Date Search")
        console.log("-----------------------")

        d3.select("#start-date-selection-1").text(`${inputStartDatetime_1}`);
        start_date_url = createStartEndPoint(inputStartDatetime_1);
        console.log(start_date_url);
        runSearch(start_date_url);
}

function runEnterStartEnd() {
    // Keep the page from refreshing
    d3.event.preventDefault();

    // Select the input datetime
    var inputEndDatetime = d3.select("#endDatetime").property("value");
    var inputStartDatetime_2 = d3.select("#startDatetime-2").property("value");

    // Printing Dates on Page & In console if both are selected
    if (inputEndDatetime === "") {
            d3.select("#end-date-selection").html(`<br>Select an End Date`);

    }
    else if (inputStartDatetime_2 === "") {
        d3.select("#start-date-selection-2").html(`<br>Select a Start Date`);
    }
    else {
        // Print the input date in the console
        console.log("Start & End Date Search")
        console.log("-----------------------")
        console.log("Start Date: ", inputStartDatetime_2);
        console.log("End Date: ", inputEndDatetime);

        // Add chosen input date (on page)
        d3.select("#end-date-selection").text(`${inputEndDatetime}`);
        d3.select("#start-date-selection-2").text(`${inputStartDatetime_2}`);

        full_date_url = createFullEndPoint(inputStartDatetime_2, inputEndDatetime);
        runSearch(full_date_url);
    };

    // console.log(start_date_url);
    // console.log(full_date_url);
    // return (full_date_url);
    
};

function createFullEndPoint(startDate, endDate) {
    full_date_url = `/api/v1.0/${startDate}/${endDate}`;

    return full_date_url;
};

function createStartEndPoint(startDate) {
    start_date_url = `/api/v1.0/${startDate}`;

    return start_date_url;
};

function runSearch(date_url) {
    location.href = date_url;
    
};