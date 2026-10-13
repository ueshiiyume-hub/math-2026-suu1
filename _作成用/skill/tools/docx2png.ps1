# プリント(docx)を PDF にして（Word を読み取り専用で使う）、ページごとの PNG にする
# 使い方: powershell -File docx2png.ps1 <docx> <出力フォルダ>
param([string]$src, [string]$out)
New-Item -ItemType Directory -Force $out | Out-Null
$pdf = Join-Path $out "print.pdf"
$w = New-Object -ComObject Word.Application; $w.Visible = $false
try { $d = $w.Documents.Open($src, $false, $true); $d.ExportAsFixedFormat($pdf, 17); $d.Close($false) } finally { $w.Quit() }
python -W ignore -c "import fitz,sys; d=fitz.open(sys.argv[1]); [p.get_pixmap(dpi=110).save(sys.argv[2]+'/pg%d.png'%(i+1)) for i,p in enumerate(d)]" $pdf $out
