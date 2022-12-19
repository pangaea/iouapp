function init(form_query, api_path, success_path) {
    document
    .querySelector(form_query)
    .addEventListener("submit", async function (e) {
        e.preventDefault();
        console.log(new URLSearchParams(new FormData(e.target)).toString());
        const res = await fetch(api_path, {
            body: new URLSearchParams(new FormData(e.target)).toString(),
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
        });
        await res.json().then(o => {
            if(o.success === "true") {
                // Redirect to root
                location = success_path;
            } else {
                alert(o.error);
            }
        });
    });
}