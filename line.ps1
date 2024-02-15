$boundary = [System.Guid]::NewGuid().ToString()
$headers = @{
    "Authorization" = "Bearer YjRN9VmuTjsw5oXUXgeiqfYLXaCYMBnmlEvOAc2hNJp"
    "Content-Type" = "multipart/form-data; boundary=$boundary"
}
$message = "foobar"
$body = @"
--$boundary
Content-Disposition: form-data; name="message"

$message
--$boundary--
"@

try {
    $response = Invoke-RestMethod -Uri "https://notify-api.line.me/api/notify" -Method POST -Headers $headers -Body $body
    $response
}
catch {
    Write-Host "Error: $($_.Exception.Message)"
}
