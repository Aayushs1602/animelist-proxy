fetch('static/anime.json')
.then(data => data.json())
.then(Data => {
    str=''
    console.log(Data.length);
    for (let z=0; z<Data.length; z++)
    {
        data = Data[z];
        eps = data.episodes? data.episodes: "Ongoing";
        image_url = data.image_url
        str += `
        <div class="card post bg-primary shadow-soft border-light my-3" target="_blank" onclick="window.open('${data.url}')">
        <div class="row no-gutters align-items-center hov">
        <div class="col-md-4">
            <img src="${image_url}">
        </div>
            <div class="col-md-8">
                <div class="card-body">
                    <h3 class="h2 card-title">${data.title}</h3>

                    <p class="card-text mb-4">
                       ${data.synopsis}
                    </p>
                    <div class="d-flex justify-content-between align-items-center">
                        <span class="card-text h6">
                            <span class="far fa-calendar-alt mr-2">

                            </span>
                           Episodes: ${eps}
                        </span>
                    </div>
                </div>
            </div>
        </div>
    </div>

        `
        // console.log(z);
    }
    document.getElementById("top").innerHTML = str;
})
// extender = document.getElementById("input_field").value
// console.log(extender)
// window.history.pushState(extender, 'Title', extender);
