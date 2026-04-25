// E-TASK (NodeJS)

// Shunday function tuzing, u bitta string argumentni qabul qilib osha stringni teskari qilib return qilsin.
// MASALAN: getReverse("hello") return qilsin "olleh"

function getreverse(word){
    return word.split('').reverse().join('')
}
console.log(getreverse('hellou'))




















//D-TASK (NodeJS)

//Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
//MASALAN: getHighestIndex([5, 21, 12, 21, 8]) return qiladi 1 sonini.


 // 1-yechim

// function getHighIndex(num){
//     //console.log(...num) 
//     return max = Math.max(...num)
// }
// console.log(getHighIndex([5, 21, 12, 21, 8]))

// // 2- yechim 

// function hn(numbs){
//     a = numbs[0]
//     for (i=0; numbs.length>i; i++){
//         if(numbs[i]>a)
//             a=numbs[i]
//     }
//     return a
// }
// console.log(hn([5, 21, 22, 21, 8]))



// let mix = [1,2,[45,65,7],87]

// console.log(...mix)



















//  C-TASK 


//Shunday function tuzing, u 2ta string parametr ega bolsin, hamda agar har ikkala string bir hil harflardan iborat bolsa true aks holda false qaytarsin
//MASALAN checkContent("mitgroup", "gmtiprou") return qiladi true;

//masala yechimi 
 
// function text(word , input_word){
//    let a= word.split('')
//    let c= input_word.split('')
//     return last= a.every((ele)=> c.includes(ele))

    
// }

// console.log(text('aaarrvs', 'sarvaar'))















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


//console.log("=============================================")


//   B-task

//Shunday function tuzing, u 1ta string parametrga ega bolsin, hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.
//MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.
// count = [];
// numbers = [0,1,2,3,4,5,6,7,8,9]
// function countDigit(numabs){
//     numabs.split('')
//     for(i=0; numbers.length>i;i++){
//         for (j=0; numabs.length>j; j++){
//             if (numbers[i]==numabs[j]){
//                 count.push(numbers[i])
//             }
//         }
//     }
//     return count.length
// }
// console.log(countDigit("ad2a5 4y79w4t0sfgb9"))


console.log("=============================================")



// Challenge task

// const animal_list = ["fox" , "ant" , "bird", "lion" , "dog", "goat"]

// function findAnimal(txt){
//     let a = txt.split('')
    //console.log(a)
//     let animals = []
//     animal_list.forEach((ele) =>{
//         let aa= ele.split('')
//         //console.log(aa)
//           const isMatch = aa.every((e) =>{
//             return a.includes(e)
//               })
//                 if(isMatch){
//                     animals.push(ele)
                    
//                 }
//             }
//         )
//         return animals
//     }
        
// console.log(findAnimal("ifoxdglnta"))
  



//   challenge 2-usul

// const animal_list = ["fox" , "ant" , "bird", "lion" , "dog", "goat"]

// function findAnimal(txt){
//     let a = txt.split('')
//    return animal_list.filter((ele) =>{
//         let aa= ele.split('')
//           return isMatch = aa.every((e) => a.includes(e) )
//         }
//     )
// }
        
// console.log(findAnimal("ilon"))







//  C - task 


//  masala sharti 

//  C-TASK 

//Shunday function tuzing, u 2ta string parametr ega bolsin, hamda agar har ikkala string bir hil harflardan iborat bolsa true aks holda false qaytarsin
//MASALAN checkContent("mitgroup", "gmtiprou") return qiladi true;

//masala yechimi 

// function text(word , input_word){
//    let a= word.split('')
//    let c= input_word.split('')
//     return last= a.every((ele)=> c.includes(ele))

    
// }

// console.log(text('aaarrvs', 'sarvaar'))





