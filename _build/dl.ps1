$ProgressPreference = 'SilentlyContinue'
$base = 'https://autoglm-oss.z.ai/auto_fly/'
$out  = Join-Path $PSScriptRoot '..\assets\img'
New-Item -ItemType Directory -Force -Path $out | Out-Null

$items = @(
  'hero-clinic|61bb495d-bf31-4660-a017-72941176f202.jpg|1795336865-0-0-2eb982c2ffa9502a770b8b5a24151b0d',
  'operatory|95c6b1cc-f31c-4863-b418-dd796d3b894f.jpg|1795336865-0-0-4805e35af143ec1d6c8945703a836b6c',
  'clinic-room|40d7bfd8-fd1f-47a7-93dd-7116e99c898e.jpeg|1795336865-0-0-a945cb79561a00b42cfe5b9c317c1ccf',
  'exam-room|df86683f-175f-4438-af35-847ff8e5e263.jpg|1795336865-0-0-73f1066357f2bf96f01e8d7a21c90490',
  'consult|98ec42e3-fd06-479b-8a37-9032d0081442.jpg|1795336868-0-0-c7246a64fb28105b6434703eed564244',
  'treatment|5514ee80-ba15-40a3-944b-f7b24fd70e1b.png|1795336868-0-0-72c80b18154f44d96186e5834d9b6c3d',
  'rct|315f53df-adfc-4a97-a80e-5cff32ef83ca.jpg|1795336868-0-0-3684207ef9c6e4f34c313d1511815150',
  'instruments|cf19e371-694a-48ea-aa8a-4dc56caa0f9a.jpg|1795336868-0-0-a87b67925c8bc94afff7cc8fe92d6f30',
  'chair-patient|82d049a0-deba-4318-b261-6a68b1a99297.jpg|1795336868-0-0-83f240b31d81f18166c6ab6d66395a1f',
  'patient-hijab|dc92075c-ec41-4d07-90db-6cc760ad57eb.jpg|1795336868-0-0-4f6c2a3fae64dedcb2d81ddc727f20fd',
  'smile-macro|375321ed-8e8a-40dd-a9f1-0a9dc97e82dd.jpg|1795336893-0-0-22be86f42efed927091ed0b7865dc323',
  'smile-portrait|aa308f51-eccf-4104-bb72-b66dde70dad7.jpg|1795336893-0-0-b1a135ce4588ccb65288512acd806c5e',
  'smile-woman|98bcba32-5dca-4510-a108-1d69b9fa1532.png|1795336893-0-0-d8aaf980787b6174b080347acf755ee4',
  'implant-model|75944ff4-dd72-4f4f-9141-d0f36c65e352.jpg|1795336893-0-0-2142670757c0c4d12e1ee8e9127728f0',
  'desk-xray|48a81186-e12f-48af-8d34-41602b5d0b36.jpg|1795336893-0-0-25285f011045d4bd2d5f01df3e6b5e63',
  'implants-row|8be66f86-579c-4821-b472-48961278f089.jpg|1795336893-0-0-94ed76fd6ef84c936698dcd0f8d5c252',
  'reception|49f1aa36-5346-435c-93bb-e26c754698c6.jpeg|1795336892-0-0-2300db31e0321a1181b4543813a753bf',
  'waiting|ac7d7969-a5e4-4d58-8006-18937d5853b5.jpg|1795336892-0-0-906e6886398b66f30b34e9883f1c6135',
  'aligner-vs-braces|ebdbe733-5120-4acc-bbf8-fed6359ab4bc.jpg|1795336890-0-0-34ce01d5d44a8b9a649468aaa90b2d59',
  'aligner|74694b53-62ad-4ecd-a109-520a072e1f99.jpg|1795336890-0-0-c85acdd6efbc27612af44652fbfe1e03',
  'aligner-woman|70ac9d28-66d8-4b54-97c1-9c8d5853c978.jpg|1795336890-0-0-af1007eea76251e820619e36910c174b',
  'braces-model|7c7ae320-93c1-487b-8d3f-178f3260d378.jpg|1795336890-0-0-0780df48919a5301d4b0f228bb22945f'
)

$ok = 0; $fail = @()
foreach ($it in $items) {
  $p = $it.Split('|')
  $name = $p[0]; $file = $p[1]; $key = $p[2]
  $ext = [System.IO.Path]::GetExtension($file)
  $dest = Join-Path $out ($name + $ext)
  try {
    Invoke-WebRequest -Uri ($base + $file + '?auth_key=' + $key) -OutFile $dest -TimeoutSec 60 -UserAgent 'Mozilla/5.0'
    $sz = (Get-Item $dest).Length
    if ($sz -lt 3000) { throw "too small ($sz bytes)" }
    $ok++
    Write-Output "OK   $name$ext  $([math]::Round($sz/1kb)) KB"
  } catch {
    $fail += $name
    Write-Output "FAIL $name -> $($_.Exception.Message)"
  }
}
Write-Output "----"
Write-Output "downloaded: $ok / $($items.Count)"
if ($fail.Count -gt 0) { Write-Output ("failed: " + ($fail -join ', ')) }
