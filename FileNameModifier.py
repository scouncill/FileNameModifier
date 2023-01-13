import os
rootdir = 'C:\startdirectory'
count = 0

# this code takes modifies files in a directory tree structure and renames the files using only the left 10 characters 
# and re-applies the original extension

for subdir, dirs, files in os.walk(rootdir):
    print("Subdirectory is: "+ subdir)
    subslice = subdir[7:]
    print("Slice is: "+subslice)
    #if(subslice>"0999"):  #use these if statements to start/stop on specific subfolders
    #    break
    if(subslice>"0999"):   #and(subslice<"1000"):
        for file in files:
            # Split on the extension.
            split = file.split(".")
            # Get the first 5 characters in the file name
            name = split[0][:10]
            # Extension
            ext = split[1]
    
            
            if(name != split[0]):
                count = count + 1
                print("Renaming "+file+" to "+name+"."+ext)
                #os.rename(file, name+"."+ext)
                os.rename(os.path.join(subdir, file), os.path.join(subdir, name+"."+ext))
                print("Renaming "+os.path.join(subdir, file)+" to "+ os.path.join(subdir, name+"."+ext))
            #print(os.path.join(subdir, file))
            #if count > 5: #used for testing up to 2000
            #   break
        #if count > 5:
        #   break
