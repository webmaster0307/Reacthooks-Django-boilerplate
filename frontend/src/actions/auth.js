import ROLE from '../../utils/constants/role';

export const isLoggedIn = state => () => {
    const isLoggedIn = !!state.currentUser.id;
    return isLoggedIn;
}