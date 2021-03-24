import axios from 'axios'
const URL = 'http://localhost:5000/'
var headers = {
  user: 'abc wilson test'
}
export function fetchAllImagesURL (state) {
  var urls = []
  headers.user = state.rootGetters['user/getUserUUID']
  axios.get(URL + 'image', { headers }).then(function (res) {
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
  headers.user = state.rootGetters['user/getUserUUID']
  axios.get(URL + 'favorite', { headers }).then(function (res) {
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
  headers.user = state.rootGetters['user/getUserUUID']
  if (label === 'all') {
    state.dispatch('fetchAllImagesURL')
  } else {
    axios.get(URL + 'filter', { headers: headers, params: { filter_by: label } }).then((res) => {
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
  headers.user = state.rootGetters['user/getUserUUID']
  axios.post(URL + 'search', { text: inputText }).then((res) => {
    for (var i in res.data) {
      var targetURL = URL + 'image/' + res.data[i]
      urls.push(targetURL)
    }
    console.log(urls)
    state.commit('updateIDsArray', urls)
  })
}

export function fetchAllLabels (state) {
  var labels = []
  headers.user = state.rootGetters['user/getUserUUID']
  if (headers.user === '') {
    this.$router.push('/')
  } else {
    axios.get(URL + 'labels', { headers }).then((res) => {
      labels.push('all')
      for (var index in res.data) {
        labels.push(res.data[index])
      }
      state.commit('updateLabelsArray', labels)
    })
  }
}
