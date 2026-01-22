#Pegar o diretorio atual
$scriptDirectory = Split-Path -Path $MyInvocation.MyCommand.Definition -Parent 

#Arquivo saída com todos sql
$outputFile = Join-Path -Path $scriptDirectory -ChildPath "migration.sql"

#Verifica se o arquivo já existe, se ja existir deleta
if (Test-Path $outputFile){
    Remove-Item $outputFile
}

#Pega o conteudo dos arquivos
$sqlFiles = Get-ChildItem -Path $scriptDirectory -Filter *.sql -File | Sort-Object Name 

#Concatena arquivos
foreach($file in $sqlFiles){
    Get-Content $file.FullName | Out-File -Append -FilePath $outputFile
    "GO" | Out-File -Append -FilePath $outputFile
}

Write-Host "Todos arquivos foram combinados com sucesso!!"