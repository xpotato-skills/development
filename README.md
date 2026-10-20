# 日本語リリースノート SKILL

変更点を利用者の視点で伝え、ダウンロードと導入・更新へ迷わず進める日本語の更新告知を作る Codex SKILL です。Minecraft Release Changelogs の見渡しやすさを参考にした構成で、任意のプロジェクトに使えます。他製品の文面・ロゴ・固有表現は含みません。

## 内容

- [SKILL.md](skills/japanese-release-notes/SKILL.md): 根拠確認、編集手順、品質チェック
- [テンプレート](skills/japanese-release-notes/references/template.md): 変更規模に応じて調整する告知の構成

## 導入

Codex の `skill-installer` に、このリポジトリの `skills/japanese-release-notes` を指定してください。既存の同名 SKILL は上書きせず、差分を確認してください。

現行 Codex のユーザー共通探索先は `~/.agents/skills` です。インストーラーが旧 `~/.codex/skills` を使う場合は、`--dest` で現行の探索先を明示してください。必要な LICENSE・NOTICE も SKILL ディレクトリに含まれます。既存の同名ディレクトリは上書きしません。

導入後、Codex の SKILL 一覧で認識を確認してください。反映されない場合は Codex を再起動して確認します。[公式の探索先と導入案内](https://developers.openai.com/codex/build-skills)を参照してください。

```text
$japanese-release-notes を使って、対象の GitHub Release を日本語で整理してください。
```

本文更新には対象 Release の編集権限と依頼が必要です。この SKILL は新規公開、タグ変更、配布物の差し替え、ソフトの実行を許可するものではありません。

## ライセンスと表示の範囲

この SKILL の配布物には **AGPL-3.0-only** を適用します。クレジットは **Xpotato.net / Xpotato1024** です。[LICENSE](LICENSE) の正式全文と [NOTICE](NOTICE) を参照してください。再配布・改変時に適用される条件と必要な表示を保持してください。第三者の権利を変更しません。

この SKILL 自身の作者クレジットや配布ライセンスは、SKILL が生成するリリースノートへ追加しません。利用したという理由だけで、生成物への作者帰属・AGPL 適用・クレジットを要求せず、SKILL 作者の権利を主張しません。所有するテンプレートや例文を生成文書へ組み込む場合の追加許諾は [生成物の利用方針・追加許諾](OUTPUT-PERMISSION.md) に記載しています。ユーザーや第三者の既存権利は変更しません。

対象ソフトウェア自身の必要な著作権・ライセンス・第三者通知は保持します。架空プロジェクトの [入力例](tests/fixtures/maple-release.json) と [出力例](examples/maple-v1.4.0.md) でこの境界を確認できます。これらは実在する製品・配布物の告知ではありません。

## 検証

Python 標準ライブラリのみで、`python -m unittest discover -s tests -v` を実行できます。架空例の事実・対象プロジェクトの表示保持・SKILL クレジットの非混入・配布時の法的メタデータ保持を検証します。
