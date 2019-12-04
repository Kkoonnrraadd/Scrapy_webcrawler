import os
import os.path

import cherrypy


tablica_nazwy=[]


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
                    width: 1000px;
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
                    width: 640px;
                }
                #ad
                {
                    float: left;
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
                </style>
                
                
            </head>
            
            
        '''

    def footer(self):
        return'''
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
    def getProduct(self,name):
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
                     <h1>WEB APPLICATION</h1>
                 </div>

                 <div id="nav">

                 </div>

                 <div id="content">
                     
                 </div>

                 <div id="ad">
                     <img src="reklama.jpg" />
                 </div>

                 <div id="footer">
                     Jestem footer
                 </div>

             </div>
             ''' + self.footer()


# @cherrypy.tools.json_in()
#     def index(self):
#         data = cherrypy.request.json
#response.stream yield

tutconf = os.path.join(os.path.dirname(__file__), 'tutorial.conf')

if __name__ == '__main__':
    cherrypy.quickstart(HomePage(), config=tutconf)