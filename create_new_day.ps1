# Create a new day script for Advent of Code 2025
# Usage: .\create_new_day.ps1 -dayNumber <1-25>
# copies template files (00_ex.py) and creates input files (xx_ex.py) for the specified day

param (
    [Parameter(Mandatory=$true)]
    [int]$day
)
if ($day -lt 1 -or $day -gt 25) {
    Write-Error "Day number must be between 1 and 25."
    exit 1
}

# print message
Write-Host "Creating files for Day" ($day).ToString("00")"..."

# Copy template code file
$templateCodeFile = "00_ex.py"
Copy-Item -Path $templateCodeFile -Destination (($day).ToString("00") + "_ex.py")

# Create input file
New-Item -ItemType File -Path (($day).ToString("00") + "_in.txt") | Out-Null

# Create test input file
New-Item -ItemType File -Path (($day).ToString("00") + "_test.txt") | Out-Null
Write-Host "Files created successfully."