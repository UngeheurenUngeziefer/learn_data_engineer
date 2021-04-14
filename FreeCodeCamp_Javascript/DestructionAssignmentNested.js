const LOCAL_FORECAST = {
  today: { min: 72, max: 83 },
  tomorrow: { min: 73.3, max: 84.6 }
};

function getMaxOfTmrw(forecast) {
  'use strict';

  const { tomorrow : { max : maxOfTomorrow }} = forecast;

  return maxOfTomorrow;
}

console.log(getMaxOfTmrw(LOCAL_FORECAST));