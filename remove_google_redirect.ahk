F1::
    clipboard := RegExReplace(clipboard, "https://www\.google\.com/url\?q=([^&""]+)[^""<]+", "$1") ; Remove the tracking URL prefix and parameters
return
