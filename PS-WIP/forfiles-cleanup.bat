REM REM forfiles /P c:\temp\test /D 16.10.2010 /m localhost_access_log.* /C "cmd /c echo @file && if /I @file==0x22localhost_access_log.2010-10-17.txt0x22 (echo ---------true) else (echo false)"
REM REM forfiles /p "C:\temp" /s /C "cmd /c echo @file" && if /I @file==*.rpm (echo "file is a RPM package") else (echo false)"
REM REM forfiles /p "$serverpath\SaxoLogs" /s /d -90 /c "cmd /c del /Q /F @file"


REM @echo on
REM set found=0
REM forfiles /p C:\temp /s /c "cmd /c echo @file"
REM if /i %found%==1 (
REM REM Call Success.bat
REM ) else (
REM if /i %found%==0 (
REM REM Call Fail.bat  
REM )
REM PAUSE



forfiles /p C:\temp /c "cmd /c echo @file"