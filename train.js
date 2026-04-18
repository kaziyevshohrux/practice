/*   A-task 

Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
MASALAN countLetter("e", "engineer") 3ni return qiladi.
*/


//Masala yechimi 
// function countletter(harf, str){
//     let count = 0 
//    let a = str.split('')
//    for (i=0 ; a.length>i ; i++){
//     if(a[i]==harf){
//         count++
//     }
    
//    }
//    return count
// }
// console.log(countletter('n' , 'engeeenneer'))





//   B-task

//Shunday function tuzing, u 1ta string parametrga ega bolsin, hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.
//MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.
count = [];
numbers = [0,1,2,3,4,5,6,7,8,9]
function countDigit(numabs){
    numabs.split('')
    for(i=0; numbers.length>i;i++){
        for (j=0; numabs.length>j; j++){
            if (numbers[i]==numabs[j]){
                count.push(numbers[i])
            }
        }
    }
    return count.length
}
console.log(countDigit("ad2a54y79w4t0sfgb9"))