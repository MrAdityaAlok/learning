// Package weather implements functions to forcast weather conditions.
package weather

// CurrentCondition stores current weather condition.
var CurrentCondition string

// CurrentLocation stores current location.
var CurrentLocation string

// Forecasts weather condition.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
