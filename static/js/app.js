// Select the form 
var form = d3.select("#form");

// Select the date buttons
var start_date_button_1 = d3.select("#start-filter-button-1");
// var start_date_button_2 = d3.select("#start-filter-button-2");
var end_date_button = d3.select("#end-filter-button");

// Create event handlers for clicking the buttons & submitting the form
start_date_button_1.on("click", runEnterStart);
// start_date_button_2.on("click", runEnterStartEnd);
end_date_button.on("click", runEnterStartEnd);
// form.on("submit", runEnter);

// var input = new Date("2014-01-01");
// var date = input.getTime();
// var year = input.getUTCFullYear();
// var day = input.getUTCDate();
// var month = input.getUTCMonth() + 1;
// console.log(year);
// console.log(day);
// console.log(month);

function runEnterStart() {
    // Keep the page from refreshing
    d3.event.preventDefault();

    // Select the input datetime
    var inputStartDatetime_1 = d3.select("#startDatetime-1").property("value");
    
    var inputStartDate = new Date(inputStartDatetime_1);
    var start_date_validation = validateDate(inputStartDate);
    console.log("Start Date Valid: ", start_date_validation);

    if (start_date_validation === true) {
        // Printing Dates on Page & In console 
        console.log("Start Date Search")
        console.log("-----------------------")
        console.log("Start Date: ", inputStartDatetime_1);

        // Append start date to page
        d3.select("#start-date-selection-1").text(`${inputStartDatetime_1}`);

        // Call function to get the endpoint
        start_date_url = createStartEndPoint(inputStartDatetime_1);
        // Run search function
        // runSearch(start_date_url);
    }
    else {
        d3.select("#start-date-selection-1").html(`<br>Enter a Valid Date`);
    }

};

function runEnterStartEnd() {
    // Keep the page from refreshing
    d3.event.preventDefault();

    // Select the input datetime
    var inputEndDatetime = d3.select("#endDatetime").property("value");
    var inputStartDatetime_2 = d3.select("#startDatetime-2").property("value");

    var inputEndDate = new Date(inputEndDatetime);
    var inputStartDate = new Date(inputStartDatetime_2);
    // var end_date = inputEndDate.getUTCTime();
    // console.log(date);

    var end_date_validation = validateDate(inputEndDate);
    var start_date_validation = validateDate(inputStartDate);

    console.log("End Date Valid: ", end_date_validation);
    console.log("Start Date Valid: ", start_date_validation);


    if (inputEndDatetime < inputStartDatetime_2) {
        d3.select("#end-date-selection").html(`<br>Date Cannot be Before Start Date`);
    }
    else if (end_date_validation === true && start_date_validation === true) {
    
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

            // Call function to get the endpoint
            full_date_url = createFullEndPoint(inputStartDatetime_2, inputEndDatetime);
            // Run search button
            // runSearch(full_date_url);
        };
    }
    else if (end_date_validation === false) {
        d3.select("#end-date-selection").html(`<br>Enter a Valid Date`);
    }
    else if (start_date_validation === false) {
        d3.select("#start-date-selection-2").html(`<br>Enter a Valid Date`);
    };
};

// Function to create the full endpoint from chosen dates
function createFullEndPoint(startDate, endDate) {
    full_date_url = `/api/v1.0/${startDate}/${endDate}`;

    return full_date_url;
};

// Function to create the endpoint from chosen start date
function createStartEndPoint(startDate) {
    start_date_url = `/api/v1.0/${startDate}`;

    return start_date_url;
};

// Function to run search
function runSearch(date_url) {
    location.href = date_url;
};

function validateDate(inputDate) {
    
    // Initialize validation variable
    var date_validation = false;

    var year = inputDate.getUTCFullYear();
    var day = inputDate.getUTCDate();
    var month = inputDate.getUTCMonth() + 1;

    if (year > 2017 || year < 2010) {
        date_validation = false;
    }
    else if (year === 2017){
        if (month > 8) {
            date_validation = false;
        }
        else if (month < 8 && month >= 1) {
            if (day > 23 && month === 8) {
                date_validation = false;
            };
        };
    }
    else {
        if (month > 12 || month < 1) {
            date_validation = false;
        }
        else if (month === 1 || month === 3 || month === 5 || month === 7 || month === 8 || month === 10 || month === 12 ) {
            if (day > 31 || day < 1) {
                date_validation = false;
            }
            else if (day <= 31 && day >= 1) {
                date_validation = true;
            };
        }
        else if (month === 4 || month === 6 || month === 9 || month === 11) {
            if (day > 30 || day < 1) {
                date_validation = false;
            }
            else if (day <= 30 && day >= 1)  {
                date_validation = true;
            };
        }
        else if (month === 2) {
            if ((year % 100 !== 0 && year % 4 === 0) || year % 400 === 0) {
                if (day > 29 || day < 1) {
                    date_validation = false;
                } 
                else if (day <= 29 && day >= 1) {
                    date_validation = true;
                };
            }
            else {
                if (day > 28 || day < 1) {
                    date_validation = false;
                } 
                else if (day <= 28 && day >= 1) {
                    date_validation = true;
                };
            };
        }
}
    return date_validation;
}