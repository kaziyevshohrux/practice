/*   A-task 

Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
MASALAN countLetter("e", "engineer") 3ni return qiladi.
*/


//Masala yechimi 
function countletter(harf, str){
    let count = 0 
   let a = str.split('')
   for (i=0 ; a.length>i ; i++){
    if(a[i]==harf){
        count++
    }
    
   }
   return count
}
console.log(countletter('g' , 'engeee'))
