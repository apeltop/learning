import {useEffect, useState} from "react";

function Sayhello() {
    const [data, setData] = useState({name: ''});

    useEffect(() => {
        fetch('/api/hello')
            .then((response) => response.json())
            .then((data) => setData(data));
    }, []);

    return <div>hello {data.name}</div>
}


export default Sayhello;
