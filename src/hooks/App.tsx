import React, {useEffect, useState} from "react";
import {StyleSheet, SafeAreaView, Text} from "react-native";
import {useFonts, MajorMonoDisplay_400Regular} from '@expo-google-fonts/major-mono-display'

import AppLoading from 'expo-app-loading';

export default function App() {
    let [fontsLoaded] = useFonts({
        MajorMonoDisplay_400Regular
    })

    const [time, setTime] = useState(new Date())
    useEffect(() => {
        const id = setInterval(() => {
            setTime(new Date())
        }, 1000)

        return () => clearInterval(id)
    }, [])


    if (!fontsLoaded) {
        return <AppLoading/>
    } else {
        return (
            <SafeAreaView style={styles.safeAreaView}>
                <Text style={[styles.digitFont, styles.time]}>
                    {time.toLocaleTimeString()}
                </Text>

                <Text style={styles.digitFont}>
                    {time.toLocaleDateString()}
                </Text>
            </SafeAreaView>
        )
    }

}

const styles = StyleSheet.create({
    safeAreaView: {flex: 1, alignItems: 'center', justifyContent: 'center'},
    digitFont: {fontFamily: 'MajorMonoDisplay_400Regular', fontWeight: '400'},
    // digitFont: {},
    time: {fontSize: 50}
})