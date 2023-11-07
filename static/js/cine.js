
/*
 * Initialize Plyr
 */
const player = new Plyr('#videoPlayer');
window.player = player;



// window.onload = (event) => {
//     // console.log("page is fully loaded");

//     let timeVideo = player.currentTime;
//     console.log("currentTime : " +timeVideo);

//     let durationVideo = player.duration;
//     console.log("duration : " +durationVideo);

//     // convertir la durée en text
//     let du = durationVideo.toString();

//     // couper le texte au niveau du point
//     let arr = du.split(".");
//     let x = arr[0];

//     // convertir en entier
//     let y = parseInt(x,10);
//     console.log(y);

//     function secondsToHHMMSS(totalSeconds) {
//         let hours = Math.floor(totalSeconds / 3600);
//         let minutes = Math.floor((totalSeconds - (hours * 3600)) / 60);
//         let seconds = totalSeconds - (hours * 3600) - (minutes * 60);
      
//         // Remplissage des valeurs pour s'assurer qu'il s'agit de deux chiffres
//         if (hours < 10) { hours = "0" + hours; }
//         if (minutes < 10) { minutes = "0" + minutes; }
//         if (seconds < 10) { seconds = "0" + seconds; }
      
//         return hours + ':' + minutes + ':' + seconds;
//     }
      
//     // Exemple d'utilisation :
//     let totalSeconds = y;
//     // console.log("time :" + secondsToHHMMSS(totalSeconds));

//     let dur = document.getElementsByClassName('duration');
//     dur.textContent = secondsToHHMMSS(totalSeconds);

// };