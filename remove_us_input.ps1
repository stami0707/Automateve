$usLangTag = "en-US"
$usInputCode = "0409:00000409"
$langList = Get-WinUserLanguageList
$usLang = $LangList.Where({$_.LanguageTag -eq $usLangTag})[0]
$usLang.InputMethodTips.Add($usInputCode)
Set-WinUserLanguageList -LanguageList $LangList -Force
[void]($usLang.InputMethodTips.RemoveAll({$args[0] -eq $usInputCode})) # supress output by casting to void
Set-WinUserLanguageList -LanguageList $LangList -Force
