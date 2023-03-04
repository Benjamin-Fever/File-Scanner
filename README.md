<body>
<h1>File Scanner</h1>
<p>
<h2>Description</h2>
This is a python package that works similar to the java.util.scanner.
You can easily scan through a file from a specified path.
</p>

<h2>Documentation</h2>
<h3>How to install</h3>
Download the Scanner.py script in the src file and add to your project

<h3>Example</h3>
This reads a file one word or number at a time:

    import Scanner
    
    scan = Scanner("*insert file path")   <- Replace insery file path with the file you wish to read
    scan.next()                           <- Returns the next word as a string
    scan.nextInt()                        <- Returns the next int this will set its possition at this point
    scan.nextFloat()                      <- Returns the next float, works same as nextInt()

</body>
