let details = {
  my: 'name',
  is: 'Rudolf',
  the: 'raindeer'
}


for (let [x, value] of Object.entries(details)){

  console.log(`${x}, ${value}`)}


  console.log(details);
  //i know it's just a cheat but, the wrods are aligned for a row :-)

  for (let key in details){
    console.log(`${key} ${details[key]}`)
    console.log(details[key])
  }