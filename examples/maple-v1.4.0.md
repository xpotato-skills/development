> 架空プロジェクトの検証用サンプルです。リンク先の example.invalid は実在する配布先ではありません。

# Maple Notes 1.4.0

1.3.2 からの更新では、検索結果を更新日時順に並べ替えられるようになりました。空のノートをエクスポートすると失敗していた問題も修正しました。

## ダウンロード

| 環境・用途 | ファイル |
| --- | --- |
| Windows x64 | [maple-1.4.0-windows-x64.zip](https://example.invalid/maple/releases/download/v1.4.0/maple-1.4.0-windows-x64.zip) |
| 対応ソース | [maple-1.4.0-source.tar.gz](https://example.invalid/maple/releases/download/v1.4.0/maple-1.4.0-source.tar.gz) |

導入・更新の手順と検証範囲は、以下を確認してください。

## 新機能

- 検索結果を更新日時順に並べ替えられるようになりました。

## 修正

- 空のノートをエクスポートすると失敗していた問題を修正しました。

## 導入・更新

新しく利用する場合は、Windows x64 用の ZIP を新しいフォルダーへ展開し、`maple.exe` を起動してください。

更新する場合は、旧アプリを終了してください。その後、新しい版の ZIP を新しいフォルダーへ展開し、`maple.exe` を起動してください。ノートの形式変更はありません。

## 検証範囲・注意事項

Windows x64 の fixture 検証と単体テストを実施しています。実端末への導入は未実施です。

ネットワークフォルダー上のノートは未検証です。

## ライセンス・対応ソース

クレジット: Maple Team

Maple Notes のライセンスは [MIT](https://example.invalid/maple/blob/v1.4.0/LICENSE) です。

Birch parser — BSD-3-Clause。詳細は [第三者通知](https://example.invalid/maple/blob/v1.4.0/THIRD-PARTY-NOTICES.txt) を参照してください。

1.4.0 の対応ソースは、上記ダウンロード表から入手できます。
