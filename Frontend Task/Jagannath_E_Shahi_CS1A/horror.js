async function hehe() {
   
    var k = document.getElementById("con");
    
    
      var data = await fetch("https://www.googleapis.com/books/v1/volumes?q=subject:Horror&startIndex=0&maxResults=30");
      const response =  await data.json();
   for (var i = 0; i < response.items.length; i+=1) {
   
      
      
    var item = response.items[i];
    var bookImg= item.volumeInfo.imageLinks.smallThumbnail;
    var title = response.items[i].volumeInfo.title;
    var lnk = item.volumeInfo.infoLink;
    var htmlcard= `
    <div class="box">
         <div class="image">
         <a href="${lnk}">
           <div class="pic"> <img src="${bookImg}" alt="Sorry Image not available" class="picimg"> </div></a>
           <h3 class="name">${title}</h3>
         </div>
         <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum tincidunt est vitae ultrices accumsan. Aliquam ornare lacus adipiscing, posuere.<br></p>
     </div>
    `;
    k.innerHTML+= htmlcard;

   }

  
  };
    /* Sets the width of the sidebar 
to 250 and the left margin of the 
page content to 250 */
function openNav() {
  document.getElementById(
    "sidebar").style.width = "250px";
 
}

/* Set the width of the sidebar 
to 0 and the left margin of the 
page content to 0 */
function closeNav() {
  document.getElementById(
    "sidebar").style.width = "0";
  document.getElementById(
    "main").style.marginLeft = "0";
}
async function hehehe() {
   
    var k = document.getElementById("con");
    
    var qr= document.getElementById("search").value;
      var data = await fetch("https://www.googleapis.com/books/v1/volumes?q="+qr+"&startIndex=0&maxResults=30");
      const response =  await data.json();
      k.innerHTML="";
      if(response.items.length==0)k.innerHTML="sorry cannot find any relevant results";
   for (var i = 0; i < response.items.length; i+=1) {
   
      
      
     var item = response.items[i];
     var bookImg= item.volumeInfo.imageLinks.smallThumbnail;
     var title = response.items[i].volumeInfo.title;
     var lnk = item.volumeInfo.infoLink;
     var htmlcard= `
     <div class="box">
          <div class="image">
          <a href="${lnk}">
            <div class="pic"> <img src="${bookImg}" alt="Sorry Image not available" class="picimg"> </div></a>
            <h3 class="name">${title}</h3>
          </div>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum tincidunt est vitae ultrices accumsan. Aliquam ornare lacus adipiscing, posuere.<br></p>
      </div>
     `;
     k.innerHTML+= htmlcard;

   }};