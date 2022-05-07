// import request from "./node_modules/request";
// const request = require('request');
let channelId = "";
let listTitle = [];
let listId = [];
let ListVideosURL = {};
let videoId = [];
let html_temp = ``;
const APIKey = "AIzaSyAGIfKa_suSp7vJ2rC1CyApCaDWFYZYwjE";

function getChannelId(name, APIKey) {
  $.ajax({
    type: "GET",
    url: "https://www.googleapis.com/youtube/v3/search?",
    data: { part: "snippet", key: APIKey, type: "video", q: name },
    success: function (response) {
      channelId = response.items[0].snippet.channelId;
      // console.log("Channel-Id : "+ channelId+" \nAPIKEy : "+ APIKey);
      getChannelLists(channelId, APIKey);
    },
  });
}

function getChannelLists(channelId, APIKey) {
  $.ajax({
    type: "GET",
    url: "https://www.googleapis.com/youtube/v3/playlists?",
    data: {
      part: "snippet",
      channelId: channelId,
      key: APIKey,
      type: "playlist",
      maxResults: 500,
    },
    success: function (response) {
      let playListLength = response.pageInfo.totalResults;
      for (let i = 0; i < playListLength; i++) {
        listTitle.push(response.items[i].snippet.title);
        listId.push(response.items[i].id);
      }
      getVideos();
    },
  });
}

function getVideos() {
  for (let i = 0; i < listId.length; i++) {
    $.ajax({
      type: "GET",
      url: "https://www.googleapis.com/youtube/v3/playlistItems?",
      data: {
        part: "snippet",
        playlistId: listId[i],
        key: APIKey,
        maxResults: 500,
      },

      success: function (response) {
        let data = response;
        let temp_listTitle = `<div class=${'newDiv'+[i]}><h1>${listTitle[i]}</h1></div>`
        console.log(temp_listTitle);
        $(".titleBox").append(temp_listTitle); 
        for (let j = 0; j < data.pageInfo.totalResults; j++) {
          videoId.push(data.items[j].snippet.resourceId.videoId);
          ListVideosURL = "https://www.youtube.com/embed/" + videoId[j];
          html_temp = `<iframe width="448" height="252" src=${ListVideosURL} id=${[j]} title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>`;
          console.log(html_temp);
          $(".newDiv"+[i]).append(html_temp)
        }
        videoId = [];
      },
    });
  }
}


const btnsTip = document.querySelectorAll(".btn");
let channelName = "";

btnsTip.forEach((btnTip) => {
  btnTip.addEventListener("click", (e) => {
    if (channelName !== ""){
      window.location.reload();
      channelName= e.currentTarget.innerHTML;
      console.log(e.currentTarget.innerHTML);
      getChannelId(channelName, APIKey);
    }else{
    channelName= e.currentTarget.innerHTML;
    console.log(e.currentTarget.innerHTML);
    // getChannelLists("UC1B6SalAoiJD7eHfMUA9QrA", "AIzaSyBBdv-GASLz2o5tf10FBwoNQIP1oqtwVSI");
    getChannelId(channelName, APIKey);}
  });
});







