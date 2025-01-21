function continueSequence(sequence){
    sequence+=' '
    returned_str=''
    counter=1
    for (i=1;i<sequence.length;i++) {
        if (sequence[i] == sequence[i-1] && i != sequence.length){
            counter+=1}
        else
        {
            returned_str += counter.toString() + sequence[i-1]
            counter=1
        }
    }
    return returned_str
}
console.log(continueSequence('111221'))