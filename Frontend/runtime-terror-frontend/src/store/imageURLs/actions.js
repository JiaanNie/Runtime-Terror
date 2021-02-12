import axios from 'axios'
export function setImagesURL (state) {
  const URL = 'http://localhost:5000/'
  var urls = []
  axios.get(URL + 'image').then(function (res) {
    for (var i in res.data) {
      var targetURL = URL + 'image/' + res.data[i]
      urls.push(targetURL)
    }
    state.commit('updateIDsArray', urls)
  })
}
