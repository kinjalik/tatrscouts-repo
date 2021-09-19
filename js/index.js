(async () => {
    try {

        const questsRes = await fetch("https://tatar-scouts-api.herokuapp.com/quests/", {
            headers: {
                Accept: "application/json"
            },
        });
        const quests = await questsRes.json()

        const list_of_quests = document.querySelector("#stories")
        for (const quest of quests) {
            list_of_quests.innerHTML += `<li><a href="game.html?quest_id=${quest["id"]}">${quest['name']}</a></li>`
        }


        // console.log(quests);
    } catch (e) {
        // console.log(e);
    }

})()