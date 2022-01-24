import {SafeAreaView, Text, View} from 'react-native';
import * as D from './src/data';
import Main from './src/hooks/App'

const person = D.createRandomPerson();

export default function App() {
    return (
        <Main/>
    )
}