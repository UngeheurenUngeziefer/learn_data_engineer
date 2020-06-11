var voxel = {x: 3.6, y: 7.4, z: 6.54};

var x = voxel.x;
var y = voxel.y;
var z = voxel.z;

const { x : a, y : b, z : c } = voxel;

const AVG_TEMPERATURES = {
  today: 77.5,
  tomorrow: 79
};

function getTempOfTmrw(avgTemperatures) {
  'use strict';
  const { tomorrow : tempOfTomorrow } = avgTemperatures;
  return tempOfTomorrow;
}

console.log(getTempOfTmrw(AVG_TEMPERATURES));
