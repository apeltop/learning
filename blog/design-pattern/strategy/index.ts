// 나열한 코드

// class KrLotto {
//     buyKr() {
//         console.log('Buy Kr Lotto');
//     }
// }
//
// class EnLotto {
//     buyEn() {
//         console.log('Buy En Lotto');
//     }
// }

interface ILotto {
    buy: () => void;
    checkDrawResult: () => void;
}

class KrLotto implements ILotto {
    buy(): void {
        console.log('Buy Kr Lotto');
    }

    checkDrawResult(): void {
        console.log('Check Kr Draw Result');
    }
}

class EnLotto implements ILotto {
    buy(): void {
        console.log('Buy En Lotto')
    }

    checkDrawResult(): void {
        console.log('Check En Draw Result');
    }
}

function createLotto(country: 'kr' | 'en') {
    return country === 'kr' ? new KrLotto() : new EnLotto();
}

const krLotto = createLotto('kr');
krLotto.buy();

const enLotto = createLotto('en');
enLotto.buy();

// function buyLotto(lotto: ILotto) {
//     lotto.buy();
// }
//
// buyLotto(new KrLotto());
