export default function userReducer(state, { type, payload }) {
    switch (type) {
        /** userlist */
        case "SET_USERS":
            return {
                ...state,
                users: payload
            };
        case "CREATE_USER_SUCCESS":
            return {
                ...state,
                users: state.users.filter(u => u._id !== payload._id).concat(payload)
            };

        case "UPDATE_USER_SUCCESS":
            const { users } = state;
            const index = users.findIndex(u => u._id === payload._id);
            users[index] = payload;
            return {
                ...state,
                users
            };

        case "DELETE_USER_SUCCESS":
            state.users.splice(
                state.users.findIndex(u => u._id === payload._id),
                1
            );
            return {
                ...state
            };

        default:
            return state;
    }
}
