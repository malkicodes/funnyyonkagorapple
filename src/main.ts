import './style.css'
import { data } from './data'

const WIDTH = 24
const HEIGHT = 18
const FPS = 16

const cells: HTMLImageElement[] = []
const cellContainer = document.querySelector('main')

for (let y = 0; y < HEIGHT; y++) {
  for (let x = 0; x < WIDTH; x++) {
    const cell = document.createElement('img')
    cell.setAttribute('src', "/funnyyonkagormemes.jpg")
    cell.style.setProperty("visibility", "hidden")

    cells.push(cell)
    cellContainer!.appendChild(cell)
  }
}

let currentFrame = 0

function pushFrame() {
  for (let y = 0; y < HEIGHT; y++) {
    const rowI = currentFrame * HEIGHT + y
    let row = data[rowI]

    for (let x = 1; x < WIDTH + 1; x++) {
      const isOn = row % 2 == 1

      cells[(y + 1) * WIDTH - x].style.setProperty("visibility", isOn ? "visible" : "hidden")

      row >>= 1
    }
  }

  currentFrame++
}

document.querySelector('button')!.addEventListener('click', () => {
  document.querySelector('button')?.remove()

  document.querySelector('audio')?.play()
  
  setInterval(() => {
    pushFrame()
  }, 1000 / FPS);
})

