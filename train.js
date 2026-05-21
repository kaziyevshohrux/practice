// P-TASK (NodeJS)

// Shunday function yozing, u object qabul qilsin va arrayni object arrayga otkazib arrayni qaytarsin qaytarsin.
// MASALAN: objectToArray( {a: 10, b: 20}) return [['a', 10], ['b', 20]]
function objectToArray(obj){
    let result = [];
    for (let i = 0; Object.keys(obj).length > i; i++){
        let key = Object.keys(obj)[i];
        result.push([key, obj[key]]);
    }
    return result;
}
console.log(objectToArray({a: 10, b: 20}))

// N-TASK (NodeJS)

// Shunday function yozing, u raqamlardan tashkil topgan array qabul qilsin va array ichidagi har bir raqam uchun raqamni ozi va hamda osha raqamni kvadratidan tashkil topgan object hosil qilib, hosil bolgan objectlarni array ichida qaytarsin.
// MASALAN: getSquareNumbers([1, 2, 3]) return [{number: 1, square: 1}, {number: 2, square: 4}, {number: 3, square: 9}];

// function getSquareNumbers(nums){
//     l=[]
//     for (i=0; nums.length>i; i++){
//         l.push({number: nums[i],
//                 square: nums[i]**2})
//     }
//     return l

// }

// console.log(getSquareNumbers([1,2,3,4]))










// L-TASK (NodeJS)

// Shunday function yozing, u string qabul qilsin va string ichidagi hamma sozlarni chappasiga yozib va sozlar ketma-ketligini buzmasdan stringni qaytarsin.
// MASALAN: reverseSentence("we like coding!") return "ew ekil gnidoc"

// function reverseSentence(gap){
//     return gap.split(" ").map((ele) => ele.split("").reverse().join('')).join(' ')

// }

// console.log(reverseSentence("we like coding!"))

// // J-TASK (NodeJS)

// // Shunday function yozing, u parametridagi array ichida eng kop takrorlangan raqamni topib qaytarsin.
// // MASALAN: majorityElement([1,2,3,4,5,4,3,4]) return 4


// function majorityElement(arr){
//     result={}
//     let count = 0
//     let ele = null
//     for (i=0; arr.length>i;i++){
//         let every=arr[i]
//         if(result[arr[i]]){
           
//             result[every]++
//         }else{
//             result[every]=1
//         }
//         if (result[every]>count){
//             count=result[every]
//             ele = every
//         }
        
//     }
//     return ele
// }
// console.log(majorityElement([1,2,3,4,5,4,3,4,5,5,5]))








// // H-TASK (NodeJS)

// // shunday function tuzing, u integerlardan iborat arrayni argument sifatida qabul qilib, faqat positive qiymatlarni olib string holatda return qilsin
// // MASALAN: getPositive([1, -4, 2]) return qiladi "12"


// function getpos(arr){
//     return arr.filter((ele)=> ele>0).join('')
// }
// console.log(getpos([1,-4,12]))






















// F-TASK (NodeJS)

// Shunday findDoublers function tuzing, unga faqat bitta string argument pass bolib, agar stringda bir hil harf qatnashgan bolsa true, qatnashmasa false qaytarishi kerak.
// MASALAN: getReverse("hello") return true return qiladi


// function getReverse(word){
//     a = word.split('')
//     let set = new Set(a)
//     if(a.length > set.size){
        
//         return true
//     }else{
//         return false
//     }
// }
// console.log(getReverse('helo'))















// E-TASK (NodeJS)

// Shunday function tuzing, u bitta string argumentni qabul qilib osha stringni teskari qilib return qilsin.
// MASALAN: getReverse("hello") return qilsin "olleh"

// function getreverse(word){
//     return word.split('').reverse().join('')
// }
// <<<<<<< HEAD
// console.log(getreverse('hellou'))
// =======
// console.log(getreverse('salom'))
// >>>>>>> 70f177d532444e326c50ff3b43e593c9b510da01




//   text = "banana"  

// function word(txt){
//     let result = {}
//    // let split_text = txt.split('')
//     //console.log(split_text)
//     for (i=0; txt.length>i; i++){
//         let every = txt[i]
//         if(result[every]){
//             result[every]++
//         }else{
//             result[every] = 1
//         }
//     }
//     return result
// }

// console.log(word('banana'))




// target = 18
// def like(nums):
//     for i in nums:
//         cur = target - i
//         if cur in nums:
//             result=(i , cur)
//     return result
// print(like([2,7,15,14,3]))















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





