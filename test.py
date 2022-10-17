def readData(rdata):
    
    read_file=open("data.txt","r")
    line=(read_file.read())
    
    
    line22 = ast.literal_eval(line)
    #global main_data
    main_data = json.dumps(line22)
    return main_data

print(readData(a))
