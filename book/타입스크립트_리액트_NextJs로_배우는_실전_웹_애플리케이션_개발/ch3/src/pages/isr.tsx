import {GetStaticProps, NextPage} from "next";
import {useRouter} from "next/router";
import Head from "next/head";

type ISRProps = {
    message: string;
}

const ISR: NextPage<ISRProps> = (props) => {
    const {message} = props;

    const router = useRouter();

    if (router.isFallback) {
        return <div>Loading...</div>
    }

    return (
        <div>
            <Head>
                <title>ISR</title>
                <link rel="icon" href="/favicon.ico"/>
            </Head>

            <main>
                <p>이 페이지는 ISR 을 통해 빌드 시 생성된 페이지입니다.</p>
                <p>{message}</p>
            </main>
        </div>
    )
}

export const getStaticProps: GetStaticProps = async (context) => {
    const timestamp = new Date().toLocaleString();
    const message = `${timestamp}에 getStaticProps가 호출되었습니다.`;
    console.log(message);

    return {
        props: {
            message
        },
        revalidate: 10
    }
}

export default ISR;
