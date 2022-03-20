    let c;
    let a = 34;
    let b = 21;

    console.log(a+b) //first expression
    // Prediction: 55
    // Actual:55

    a = 2;

    console.log(a+b) //second expression
    // Prediction: 23
    // Actual:23

    console.log(3 + 4 + '5');
    //well the out come should be the number 3 plus the number 4, 
    //however we are adding a string to the calculations 
    //meaning that i don't think the outcome will present anything
    //but an error

    // ok so after running it in the browser i see that the calculations
    //were performed but the number presented on the screen is 75 
    //because the string (`5`) was printed as is and added to the 
    //end of the line which in this case was immediatly after the calculations result