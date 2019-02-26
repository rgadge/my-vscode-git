# # forfiles /p "C:\temp" /s /d -90 /c 

# # "cmd /c del /Q /F @file"

# # forfiles /P c:\temp\test /D 16.10.2010 /m localhost_access_log.* /C "cmd /c echo @file && if /I @file==0x22localhost_access_log.2010-10-17.txt0x22 (echo ---------true) else (echo false)"



# # forfiles /p "C:\temp" /s /C "cmd /c echo @file" #&& if /I @file==*.rpm (echo "file is a RPM package") else (echo false)"

# Get-ChildItem -Recurse -Path "c:\temp" | ForEach-Object {

#     $filename = $_.FullName

#     if ($filename -like "*cleanup*") {
#         # $lastwrite = (Get-Item $filename).LastWriteTime
#         # $today = (Get-Date).AddDays(-30)
#         if ($_.LastWriteTime -lt (Get-Date).AddDays(-30) -eq 1){
#             #Write-Output "$filename $today, $lastwrite "
#             Write-Output $filename
#         }
#         # $lastwrite = (Get-Item $filename).LastWriteTime
#         # $today = Get-Date
#         # Write-Output "$filename, was last accessed on $lastwrite"
#         # $path_test = Test-Path $filename -OlderThan (Get-Date).AddDays(-5)
#         # if ($path_test = 1 ){

#         #     Write-Output "$filename is older than 5 days "
#         # }
#     }        
# }





# Get-ChildItem -Path C:\Data | ForEach-Object {
#     $serverpath = $_.FullName
#     forfiles /p "$serverpath\Logs" /s /d -90 /c "cmd /c del /Q /F @file"
# }

# $Path = "C:\Temp"
# $Files = Get-ChildItem -Path $Path -Recurse -File  
# ForEach($File in $Files)  { 
#     if ($File.LastWriteTime -le (Get-Date).AddDays(-90)){
#         Write-Output $File
#     } elseif ($File.Name -notlike "*.log" -and $File.LastWriteTime -le (Get-Date).AddDays(-30)){
#         Write-Output $File
#     }
# }


# Get-ChildItem -Path C:\temp -File -Recurse | Where-Object {
#     $_.LastWriteTime -le (Get-Date).Date.AddDays(-90) -or
#   ( $_.LastWriteTime -le (Get-Date).Date.AddDays(-30) -and
#     $_.Extension -ne '.Log' ) } | Remove-Item -WhatIf



# Get-ChildItem -Path C:\Data\Logs -Files -Recurse | Where-Object {
#     $_.LastWriteTime -le (Get-Date).Date.AddDays(-90) -or
#   ( $_.LastWriteTime -le (Get-Date).Date.AddDays(-30) -and
#     $_.Extension -ne '.Log' ) } | Remove-Item -WhatIf


Get-ChildItem -Path C:\TEMP | ForEach-Object {
    $servername = $_.FullName
    
    Get-ChildItem -Path "$servername" -File -Recurse | Where-Object {
    $_.LastWriteTime -le (Get-Date).Date.AddDays(-90) -or
    ( $_.LastWriteTime -le (Get-Date).Date.AddDays(-30) -and
    $_.FullName -like "*" ) } | Remove-Item -WhatIf
}
    