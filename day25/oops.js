// let employee = {
//     baseSalary : 30_000,
//     overtime : 10,
//     rate : 20,
//     getWage: function(){
//         return this.baseSalary+(this.overtime*this.rate)
//     }
// };

// employee.getWage()

//objects
const circle={
    radius:1 ,
    location:{
        x:1,
        y:1
    },
    draw : function(){
        console.log('draw');
    }
}

//factory func
function createCircle(r){
    return{
        r,
        gi : function(){
            console.log("Gii ra babu")
        }
    };
}
const cir = createCircle(1)

//constructor func

function Circle(l){
    this.l = l;
    this.wow = function(){
        console.log("lol");
    }
}

const plz = new Circle(1);