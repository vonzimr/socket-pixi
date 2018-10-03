import io from 'socket.io-client';
import * as PIXI from 'pixi.js';
import character from './images/ph.png';


export const socket = new WebSocket('ws://localhost:5000/ws');
socket.binaryType = 'arraybuffer';

let players = {}

socket.addEventListener('message', function(event){
    let data = read_bits(event.data)
    let id = data['id']
    if(players[id]){
        let player = players[id];
        player.character.x = data['x'];
        player.character.y = data['y'];

    } else {
        loader.load((loader, resources) => {
            let otherPlayer = new OtherPlayer(resources.character.texture, data);
            players[otherPlayer.id] = otherPlayer;
        });
    }
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
    } else {
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

function send_bits(x, y){
    let bits = new ArrayBuffer(8)
    let dv = new DataView(bits)
    dv.setInt32(0, x, true)
    dv.setInt32(4, y, true)
    return bits
}

function read_bits(bits){
    let dv = new DataView(bits)
    let id = dv.getInt32(0, true)
    let x = dv.getInt32(4, true)
    let y = dv.getInt32(8, true)
    return {'id': id, 'x': x, 'y': y}
}

class OtherPlayer {
    constructor(sprite, data){
        this.sprite = sprite;
        this.x = data['x'];
        this.y = data['y'];
        this.id = data['id'] 
        this.setup(sprite);
    }

    setup(sprite){
        this.character = new PIXI.Sprite(sprite);
        app.stage.addChild(this.character);
    }
}


class Character {
    constructor(sprite){
        this.sprite = sprite;
        this.vel = 5;
        this.setup(sprite);
    }
    setup(sprite){
        this.character = new PIXI.Sprite(sprite);
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
        socket.send(send_bits(this.character.x, this.character.y))
    }

    ArrowDown(){
        this.character.y += this.vel;
        socket.send(send_bits(this.character.x, this.character.y))
    }
    ArrowLeft(){
        this.character.x -= this.vel;
        socket.send(send_bits(this.character.x, this.character.y))
    }
    ArrowRight(){
        this.character.x += this.vel;
        socket.send(send_bits(this.character.x, this.character.y))
    }


}

const app = new PIXI.Application({width: 256, height: 256})
const loader = PIXI.loader;
loader.add('character', character);
loader.load((loader, resources) => {
    new Character(resources.character.texture);
});


document.body.appendChild(app.view);
