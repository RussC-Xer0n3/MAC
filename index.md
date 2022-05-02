<nav class="w3-container w3-teal w3-center w3-margin-top">
<br>
  <a href="https://www.facebook.com/profile.php?id=100075972987666"><i class="fa fa-facebook-official w3-hover-opacity"></i></a>
  <a href="https://www.instagram.com/russellclarke821"><i class="fa fa-instagram w3-hover-opacity"></i></a>
  <a href="https://www.pinterest.co.uk/russellclarke821/"><i class="fa fa-pinterest-p w3-hover-opacity"></i></a>
  <a href="https://twitter.com/Developing821"><i class="fa fa-twitter w3-hover-opacity"></i></a>
  <a href="https://www.linkedin.com/in/russell-clarke-09a1a5238"></a><i class="fa fa-linkedin w3-hover-opacity"></i>
<br>
</nav>
# MAC Address Generation
## Generating all possible MAC Addresses

### Preamble
The code here was the preamble to [IP-Port](https://russc-xer0n3.github.io/IP-Port). I was looking into MAC addresses and noting them all down to reference them in another project which has not yet been started; I considered an automated randomiser however, the issue is that consumes a lot of processing power to randomise and what if you want to reference certain addresses?

### Solution
The solution was to pipe ```>>``` or ```||``` out to a text file or generate the MAC addresses to [key to value pairs dictionary](https://www.geeksforgeeks.org/add-a-keyvalue-pair-to-dictionary-in-python/) and use the file as a reference saving processing power in the long run.

### MAC Daddy code
```
#!/usr/bin/env python

# Simple to increment some values.
# @author Russell Clarke 0ka Rusher SD200984
# @version 2.0  
# @Created 14.08.2020
# @Listening to My Screaming Fridge and the Extractor

#/bin/env python

for w in range(16):
    m = '%x' % w
    for v in range(16):
        l = '%x' % v
        for u in range(16):
            j = '%x' % u
            for t in range(16):
                x = '%x' % t
                for s in range(16):
                    h = '%x' % s
                    for r in range(16):
                        g = '%x' % r
                        for q in range(16):
                            f = '%x' % q
                            for p in range(16):
                                e = '%x' % p
                                for o in range(16):
                                    d = '%x' % o
                                    for n in range(16):
                                        c = '%x' % n
                                        for k in range(16):
                                            b = '%x' % k
                                            for i in range(16):
                                                a = '%x' % i
                                                print(a + b + ':' + c + d + ':' + e + f + ':' + g + h + ':' + x + j + ':' + l + m)

exit(0)
```

### Moving forward
Perhaps I can think of several projects linked with MAC Addresses, there are a few out there including [MAC Address Lookup](https://maclookup.app/) one of my favourites and [macvendors](https://macvendors.com/) my go to guys whenrequired. 
<head>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type">
    <meta charset="UTF-8">
    <meta name="description" content="Projects and Portfolio">
    <meta name="keywords" content="HTML, CSS, JavaScript, PHP, MySQLi, Python, Java, C, C++, C#, Time, Shapes">
    <meta name="author" content="Russell Clarke">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<footer class="w3-container w3-teal w3-center w3-margin-top">
  <p>Find me on social media.</p>
  <a href="https://www.facebook.com/profile.php?id=100075972987666"><i class="fa fa-facebook-official w3-hover-opacity"></i></a>
  <a href="https://www.instagram.com/russellclarke821"><i class="fa fa-instagram w3-hover-opacity"></i></a>
  <a href="https://www.pinterest.co.uk/russellclarke821/"><i class="fa fa-pinterest-p w3-hover-opacity"></i></a>
  <a href="https://twitter.com/Developing821"><i class="fa fa-twitter w3-hover-opacity"></i></a>
  <a href="https://www.linkedin.com/in/russell-clarke-09a1a5238"></a><i class="fa fa-linkedin w3-hover-opacity"></i>
  <p>Powered by <a href="https://www.w3schools.com/w3css/default.asp" target="_blank">w3.css</a></p>
</footer>
