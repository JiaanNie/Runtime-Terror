import axios from 'axios'
var headers = {
  user: ''
}
export function fetchAllImagesURL (state) {
  var urls = []
  headers.user = state.rootGetters['user/getUserUUID']
  axios.get(state.rootGetters['env/getHostURL'] + 'image', { headers }).then(function (res) {
    for (var i in res.data) {
      var targetURL = state.rootGetters['env/getHostURL'] + 'image/' + res.data[i].id
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
  axios.get(state.rootGetters['env/getHostURL'] + 'favorite', { headers }).then(function (res) {
    for (var i in res.data) {
      var targetURL = state.rootGetters['env/getHostURL'] + 'image/' + res.data[i].id
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
    axios.get(state.rootGetters['env/getHostURL'] + 'filter', { headers: headers, params: { filter_by: label } }).then((res) => {
      for (var i in res.data) {
        var targetURL = state.rootGetters['env/getHostURL'] + 'image/' + res.data[i].id
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
  axios.post(state.rootGetters['env/getHostURL'] + 'search', { text: inputText }, { headers: headers }).then((res) => {
    for (var i in res.data) {
      var targetURL = state.rootGetters['env/getHostURL'] + 'image/' + res.data[i]
      var urlDetails = {
        id: res.data[i],
        url: targetURL,
        favorite: res.data[i].favorite
      }
      urls.push(urlDetails)
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
    axios.get(state.rootGetters['env/getHostURL'] + 'labels', { headers }).then((res) => {
      labels.push('all')
      for (var index in res.data) {
        labels.push(res.data[index])
      }
      state.commit('updateLabelsArray', labels)
    })
  }
}

export function fetchSortedImages (state) {
  headers.user = state.rootGetters['user/getUserUUID']
  axios.get(state.rootGetters['env/getHostURL'] + 'sort_view', { headers }).then((res) => {
    state.commit('updateSortedImages', res.data)
  })
}
