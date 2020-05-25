import collections


class BiDirectionalBFS:
    def __init__(self, start, end, word_list):
        self.start = start
        self.end = end
        self.is_finished = False
        self.no_path_found = True
        self.word_list = word_list
        self.queue = collections.deque()
        self.visited = set()
        self.queue.append((start, []))
        self.paths = {}
    
    def build_words(self, old_word):
        word_len = len(old_word)
        word_list = []
        for j in range(0,word_len):
            for i in range(97, 123):
                lst_word = list(old_word)
                lst_word[j] = chr(i)
                new_word = ''.join(lst_word)
                if new_word in self.word_list and \
                        new_word not in self.visited:
                    word_list.append(new_word)
        return word_list
    
    def find_next_path(self):
        if not self.queue:
            self.is_finished = True
            return None
            
        item = self.queue.popleft()
        word, path = item
        self.visited.add(word)
        path.append(word)
        self.paths[word] = path
        if self.end == word:
            self.paths[word] = path
            self.is_finished = True
            self.no_path_found = False
            
        words = self.build_words(word)
        for w in words:
            self.queue.append((w,path))
        return word
    
    def get_path_if_word_visited(self, word):
        if word in self.visited:
            return self.paths[word]
        return []
    
    
def word_transformed_BD_BFS(start, stop, word_list):
    start_word = BiDirectionalBFS(start, stop, word_list)
    end_word = BiDirectionalBFS(stop, start, word_list)
    
    while not (start_word.is_finished and end_word.is_finished):
        last_word = start_word.find_next_path()
        last_word2 = end_word.find_next_path()
        
        path = start_word.get_path_if_word_visited(last_word2)
        if len(path) != 0:
            path2 = end_word.paths[last_word2]
        else:
            path2 = end_word.get_path_if_word_visited(last_word)
            if len(path2) != 0:
                path = start_word.paths[last_word]

        if len(path) != 0 and len(path2) != 0:
            merge_path = []
            for word in path:
                merge_path.append(word)
            for i in range(len(path2)-1, -1, -1):
                if path2[i] not in merge_path:
                    merge_path.append(path2[i])
            return merge_path
    return []
        
    
def word_transformed(start, stop, word_dictionary):
    def build_words(old_word, word_visited):
        word_len = len(old_word)
        word_list = []
        for j in range(0,word_len):
            for i in range(97, 123):
                lst_word = list(old_word)
                lst_word[j] = chr(i)
                new_word = ''.join(lst_word)
                if new_word in word_dictionary and \
                        new_word not in word_visited:
                    word_list.append(new_word)
        return word_list

    queue = collections.deque()
    visited = set()
    queue.append((start, []))
    while queue:
        item = queue.popleft()
        node, path = item
        visited.add(node)
        path.append(node)
        if node == stop:
            return path
        words = build_words(node, visited)
        for word in words:
            queue.append((word, path))

    return None


def test_word_transform():
    word_dictionary = ["maps", "tan", "tree", "apple", "cans", "help", "aped", "pree", "pret", "apes", "flat", "trap", "fret", "trip", "trie", "frat", "fril"]
    result = word_transformed('tree','flat', word_dictionary)
    print(result)
    result = word_transformed_BD_BFS('tree', 'flat', word_dictionary)
    print(result)


test_word_transform()


