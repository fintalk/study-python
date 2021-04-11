import sys 

for fn in sys.argv[1:]:
    # try:
    #     f = open(fn)
    # except:
    #     print(f"{fn} というファイルは存在しません")
    # else:
    #     try:
    #         print(fn, len(f.read()))
    #     finally:
    #         f.close() 
    
   
    try:
        with open(fn) as f: 
            print(fn, len(f.read()))
    except:
        print(f"{fn} というファイルは存在しません")
        
            
        

