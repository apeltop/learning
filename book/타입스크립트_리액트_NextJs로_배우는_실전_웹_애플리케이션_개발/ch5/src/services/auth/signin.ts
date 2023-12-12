import {ApiContext} from "@/types";
import {fetcher} from "@/utils";

export type SigninParams = {
    username: string;
    password: string;
}

const signin = async (
    context: ApiContext,
    params: SigninParams
) => {
    return await fetcher(
        `${context.apiRootUrl}/auth/signin`,
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            body: JSON.stringify(params)
        }
    )
}

export default signin;
