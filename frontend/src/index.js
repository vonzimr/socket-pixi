import io from 'socket.io-client';
import * as PIXI from 'pixi.js';
import character from './images/ph.png';

console.log(character);

export const socket = new WebSocket('ws://localhost:5000/ws');
socket.binaryType = 'arraybuffer';

socket.addEventListener('open', function(event){
    socket.send("connected");
});

socket.addEventListener('message', function(event){
    console.log("message received: ", event.data);
});

let keyState = {
    "ArrowDown": false,
    "ArrowUp": false,
    "ArrowLeft": false,
    "ArrowRight": false
}

document.addEventListener('keydown', (event) => {
    let key = event.key;
    if(keyState.hasOwnProperty(key)){
        keyState[key] = true;
    }
    event.preventDefault();
}, true);

document.addEventListener('keyup', (event) => {
    let key = event.key;
    if(keyState.hasOwnProperty(key)){
        keyState[key] = false;
    }
    event.preventDefault();
}, true);


class Character {
    constructor(sprite){
        this.sprite = sprite;
        this.setup(sprite);
        this.vel = 5;


    }
    setup(sprite){
        this.character = new PIXI.Sprite(sprite);
        console.log(this.character);
        app.stage.addChild(this.character);
        app.ticker.add(delta => this.gameloop(delta));
    }
    gameloop(delta){
        for (var key in keyState){
            if(keyState[key]){
                this[key]();
            }
        }

    } 
    ArrowUp(){
        this.character.y -= this.vel;
    }

    ArrowDown(){
        this.character.y += this.vel;
    }
    ArrowLeft(){
        this.character.x -= this.vel;
    }
    ArrowRight(){
        this.character.x += this.vel;
    }


}

const app = new PIXI.Application({width: 256, height: 256})
const loader = PIXI.loader;
loader.add('character', character);
loader.load((loader, resources) => {
    console.log(resources);
    new Character(resources.character.texture);
});


document.body.appendChild(app.view);
