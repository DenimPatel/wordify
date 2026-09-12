/**
 * Trie data structure, ported from algorithm/trie.py.
 */
class TrieNode {
  constructor() {
    this.children = new Array(26).fill(null);
    this.isEndOfWord = false;
  }
}

class Trie {
  constructor() {
    this.root = new TrieNode();
  }

  static charToIndex(character) {
    return character.charCodeAt(0) - 'a'.charCodeAt(0);
  }

  insert(key) {
    let currentNode = this.root;
    for (let level = 0; level < key.length; level++) {
      const index = Trie.charToIndex(key[level]);
      if (!currentNode.children[index]) {
        currentNode.children[index] = new TrieNode();
      }
      currentNode = currentNode.children[index];
    }
    currentNode.isEndOfWord = true;
  }

  search(key) {
    let currentNode = this.root;
    for (let level = 0; level < key.length; level++) {
      const index = Trie.charToIndex(key[level]);
      if (!currentNode.children[index]) {
        return false;
      }
      currentNode = currentNode.children[index];
    }
    return currentNode !== null && currentNode.isEndOfWord;
  }

  searchMultiWords(key) {
    key = key.toLowerCase();
    let currentNode = this.root;
    let tempAns = false;
    for (let level = 0; level < key.length; level++) {
      const index = Trie.charToIndex(key[level]);
      if (!currentNode.children[index]) {
        return false;
      }
      currentNode = currentNode.children[index];
      if (currentNode.isEndOfWord) {
        if (level !== key.length - 1) {
          tempAns = this.searchMultiWords(key.slice(level + 1));
          if (tempAns) {
            return true;
          }
        }
      }
    }
    return currentNode !== null ? currentNode.isEndOfWord : tempAns;
  }
}
