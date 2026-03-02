async function runCode() {
    const code = document.getElementById("code").value;

    const response = await fetch("/run", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ code: code })
    });

    const data = await response.json();

    document.getElementById("pythonOutput").innerText = data.generated_python;
    document.getElementById("result").innerText =
        data.output ? data.output : data.error;
}