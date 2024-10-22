export const fetcher = async (
    resource: RequestInfo,
    init?: RequestInit
): Promise<Response> => {
    const res = await fetch(resource, init);

    if (!res.ok) {
        const errorRes = await res.json();
        const error = new Error(` ${res.status} ${errorRes.message}`);
        throw error;
    }

    return res.json();

}
