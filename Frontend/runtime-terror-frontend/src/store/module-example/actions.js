export function setImagesURL (state, newArray) {
  console.log("in action js")
  state.commit('updateIDsArray', newArray)
}
