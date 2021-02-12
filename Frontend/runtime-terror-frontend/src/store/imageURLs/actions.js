import axios from 'axios'
const URL = 'http://localhost:5000/'
export function setImagesURL (state) {
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
  axios.get(URL + 'filter', { params: { filter_by: label } }).then((res) => {
    for (var i in res.data) {
      var targetURL = URL + 'image/' + res.data[i]
      urls.push(targetURL)
    }
    state.commit('updateIDsArray', urls)
  })
}
