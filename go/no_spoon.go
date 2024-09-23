package main

import (
	"bufio"
	"fmt"
	"os"
)

func findNeighbors(grid [][]rune) [][6]int {
	height := len(grid)
	width := len(grid[0])
	var nodes [][2]int

	for y := 0; y < height; y++ {
		for x := 0; x < width; x++ {
			if grid[y][x] == '0' {
				nodes = append(nodes, [2]int{x, y})
			}
		}
	}

	var results [][6]int

	for _, node := range nodes {
		nodeX, nodeY := node[0], node[1]

		rightX, rightY := -1, -1
		for x := nodeX + 1; x < width; x++ {
			if grid[nodeY][x] == '0' {
				rightX = x
				rightY = nodeY
				break
			}
		}

		bottomX, bottomY := -1, -1
		for y := nodeY + 1; y < height; y++ {
			if grid[y][nodeX] == '0' {
				bottomX = nodeX
				bottomY = y
				break
			}
		}
		results = append(results, [6]int{nodeX, nodeY, rightX, rightY, bottomX, bottomY})
	}
	return results
}

func main() {

	var width, height int
	fmt.Scan(&width, &height)

	grid := make([][]rune, height)
	scanner := bufio.NewScanner(os.Stdin)
	for i := 0; i < height; i++ {
		if scanner.Scan() {
			grid[i] = []rune(scanner.Text())
		}
	}
	neighbors := findNeighbors(grid)
	for _, node := range neighbors {
		fmt.Printf("%d %d %d %d %d %d\n", node[0], node[1], node[2], node[3], node[4], node[5])
	}
}
