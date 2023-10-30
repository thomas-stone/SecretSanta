import { Configuration, AuthApi, UserApi, GroupApi } from "../../generated";

export const configuration = new Configuration();

export const authApi = new AuthApi(configuration);
export const userApi = new UserApi(configuration);
export const groupApi = new GroupApi(configuration);
