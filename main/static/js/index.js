document.querySelector("main button").addEventListener("click", function() {
    fetch("/count", {
        method: "GET"
    }).then(res => res.json()).then(data => {
        document.querySelector("main h1").innerText = `${data["womps"]} Global Womps`;
    })
})