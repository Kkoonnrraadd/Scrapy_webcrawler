import os
import os.path

import cherrypy

tablica_nazwy = []


class Page:

    def header(self):
        return '''
            <html lang="pl">
            <head>
	            <meta charset="utf-8" />
                <meta http-equiv="X-Ua-Compatible" content="IE=edge,chrome=1">
                <title>%s</title>
                <style>

                #container
                {
                    width: full;
                    margin-left: auto;
                    margin-right: auto;
                }
                #logo
                {
                    background-color: black;
                    color: white;
                    text-align: center;
                    padding: 15px;
                }
                #nav
                {
                    float: left;
                    background-color: lightgray;
                    width: 120px;
                    min-height: 620px;
                    padding: 10px;
                }
                #content
                {
                    float: left;
                    padding: 20px;
                    width: auto;
                }
                #ad
                {
                    float: right;
                    width: 160px;
                    min-height: 620px;
                    padding: 10px;
                    background-color: lightgray;
                }
                #footer
                {
                    clear: both;
                    background-color: black;
                    color: white;
                    text-align: center;
                    padding: 20px;
                }	


                .hide
                { 
                 position:absolute; top:-1px; left:-1px; width:1px; height:1px;color:green;
                 }
                 * {
                      box-sizing: border-box;
                    }
                    
                    body {
                      background-color: #f1f1f1;
                      padding: 20px;
                      font-family: Arial;
                    }
                    
                    /* Center website */
                    .main {
                      max-width: 1000px;
                      margin: auto;
                    }
                    
                    h1 {
                      font-size: 50px;
                      word-break: break-all;
                    }
                    
                    .row {
                      margin: 10px -16px;
                    }
                    
                    /* Add padding BETWEEN each column */
                    .row,
                    .row > .column {
                      padding: 8px;
                    }
                    
                    /* Create three equal columns that floats next to each other */
                    .column {
                      float: left;
                      width: 33.33%;
                      display: none; /* Hide all elements by default */
                    }
                    
                    /* Clear floats after rows */ 
                    .row:after {
                      content: "";
                      display: table;
                      clear: both;
                    }
                    
                    /* Content */
                    .content {
                      background-color: white;
                      padding: 10px;
                    }
                    
                    /* The "show" class is added to the filtered elements */
                    .show {
                      display: block;
                    }
                    
                    /* Style the buttons */
                    .btn {
                      border: none;
                      outline: none;
                      padding: 12px 16px;
                      background-color: white;
                      cursor: pointer;
                    }
                    
                    .btn:hover {
                      background-color: #ddd;
                    }
                    
                    .btn.active {
                      background-color: #666;
                      color: white;
                    }
                </style>


            </head>


        '''

    def footer(self):
        return '''
        </body>
        </html>
        '''

    # def body(self):
    #     return'''
    #     <body>
    #     <div id="container">
    #
    #         <div id="logo">
    #             <h1>WEB APPLICATION</h1>
    #         </div>
    #
    #         <div id="nav">
    #
    #         </div>
    #
    #         <div id="content">
    #             <form action="getProduct" method="GET">
    #             Wprowadz nazwe produktu: <br /> <input type="text" name="product"/><br /><input type="submit" value="Zatwierdz">
    #             </form>
    #         </div>
    #
    #         <div id="ad">
    #             <img src="reklama.jpg" />
    #         </div>
    #
    #         <div id="footer">
    #             Jestem footer
    #         </div>
    #
    #     </div>
    #     '''


class HomePage(Page):

    def __init__(self):
        # create a subpage
        self.another = AnotherPage()

    @cherrypy.expose
    def index(self):
        return self.header() + '''
          <body>
          <iframe name="hiddenFrame" class="hide"></iframe>
          <div id="container">
              <div id="logo">
                  <h1>WEB APPLICATION</h1>
              </div>
              <div id="nav">
              </div>

              <div id="content">

                  <form name="forma" action="getProduct" method="GET" target="hiddenFrame">
                  Insert product's name: 
                  <br /><input type="text" name="name"/><br />
                  <br /> <input type="text" name="name"/><br />
                  <br /> <input type="text" name="name"/><br />
                  <input type="button" value="Submit" onClick="submitFunction()">                 
                  </form>
                    <br/> <a href=./another><input type="button" value="Next Page" ></a> <br/>
                  <script>
                        function submitFunction(){
                            var frm=document.getElementsByName("forma")[0];
                            frm.submit();
                            frm.reset();
                            return false;
                        }
                       
                  </script>
              </div>
              <div id="ad">
                  <img src="reklama.jpg" />
              </div>
              <div id="footer">
                  Jestem footer
              </div>
          </div>
          ''' + self.footer()

    @cherrypy.expose
    def getProduct(self, name):
        tablica_nazwy.append(name)
        print(name)


class AnotherPage(Page):
    title = 'Another Page'

    @cherrypy.expose
    def index(self):
        return self.header() + '''
             <body>
             <div id="container">
                 <div id="logo">
                     <h1>Application</h1>
                 </div>
                 
                 
                 
                 <div id="myBtnContainer">
                      <button class="btn active" onclick="filterSelection('all')"> Show all</button>
                      <button class="btn" onclick="filterSelection('nature')"> Nature</button>
                      <button class="btn" onclick="filterSelection('cars')"> Cars</button>
                      <button class="btn" onclick="filterSelection('people')"> People</button>
                    </div>

                 <div id="content">

                        <!-- Portfolio Gallery Grid -->
                        <div class="row">
                          <div class="column nature">
                            <div class="content">
                              <img src="/w3images/mountains.jpg" alt="Mountains" style="width:100%">
                              <h4>Mountains</h4>
                              <p>Lorem ipsum dolor..</p>
                            </div>
                          </div>
                          <div class="column nature">
                            <div class="content">
                            <img src="/w3images/lights.jpg" alt="Lights" style="width:100%">
                              <h4>Lights</h4>
                              <p>Lorem ipsum dolor..</p>
                            </div>
                          </div>
                          <div class="column nature">
                            <div class="content">
                            <img src="/w3images/nature.jpg" alt="Nature" style="width:100%">
                              <h4>Forest</h4>
                              <p>Lorem ipsum dolor..</p>
                            </div>
                          </div>
                          
                          <div class="column cars">
                            <div class="content">
                              <img src="/w3images/cars1.jpg" alt="Car" style="width:100%">
                              <h4>Retro</h4>
                              <p>Lorem ipsum dolor..</p>
                            </div>
                          </div>
                          <div class="column cars">
                            <div class="content">
                            <img src="/w3images/cars2.jpg" alt="Car" style="width:100%">
                              <h4>Fast</h4>
                              <p>Lorem ipsum dolor..</p>
                            </div>
                          </div>
                          <div class="column cars">
                            <div class="content">
                            <img src="/w3images/cars3.jpg" alt="Car" style="width:100%">
                              <h4>Classic</h4>
                              <p>Lorem ipsum dolor..</p>
                            </div>
                          </div>
                        
                          <div class="column people">
                            <div class="content">
                              <img src="/w3images/people1.jpg" alt="Car" style="width:100%">
                              <h4>Girl</h4>
                              <p>Lorem ipsum dolor..</p>
                            </div>
                          </div>
                          <div class="column people">
                            <div class="content">
                            <img src="/w3images/people2.jpg" alt="Car" style="width:100%">
                              <h4>Man</h4>
                              <p>Lorem ipsum dolor..</p>
                            </div>
                          </div>
                          <div class="column people">
                            <div class="content">
                            <img src="/w3images/people3.jpg" alt="Car" style="width:100%">
                              <h4>Woman</h4>
                              <p>Lorem ipsum dolor..</p>
                            </div>
                          </div>
                        <!-- END GRID -->
                        </div>


                 </div>
                 
                 <div id="footer">
                     Jestem footer
                 </div>
             </div>
             <script>
                                  filterSelection("all")
                    function filterSelection(c) {
                      var x, i;
                      x = document.getElementsByClassName("column");
                      if (c == "all") c = "";
                      for (i = 0; i < x.length; i++) {
                        w3RemoveClass(x[i], "show");
                        if (x[i].className.indexOf(c) > -1) w3AddClass(x[i], "show");
                      }
                    }
                    
                    function w3AddClass(element, name) {
                      var i, arr1, arr2;
                      arr1 = element.className.split(" ");
                      arr2 = name.split(" ");
                      for (i = 0; i < arr2.length; i++) {
                        if (arr1.indexOf(arr2[i]) == -1) {element.className += " " + arr2[i];}
                      }
                    }
                    
                    function w3RemoveClass(element, name) {
                      var i, arr1, arr2;
                      arr1 = element.className.split(" ");
                      arr2 = name.split(" ");
                      for (i = 0; i < arr2.length; i++) {
                        while (arr1.indexOf(arr2[i]) > -1) {
                          arr1.splice(arr1.indexOf(arr2[i]), 1);     
                        }
                      }
                      element.className = arr1.join(" ");
                    }
                    
                    
                    // Add active class to the current button (highlight it)
                    var btnContainer = document.getElementById("myBtnContainer");
                    var btns = btnContainer.getElementsByClassName("btn");
                    for (var i = 0; i < btns.length; i++) {
                      btns[i].addEventListener("click", function(){
                        var current = document.getElementsByClassName("active");
                        current[0].className = current[0].className.replace(" active", "");
                        this.className += " active";
                      });
                    }
                    </script>
             ''' + self.footer()


# @cherrypy.tools.json_in()
#     def index(self):
#         data = cherrypy.request.json
# response.stream yield

tutconf = os.path.join(os.path.dirname(__file__), 'tutorial.conf')

if __name__ == '__main__':
    cherrypy.quickstart(HomePage(), config=tutconf)