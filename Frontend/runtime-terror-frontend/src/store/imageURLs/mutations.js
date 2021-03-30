export function updateIDsArray (state, newArray) {
  state.imageURLArray = newArray
}

export function updateFavoriteIDsArray (state, newArray) {
  state.favoriteURLArray = newArray
}

export function updateLabelsArray (state, newArray) {
  state.labels = newArray
}
export function updateSortedImages (state, sortedImages) {
  state.sortedImages = sortedImages
}
