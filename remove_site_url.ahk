F1::
    clipboard := RegExReplace(clipboard, "href=""https:\/\/[DOMAIN HERE]\.umich\.edu(.*?)""", "href=""$1""") ; Remove parent domain from links
return