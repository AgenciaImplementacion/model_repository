var callback = function(){
  // Handler when the DOM is fully loaded
  // https://www.sitepoint.com/jquery-document-ready-plain-javascript/
  console.log('loaded');
  document.body.style.opacity = '1';
};

if (
    document.readyState === 'complete' ||
    (document.readyState !== 'loading' && !document.documentElement.doScroll)
) {
  callback();
} else {
  document.addEventListener('DOMContentLoaded', callback);
}

var xmlDoc = null;
var loadXML = function () {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
          myFunction(this);
      }
  };
  xhttp.open('GET', '/ilimodels.xml', true);
  xhttp.send();

  function myFunction(xml) {
      xmlDoc = xml.responseXML;
  }
}

if (xmlDoc === null) {
  loadXML();
}

var setIliValues = function (name, title, shortDescription) {
  document.getElementById('ili-name').innerHTML = name;
  document.getElementById('ili-title').innerHTML = title;
  document.getElementById('ili-shortDescription').innerHTML = shortDescription;
}

var getValue = function (ili, tagName) {
  var tag = ili.getElementsByTagName(tagName);
  if (tag.length > 0) {
    return tag[0].innerHTML;
  }
  return '';
}

var drawInfo = function (ili) {
  var name = '<p><h5>Nombre:</h5>' + getValue(ili, 'Name') + '</p>';
  var title = '<p><h5>Título:</h5>' + getValue(ili, 'Title') + '</p>';
  var shortDescription = '<p><h5>Descripción:</h5>' + getValue(ili, 'shortDescription') + '</p>';
  setIliValues(name, title, shortDescription);
}

window.showDescription = function (ele) {
  var name = ele.dataset.name;
  var ilis = xmlDoc.getElementsByTagName('IliRepository09.RepositoryIndex.ModelMetadata');
  for (var i = 0; i < ilis.length; i++) {
    var ili = ilis[i];
    var file = ili.getElementsByTagName('File')[0];
    if (file.innerHTML === name) {
      drawInfo(ili);
      return;
    }
  }
  setIliValues('', '', '');
}
