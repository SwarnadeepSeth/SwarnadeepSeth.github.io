### Python code to place menubar in the respective html files by reading the menu.html file ###

filename_list=["index.html", "contact.html", "market-overview.html", "market-valuation_Example.html", 
"market-valuation_IND.html", "market-valuation_US.html", "stock_scanner.html", "option_pl_calc.html", "datascience_QA.html", "publications.html", "research-home.html", 
"research-post.html", "ml_overview.html", "diabetes_ML.html", "one_liners.html", "sql.html"]

for filename in filename_list:

    print ("FileName is:", filename)

    with open(filename) as f:
        contents = f.read()

    with open("menu.html") as f:
        menu_contents = f.read()

    start_marker = "<!-- Navigation-->"
    end_marker = "<!-- Page Content-->"

    start_index = contents.index(start_marker) + len(start_marker)
    end_index = contents.index(end_marker)

    contents = contents[:start_index] + "\n" + menu_contents + "\n" + contents[end_index:]

    with open(filename, "w") as f:
        f.write(contents)
