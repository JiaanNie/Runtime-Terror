import axios from 'axios'
const URL = 'http://localhost:5000/'
export function fetchAllImagesURL (state) {
  var urls = []
  axios.get(URL + 'image').then(function (res) {
    for (var i in res.data) {
      var targetURL = URL + 'image/' + res.data[i]
      var urlDetails = {
        id: res.data[i],
        url: targetURL
      }
      urls.push(urlDetails)
    }
    state.commit('updateIDsArray', urls)
  })
}

export function fetchFavoriteImagesURL (state) {
  var urls = []
  axios.get(URL + 'image').then(function (res) {
    for (var i in res.data) {
      var targetURL = URL + 'image/' + res.data[i]
      urls.push(targetURL)
    }
    state.commit('updateIDsArray', urls)
  })
}

export function filterImagesByLabel (state, label) {
  console.log('in filterImagesByLabel action js file')
  var urls = []
  if (label === 'all') {
    state.dispatch('fetchAllImagesURL')
  } else {
    axios.get(URL + 'filter', { params: { filter_by: label } }).then((res) => {
      for (var i in res.data) {
        var targetURL = URL + 'image/' + res.data[i]
        urls.push(targetURL)
      }
      state.commit('updateIDsArray', urls)
    })
  }
}

export function searchImages (state, inputText) {
  console.log(inputText)
  var urls = []
  axios.post(URL + 'search', { text: inputText }).then((res) => {
    for (var i in res.data) {
      var targetURL = URL + 'image/' + res.data[i]
      urls.push(targetURL)
    }
    state.commit('updateIDsArray', urls)
  })
}
