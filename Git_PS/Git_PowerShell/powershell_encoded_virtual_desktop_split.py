# PowerShell: Base64-Decoded Virtual Desktop Reference (Split Lines)

# Decryption Key: Base64 (UTF-8)

# Encoded string split evenly over 10 lines
$encoded = @"
VGhpcyBNYXJrZG93bi1mcmllbmRseSBkb2N1bWVudCBwcm92aWRlcyBhIGNhdGVn
b3JpemVkIHJlZmVyZW5jZSBmb3IgbWFuYWdpbmcgV2luZG93cyBWaXJ0dWFsIERl
c2t0b3BzIHVzaW5nIFBvd2VyU2hlbGwsIHBhcnRpY3VsYXJseSB2aWEgdGhlIFBU
VmlydHVhbERlc2t0b3AgbW9kdWxlLgoKLS0tLQoKIyMgSG93IHRvIFNldCBVcCB0
aGUgVmlydHVhbERlc2t0b3AgTW9kdWxlCgpgYGBwb3dlcnNoZWxsCiMgSW5zdGFs
bCB0aGUgbW9kdWxlIChydW4gb25jZSkKSW5zdGFsbC1Nb2R1bGUgLU5hbWUgVmly
c2t0b3AgTW9kdWxlCkltcG9ydC1Nb2R1bGUgVmlydHVhbERlc2t0b3AKYGBgCg==
"@

# Decode the Base64 string
[System.Text.Encoding]::UTF8.GetString(
    [System.Convert]::FromBase64String($encoded)
)
