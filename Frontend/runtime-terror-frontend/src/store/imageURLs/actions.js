import axios from 'axios'
const URL = 'http://localhost:5000/'
export function fetchAllImagesURL (state) {
  var urls = []
  axios.get(URL + 'image').then(function (res) {
    for (var i in res.data) {
      var targetURL = URL + 'image/' + res.data[i].id
      var urlDetails = {
        id: res.data[i].id,
        url: targetURL,
        favorite: res.data[i].favorite
      }
      urls.push(urlDetails)
    }
    state.commit('updateIDsArray', urls)
  })
}

export function fetchFavoriteImagesURL (state) {
  var urls = []
  axios.get(URL + 'favorite').then(function (res) {
    for (var i in res.data) {
      var targetURL = URL + 'image/' + res.data[i].id
      var urlDetails = {
        id: res.data[i].id,
        url: targetURL,
        favorite: res.data[i].favorite
      }
      urls.push(urlDetails)
    }
    state.commit('updateFavoriteIDsArray', urls)
  })
}

export function filterImagesByLabel (state, label) {
  var urls = []
  if (label === 'all') {
    state.dispatch('fetchAllImagesURL')
  } else {
    axios.get(URL + 'filter', { params: { filter_by: label } }).then((res) => {
      for (var i in res.data) {
        var targetURL = URL + 'image/' + res.data[i].id
        var urlDetails = {
          id: res.data[i].id,
          url: targetURL,
          favorite: res.data[i].favorite
        }
        urls.push(urlDetails)
      }
      state.commit('updateIDsArray', urls)
    })
  }
}

export function searchImages (state, inputText) {
  var urls = []
  axios.post(URL + 'search', { text: inputText }).then((res) => {
    for (var i in res.data) {
      var targetURL = URL + 'image/' + res.data[i]
      urls.push(targetURL)
    }
    state.commit('updateIDsArray', urls)
  })
}

export function fetchAllLabels (state) {
  var labels = []
  axios.get(URL + 'labels').then((res) => {
    labels.push('all')
    for (var index in res.data) {
      labels.push(res.data[index])
    }
  })
  state.commit('updateLabelsArray', labels)
}
