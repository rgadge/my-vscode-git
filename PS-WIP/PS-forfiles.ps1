# forfiles /p "C:\temp" /s /d -90 /c 

# "cmd /c del /Q /F @file"

# forfiles /P c:\temp\test /D 16.10.2010 /m localhost_access_log.* /C "cmd /c echo @file && if /I @file==0x22localhost_access_log.2010-10-17.txt0x22 (echo ---------true) else (echo false)"



# forfiles /p "C:\temp" /s /C "cmd /c echo @file" #&& if /I @file==*.rpm (echo "file is a RPM package") else (echo false)"

Get-ChildItem -Recurse -Path "c:\temp" | ForEach-Object {

    $filename = $_.FullName

    if ($filename -like "*cleanup*") {
        # $lastwrite = (Get-Item $filename).LastWriteTime
        # $today = (Get-Date).AddDays(-30)
        if ($_.LastWriteTime -lt (Get-Date).AddDays(-30) -eq 1){
            #Write-Output "$filename $today, $lastwrite "
            Write-Output $filename
        }
        # $lastwrite = (Get-Item $filename).LastWriteTime
        # $today = Get-Date
        # Write-Output "$filename, was last accessed on $lastwrite"
        # $path_test = Test-Path $filename -OlderThan (Get-Date).AddDays(-5)
        # if ($path_test = 1 ){

        #     Write-Output "$filename is older than 5 days "
        # }
    }        
}

