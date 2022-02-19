Function Get-WallPaper()
{
 $path = Get-ItemProperty -path 'HKCU:\Control Panel\Desktop\' -name wallpaper

 rundll32.exe user32.dll, UpdatePerUserSystemParameters 
 
 return $path
}

$var = Get-WallPaper

Write-Host $var

$cd = Get-Location

# New-Item -Path $cd -Name Test.text -ItemType File
$filecd = -join($cd,"\temp.tmp");
Out-File -Encoding "UTF8" -FilePath $filecd -InputObject $var

cls

start gwtf.py