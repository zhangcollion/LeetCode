object Solution {
    def checkIfPangram(sentence: String): Boolean = {
        
        for (i <- 97 until 97+26){
            if(!sentence.contains(i)){
                return false
            }
        }
        true
    }
}