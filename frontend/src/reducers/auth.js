export default function authReducer(state, { type, payload }) {
    switch (type) {
        case "SIGNUP_SUCCESS":
            localStorage.setItem("token", payload.token);
            return {
                ...state,
                currentUser: payload,
                isAuth: true
            };
        case "LOGIN_SUCCESS":
            localStorage.setItem("token", payload.token);
            delete payload.token;
            localStorage.setItem("user", JSON.stringify(payload));
            return {
                ...state,
                currentUser: payload,
                isAuth: true
            };
        case "SIGNOUT_USER":
            localStorage.removeItem("token");
            localStorage.removeItem("user");
            console.log("this is the current user", state.currentUser);
            return {
                ...state,
                currentUser: null,
                isAuth: false
            };
        default:
            return state;
    }
}