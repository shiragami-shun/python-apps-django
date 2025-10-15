document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("translateBtn");
  const input = document.getElementById("inputText");
  const output = document.getElementById("outputText");
  const lang = document.getElementById("languageSelect");

  btn.addEventListener("click", async () => {
    const text = input.value.trim();
    const target = lang.value;

    if (!text) {
      output.textContent = "⚠ 翻訳する文章を入力してください。";
      return;
    }
    output.textContent = "翻訳中...";

    try {
      const res = await fetch("/library/translate_api/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify({ text, target_lang: target }),
      });

      const data = await res.json();
      if (res.ok && data.translated_text) {
        output.textContent = data.translated_text;
      } else {
        console.error("APIエラー応答:", data);
        output.textContent = data.error || "❌ 翻訳エラーが発生しました。";
      }
    } catch (err) {
      console.error("通信エラー:", err);
      output.textContent = "❌ 通信エラーが発生しました。";
    }
  });

  function getCookie(name) {
    const cookies = document.cookie.split(";");
    for (let c of cookies) {
      c = c.trim();
      if (c.startsWith(name + "=")) return decodeURIComponent(c.substring(name.length + 1));
    }
    return "";
  }
});
