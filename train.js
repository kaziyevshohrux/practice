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
// console.log(countDigit("ad2a54y79w4t0sfgb9"))



const animal_list = ["fox" , "ant" , "bird", "lion" , "dog", "goat"]

function findAnimal(txt){
    let a = txt.split('')
    let animals = []
    
        animal_list.forEach((ele) =>{
           let aa= ele.split('')
          const isMatch = aa.every((e) =>{
            return a.includes(e)
              })
                if(isMatch){
                    animals.push(ele)
                    animal_list.splice(animal_list.indexOf(ele),1)
          }}
        )
             
        

    
    return animals
}
        
console.log(findAnimal("ifoxdglnta"))
  



// const animal_list = ["fox" , "ant" , "bird", "lion" , "dog", "goat"]
// let animal = []
// function findAnimal(txt){
//     for (i=0; animal_list.length>i; i++){
//         let a = animal_list[i].split('')
//         let w=txt.split('')
//         console.log()
//         for(l=0; a.length>l; l++){
//             for(j=0 ; w.length>j;j++){
//                 if(w[j]==a[l]){
//                     animal.push(animal_list[i])
//                 }
            
//         }
//     }


// }
// return animal
// }

//const animal_list = ["fox" , "ant" , "bird", "lion" , "dog", "goat"]
// animals = [];
// function findAnimal(txt){
//     for (j=0; animal_list.length>j; j++){
//         let a = animal_list[j].split('')
//         for(l=0 ; a.length>l;l++){
//             w = txt.split('')
//             for (i=0 ; w.length>i ; i++){
//                 if(w[i]==a[l]){
//                     animals.push(animal_list[j])

//                 }
//                 }

        
//         }
       
//     }
//      return animals
    
// }



// console.log(findAnimal("dgoatlin"))