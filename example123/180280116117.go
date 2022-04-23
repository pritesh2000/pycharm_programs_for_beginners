package main

import (
	"bytes"
	"crypto/sha256"
	"fmt"
)

type Block struct {
	Hash     []byte
	Data     []byte
	PrevHash []byte
}

type BlockChain struct {
	blocks []*Block
}

func CreateBlock(data string, prevHash []byte) *Block {
	block := &Block{[]byte{}, []byte(data), prevHash}
	block.CreateHash()
	return block
}

func (b *Block) CreateHash() {
	info := bytes.Join([][]byte{b.Data, b.PrevHash}, []byte{})
	hash := sha256.Sum256(info)
	b.Hash = hash[:]
}

func (chain *BlockChain) AddBlock(data string) {
	PrevBlock := chain.blocks[len(chain.blocks)-1]
	new := CreateBlock(data, PrevBlock.Hash)
	chain.blocks = append(chain.blocks, new)
}

func Genesis() *Block {
	return CreateBlock("Genesis", []byte{})
}
func InitBlockchain() *BlockChain {
	return &BlockChain{[]*Block{
		Genesis()}}
}
func Reverse(s string) string {
	r := []rune(s)
	for i, j := 0, len(r)-1; i < len(r)/2; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}
	return string(r)
}
func main() {
	chain := InitBlockchain()

	chain.AddBlock(Reverse("ishika's First Block"))
	chain.AddBlock(Reverse("ishika's Second Block"))
	chain.AddBlock(Reverse("ishika's Third Block"))
	for _, block := range chain.blocks {
		fmt.Printf("prevHash: %x\n", block.PrevHash)
		fmt.Printf("block data: %s\n", block.Data)
		fmt.Printf("block hash: %x\n", block.Hash)
		fmt.Printf("\n\n")
	}
}
