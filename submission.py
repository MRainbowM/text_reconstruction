from typing import Callable, List, Set

import shell
import util
import wordsegUtil


############################################################
# Problem 1b: Solve the segmentation problem under a unigram model

class SegmentationProblem(util.SearchProblem):

    def __init__(self, query: str, unigramCost: Callable[[str], float]):
        self.query = query
        self.unigramCost = unigramCost

    def startState(self):
        """Возвращает начальное состояние"""
        return self.query

    def isEnd(self, state) -> bool:
        """Проверяет, является ли состояние конечным"""
        return len(state) == 0

    def succAndCost(self, state):
        """Принимает на вход состояние.
        Возвращает массив кортежей, состоящих из:
        - действия, слова (action);
        - нового состояния (result);
        - стоимости действия (cost)"""
        result = []

        if len(state) > 0:
            for i in range(len(state), 0, -1):
                action = state[:i]
                remainder = state[len(action):]  # оставшийся текст
                result.append((action, remainder, self.unigramCost(action)))
        print('---')
        print(result)
        print('---')
        return result


def segmentWords(query: str, unigramCost: Callable[[str], float]) -> str:
    if len(query) == 0:
        return ''

    ucs = util.UniformCostSearch(verbose=0)
    ucs.solve(SegmentationProblem(query, unigramCost))
    print(ucs.totalCost)
    return ' '.join(ucs.actions)


############################################################
# Problem 2b: Solve the vowel insertion problem under a bigram cost

class VowelInsertionProblem(util.SearchProblem):
    def __init__(self, queryWords: List[str], bigramCost: Callable[[str, str], float],
                 possibleFills: Callable[[str], Set[str]]):
        self.queryWords = queryWords
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def startState(self):
        # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
        raise Exception("Not implemented yet")
        # END_YOUR_CODE

    def isEnd(self, state) -> bool:
        # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
        raise Exception("Not implemented yet")
        # END_YOUR_CODE

    def succAndCost(self, state):
        # BEGIN_YOUR_CODE (our solution is 8 lines of code, but don't worry if you deviate from this)
        raise Exception("Not implemented yet")
        # END_YOUR_CODE


def insertVowels(queryWords: List[str], bigramCost: Callable[[str, str], float],
                 possibleFills: Callable[[str], Set[str]]) -> str:
    # BEGIN_YOUR_CODE (our solution is 3 lines of code, but don't worry if you deviate from this)
    raise Exception("Not implemented yet")
    # END_YOUR_CODE


############################################################
# Problem 3b: Solve the joint segmentation-and-insertion problem

class JointSegmentationInsertionProblem(util.SearchProblem):
    def __init__(self, query: str, bigramCost: Callable[[str, str], float],
                 possibleFills: Callable[[str], Set[str]]):
        self.query = query
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def startState(self):
        return 0, wordsegUtil.SENTENCE_BEGIN  # position before which text is reconstructed & previous word

    def isEnd(self, state) -> bool:
        return state[0] == len(self.query)

    def succAndCost(self, state):
        results = []
        position, prev_word = state
        #print(state)
        for l in range(1, len(self.query) - position + 1):
            part = self.query[position:position + l]
            collection = self.possibleFills(part)

            #print("!!!!!!!" + str(part))
            # print(self.possibleFills('f'))
            #  print('collection')
            #  print(collection)
            for word in collection:
                action = word
                new_state = (position + l, word)
                cost = self.bigramCost(prev_word, word)
                results.append((action, new_state, cost))
       # print(results)
        return results


def segmentAndInsert(query: str, smoothCost: Callable[[str, str], float],
                     possibleFills: Callable[[str], Set[str]]) -> str:
    if len(query) == 0:
        return ''

    ucs = util.UniformCostSearch(verbose=0)
    ucs.solve(JointSegmentationInsertionProblem(query, smoothCost, possibleFills))

    print(ucs.actions)
    print(ucs.totalCost)

    return ' '.join(ucs.actions)


############################################################

if __name__ == '__main__':
    shell.main()
