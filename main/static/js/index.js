document.querySelector("main button").addEventListener("click", function() {
    fetch("/count", {
        method: "GET"
    }).then(res => res.json()).then(data => {
        document.querySelector("main h1").innerText = `${data["womps"]} Global Womps`;
    }).then(() => {
        fetch("/total", {
            method: "GET"
        }).then(res => res.json()).then(data => {
            return data["total"];
        }).then(womp_max => {
            console.log(womp_max);
            let random_womp = Math.floor(Math.random() * womp_max) + 1;
            return `${random_womp}.flac`;
        }).then(womp_filename => {
            let audio = new Audio(`/static/${womp_filename}`);
            audio.play();
        })
    })
})