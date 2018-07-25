![pokiiio WeatherDisplayForEPapers](https://lh3.googleusercontent.com/yp3nca1aNzq_NPH-kMltZ9-1Rl2DpftLXh2oMDxC640N0RBh4wcOn3h804IIg-B3m_bpycWb_h7rEUGKCXi561ZWcpRoAqyngSMToYSxPd67R376lkC6rXbRwS1llMPNJQ6Ds1PmGY8=s600 "pokiiio WeatherDisplayForEPapers")

# WeatherDisplayForEPapers
電子ペーパーに天気予報を表示するために、天気予報情報を画像化するスクリプトです。

## 何ができるの？
下のような画像ファイルを作成します。

![pokiiio WeatherDisplayForEPapers](https://lh3.googleusercontent.com/ewes5Np0wmUpz-NtQ3lBltoef_2L5_O5qhFN2FSkvBbiSWD4ama8FKoHL_t4fXFauoYSyrCbHE7krbZFXJg66ha-s6lksmrtJW83kZlWu2k-owynZVCjPpUOcF3duEI5XBWsvKUuQV0=s0 "pokiiio WeatherDisplayForEPapers")

## もう少し詳しく
 - PythonとPILで画像を作成
 - 画像サイズは固定 （264x176）
 - 情報はlivedoorの天気予報API（無料）を利用 （http://weather.livedoor.com/weather_hacks/webservice）
 - 横浜の天気を取得するようにハードコードしている
 - 「今日」「明日」の天気（文字とアイコン）と最高・最低気温を表示
 - フォントは毎度おなじみのM+ FONTS （https://mplus-fonts.osdn.jp/）
 - 画像ファイルは、スクリプトと同じ階層に「image.png」という名前で生成される

## 使い方
このスクリプトは、天気予報情報の取得と画像作成しか行いません。お持ちの電子ペーパーに情報を表示させるには、それぞれの電子ペーパーのライブラリ等を使って表示させてください。

## 動作確認済電子ペーパー
 - PaPiRus 2.7inch （https://jp.rs-online.com/web/p/products/1218357/）
