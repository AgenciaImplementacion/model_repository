var callback = function(){
  // Handler when the DOM is fully loaded
  // https://www.sitepoint.com/jquery-document-ready-plain-javascript/
  console.log('loaded');
  document.body.style.opacity = '1';
};

if (
    document.readyState === "complete" ||
    (document.readyState !== "loading" && !document.documentElement.doScroll)
) {
  callback();
} else {
  document.addEventListener("DOMContentLoaded", callback);
}
