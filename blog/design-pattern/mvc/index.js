const database = {
    user: [
        {
            name: 'foo',
            age: 20,
            country: 'kr',
            lastModified: '2022-06-11T11:40:38.736Z',
        },
        {
            name: 'bar',
            age: 30,
            country: 'kr',
            lastModified: '2022-06-10T11:40:38.736Z',
        },
        {
            name: 'zoo',
            age: 40,
            country: 'uk',
            lastModified: '2022-06-19T11:40:38.736Z',
        },
    ]
};

// 한국인이면 만 나이로 2살을 없애준다는 예제
// const Controller = () => {
//     const users = database.user;
//     const usersByCountryKr = [];
//     for (const user of users) {
//         if (user.country === 'kr') {
//             usersByCountryKr.push(user);
//         }
//     }
//
//     for (const userKr of usersByCountryKr) {
//         userKr.age -= 2;
//         userKr.lastModified = new Date().toISOString();
//     }
//
//     for (const user of database.user) {
//         console.log(`이름 : ${user.name}`)
//         console.log(`나이 : ${user.age}`)
//         console.log(`국가 : ${user.country}`)
//         console.log(`최종 수정 일자 : ${user.lastModified}`)
//         console.log(`-------------`)
//     }
// }

// const Controller = () => {
//     database.user
//         .filter(({country}) => country === 'kr')
//         .map(user => {
//             user.age -= 2;
//             user.lastModified = new Date().toISOString();
//         });
//
//     for (const user of database.user) {
//         console.log(`이름 : ${user.name}`)
//         console.log(`나이 : ${user.age}`)
//         console.log(`국가 : ${user.country}`)
//         console.log(`최종 수정 일자 : ${user.lastModified}`)
//         console.log(`-------------`)
//     }
// }


const Model = {
    getUserList: () => {
        return database.user;
    },
    selectByCountry: (countryId) => {
        return database.user
            .filter(({country}) => country === countryId);
    },
    incrementAge: (users, amount) => {
        for (const user of users) {
            user.age += amount;
            user.lastModified = new Date().toISOString();
        }
    }
}

const View = {
    userList: (users) => {
        for (const user of users) {
            console.log(`이름 : ${user.name}`)
            console.log(`나이 : ${user.age}`)
            console.log(`국가 : ${user.country}`)
            console.log(`최종 수정 일자 : ${user.lastModified}`)
            console.log(`-------------`)
        }
    }
}

const Controller = () => {
    // const usersByCountryKr = Model.selectByCountry('kr')
    Model.incrementAge(Model.selectByCountry('kr'), -2);
    View.userList(Model.getUserList());
}


Controller();
