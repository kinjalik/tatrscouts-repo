const title = document.querySelector("#quest-name")
// const varContainer = document.querySelector("#var-container")
const textContainer = document.querySelector("#text-container")
const buttonContainer = document.querySelector("#button-container")

const BASE = "https://tatar-scouts-api.herokuapp.com"

var variables,
    variable_names,
    quest_id,
    current_segment;

async function updateVars(variables, variable_names) {
    return;
    varContainer.innerHTML = ""
    for (const key in variables) {
        varContainer.innerHTML += `<li><b>${variable_names[key]}</b>: ${variables[key]}</li>`
    }
}

async function drawSegment(segment_id) {
    console.log(`DRAWING SEGMENT: ${segment_id}`)
    let req = await fetch(`${BASE}/quests/${quest_id}/segments/${segment_id}`)
    const segment = await req.json();
    current_segment = segment_id;
    // // console.log(segment);

    textContainer.innerHTML = `<div class="mb-1">${segment['text']}</div><div class="ru">${segment['text_ru']}</div>`;


    req = await fetch(`${BASE}/quests/${quest_id}/relations/from/${segment_id}`);
    const relations = await req.json();

    if (relations.length == 0) {
        buttonContainer.innerHTML = `<b>Игра пройдена</b>`;
        return;
    }

    if (relations[0]['is_random']) {
        randomChoose(relations)
    } else if (!relations[0]['is_typed']) {
        manualChoose(relations)
    } else {
        typedChoose(relations)
    }
}

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min) + min); //The maximum is exclusive and the minimum is inclusive
}


async function filterByPredicate(relations) {
    const result = []
    for (const rel of relations) {
        let correct = true;
        for (const variable in rel['predicate']) {
            const cur_value = variables[variable];
            const cmd = `${cur_value}${rel['predicate'][variable]}`
            if (eval(cmd) == false) {
                // // console.log(cmd);
                correct = false;
                break;
            }
        }
        if (!correct)
            continue;
        result.push(rel);
    }
    // console.log(result);
    return result;
}

async function applyEffect(rel) {
    for (const variable in rel['effects']) {
        let curValue = variables[variable];
        // console.log(curValue);
        const cmd = `curValue = curValue ${rel['effects'][variable]}`
        // console.log(cmd);
        eval(cmd);
        // console.log(curValue);
        variables[variable] = curValue;
    }
    updateVars(variables, variable_names)
}

async function randomChoose(relations) {
    relations = await filterByPredicate(relations)
    const randomRelation = relations[getRandomInt(0, relations.length)]
    // console.log(randomRelation);
    const btn = `<button onclick="callTransition(${randomRelation['id']})" class="btn btn-block btn-danger">
                    <div class="mb-1">Вакыйга: ${randomRelation['action_text']}</div>
                    <div class="ru">Cобытие: ${randomRelation['action_text_ru']}</div>
                </button>`
    buttonContainer.innerHTML = btn;
}

async function manualChoose(relations) {
    relations = await filterByPredicate(relations)
    buttonContainer.innerHTML = '';
    for (const relation of relations) {
        const btn = `<button onclick="callTransition(${relation['id']})" class="btn btn-block btn-primary mb-2">
            <div class="mb-1">${relation['action_text']}</div>
            <div class="ru">${relation['action_text_ru']}</div>
            </button>`;
        buttonContainer.innerHTML += btn;
        // // console.log(relation);
    }
}

async function typedChoose(relations) {
    relations = await filterByPredicate(relations);
    buttonContainer.innerHTML = `
  <div class="form-group">
    <input type="text" class="form-control" id="answer" aria-describedby="answer" placeholder="Введите ответ..">
  </div>
  <button onclick="applyTypedChoose(${current_segment})" type="submit" class="btn btn-primary">
    <div>Ответить (по татарски)</div>
    <div>Ответить</div>
  </button>`
}

async function applyTypedChoose(current_segment) {
    const answerContainer = document.querySelector("#answer");
    const answer = answerContainer.value;

    const req = await fetch(`${BASE}/quests/${quest_id}/relations/from/${current_segment}`);
    const nextRelations = await req.json();

    const relToChoose = nextRelations[0];
    callTransition(relToChoose['id'])

}

async function callTransition(id) {
    console.log(`RELATION ${id} CALLED`)
    let req = await fetch(`${BASE}/quests/${quest_id}/relations/${id}`)
    const rel = await req.json();
    // // console.log(rel);
    applyEffect(rel);
    drawSegment(rel['to_segment_id'])
}

(async () => {
    const params = new URLSearchParams(window.location.search)
    quest_id = params.get("quest_id");
    const req = await fetch(`${BASE}/quests/${quest_id}`, {
        headers: {
            Accept: "application/json"
        }
    });
    const quest = await req.json();
    title.innerHTML += quest['name'];

    // console.log(quest);
    current_segment = quest['starting_segment']
    variables = quest['initial_values']
    variable_names = quest['variables']
    await updateVars(quest['initial_values'], quest['variables'])

    drawSegment(current_segment);
})();