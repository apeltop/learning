import {ApiContext} from "@/types";
import {fetcher} from "@/utils";

export type GetUserParams = {
    id: number;
}

const getUser = async (context: ApiContext, params: GetUserParams) => {
    return await fetcher(
        `${context.apiRootUrl.replace(/\/$/g, '')}/users/${params.id}`,
        {
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            }
        }
    )
}

export default getUser;
