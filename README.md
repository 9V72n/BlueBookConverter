# BlueBookConverter
全くの初心者だったころに作ったコードなので、読みにくい＆汚いと思います。
また、手動でやらなくてはならない手順が多いです。
使い方は、まず対象のCSV語義ファイルの2列目をコピーしてimportfile.txtとした後、.pyファイルと同じディレクトリにそのファイルを移動し、.pyファイルをコマンドで実行してください。
すると、exportfile.txtが出力されると思うので、新しいCSVファイルを作り、
対象のCSV語義ファイルの1列目を1列目、exportfile.txtの全文を2列目としてCSVタブ区切りUTF8で保存してください。
これで、Ankiにてインポート可能になると思います（表裏はCSVに沿ってください）。
