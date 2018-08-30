import webbot 

web = webbot.Browser() ; 
web.go_to("pythonanywhere.com/login") ; 
web.type("daedalcrafters") ; 
web.type("amazonmws" , "Password") ; 
web.click("Log in") ; 
web.click("Bash console" , classname="dashboard_recent_console") ; 

web.type("Hello") ; 


>For performing such automation operations you might wanna use something that's built over selenium to handle all such tasks like tab switching , automatic element finding , Special Key press and hold  :etc.

Take a look at : "webbot"

webbot works even for webpages with dynamically changing id and classnames and has more methods and features than selenium and mechanize.

Here's a small snippet

    from webbot import Browser 
    web = Browser()
    web.go_to('google.com') 
    web.click('Sign in')
    web.type('mymail@gmail.com' , into='Email')
    web.click('NEXT' , tag='span')
    web.type('mypassword' , into='Password' , id='passwordFieldId') # specific selection
    web.click('NEXT' , tag='span') # you are logged in ^_^

For your specific usage :

    web.press( web.Key.CONTROL + 't' )