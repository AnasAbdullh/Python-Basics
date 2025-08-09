with  open("/data/data/com.ikou.pycoding/files/code_project/Hello_World/src/strings.txt","rt") as InputFile, \
      open("/data/data/com.ikou.pycoding/files/code_project/Hello_World/src/string_output.txt","wt") as OutputFile :


      text = ""

      for Line in InputFile:
          Line = Line.rstrip()
          if Line != "I" and Line != "Almadrsa":
            text = text + " " + Line.lower()
          else :
            text = text + " " + Line
   

    
      OutputFile.write(text)
  
  
  
