typeof(15)
// Prediction: number
// Actual:

typeof(5.5)
// Prediction: number
// Actual:

typeof(NaN)
// Prediction: number or more like it's not a number
// Actual:

typeof("hello")
// Prediction: string
// Actual:

typeof(true)
// Prediction: boolean
// Actual:

typeof(1 != 2)
// Prediction: boolean
// Actual:

"hamburger" + "s"
// Prediction: Nan
// Actual:

"hamburgers" - "s"
// Prediction: NaN
// Actual:

"1" + "3"
// Prediction: string
// Actual:

"1" - "3"
// Prediction: string
// Actual:

"johnny" + 5
// Prediction: null can't perform math equation beqteen
//			 a number and a string
// Actual:

"johnny" - 5
// Prediction: null can't perform math equation beqteen
//			 a number and a string
// Actual:

99 * "hello"
// Prediction: null can't perform math equation beqteen
//			 a number and a string
// Actual:

1 != 1
// Prediction: boolean
// Actual:

1 == "1"
// Prediction: null
// Actual:

1 === "1"
// Prediction: null
// Actual: