$(document).ready(function() {
    var item, tile, author, publisher, bookLink, bookImg;
    var outputList = document.getElementById("list-output");
    var bookUrl = "https://www.googleapis.com/books/v1/volumes?q=";
    var apiKey = "key=AIzaSyDtXC7kb6a7xKJdm_Le6_BYoY5biz6s8Lw";
    var placeHldr = '<img src="https://via.placeholder.com/150">';
    var searchData;
  
    //listener for search button
    $("#search").click(function() {
      outputList.innerHTML = ""; //empty html output
      document.body.style.backgroundImage = "url('')";
       searchData = $("#search-box").val();
       //handling empty search input field
       if(searchData === "" || searchData === null) {
         displayError();
       }
      else {
         // console.log(searchData);
         // $.get("https://www.googleapis.com/books/v1/volumes?q="+searchData, getBookData()});
         $.ajax({
            url: bookUrl + searchData,
            dataType: "json",
            success: function(response) {
              console.log(response)
              if (response.totalItems === 0) {
                alert("no result!.. try again")
              }
              else {
                $("#title").animate({'margin-top': '5px'}, 1000); //search box animation
                $(".book-list").css("visibility", "visible");
                displayResults(response);
              }
            },
            error: function () {
              alert("Something went wrong.. <br>"+"Try again!");
            }
          });
        }
        $("#search-box").val(""); //clearn search box
     });
  
     /*
     * function to display result in index.html
     * @param response
     */
     function displayResults(response) {
        for (var i = 0; i < response.items.length; i+=2) {
          item = response.items[i];
          title1 = item.volumeInfo.title;
          author1 = item.volumeInfo.authors;
          publisher1 = item.volumeInfo.publisher;
          bookLink1 = item.volumeInfo.previewLink;
          bookIsbn = item.volumeInfo.industryIdentifiers[i].identifier
          bookImg1 = (item.volumeInfo.imageLinks) ? item.volumeInfo.imageLinks.thumbnail : placeHldr ;
  
          item2 = response.items[i+1];
          title2 = item2.volumeInfo.title;
          author2 = item2.volumeInfo.authors;
          publisher2 = item2.volumeInfo.publisher;
          bookLink2 = item2.volumeInfo.previewLink;
          bookIsbn2 = item2.volumeInfo.industryIdentifiers[1].identifier
          bookImg2 = (item2.volumeInfo.imageLinks) ? item2.volumeInfo.imageLinks.thumbnail : placeHldr ;
  
          // in production code, item.text should have the HTML entities escaped.
          outputList.innerHTML += '<div class="row mt-4">' +
                                  formatOutput(bookImg1, title1, author1, publisher1, bookLink1, bookIsbn) +
                                  formatOutput(bookImg2, title2, author2, publisher2, bookLink2, bookIsbn2) +
                                  '</div>';
  
          console.log(outputList);
        }
     }
  
     function formatOutput(bookImg, title, author, publisher, bookLink, bookIsbn) {
       // console.log(title + ""+ author +" "+ publisher +" "+ bookLink+" "+ bookImg)
       var viewUrl = 'book.html?isbn='+bookIsbn;
       var htmlCard = `
       
       <a href="${viewUrl}">
       <div class="col-lg-2 col-md-4 col-sm-6">
        <div class="panel panel-default userlist">
          <div class="panel-body text-center">
            <div class="userprofile">
              <div class="userpic"> <img src="${bookImg}" alt="Sorry Image not available" class="userpicimg"> </div>
              <h3 class="username">${title}</h3>
            </div>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum tincidunt est vitae ultrices accumsan. Aliquam ornare lacus adipiscing, posuere.<br></p>
            </div>
          <div class="panel-footer"> <a href="${viewUrl}" class="btn btn-link"> Get E-Book </div>
        </div>
      </div>
      </a>`
       return htmlCard;
     }

     function displayError() {
       alert("search term can not be empty!")
     }
  
  });
  
