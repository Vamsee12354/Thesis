$models = @('deepseek', 'llama', 'mistral', 'phi', 'gemini')
$tasks = 1..9 | ForEach-Object { "task_$_" }
$runs = 1..10 | ForEach-Object { "run_$($_.ToString('00')).py" }

$baseDir = "c:\Users\kalup\Desktop\Thesis\results"

foreach ($model in $models) {
    foreach ($task in $tasks) {
        $dirPath = Join-Path $baseDir -ChildPath "$model\$task"
        New-Item -ItemType Directory -Force -Path $dirPath | Out-Null
        foreach ($run in $runs) {
            $filePath = Join-Path $dirPath -ChildPath $run
            New-Item -ItemType File -Force -Path $filePath | Out-Null
        }
    }
}
