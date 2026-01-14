// Adapted from https://icodemag.com/how-to-build-a-login-register-app-with-the-mern-stack-part-5-connecting-frontend-to-backend/

import React, { Component } from 'react';

const UsersContext = React.createContext();

class UsersContextProvider extends Component {
    constructor(props) {
        super(props);
        this.state = {
            isLoggedIn: false,
            user: {},
            logUserIn: this.logUserIn,
            logUserOut: this.logUserOut,
            registerUser: this.registerUser,
            updateUser: this.updateUser,
            updatePhoto: this.updatePhoto,
        };
    }

    componentDidMount = async () => {
        const res = await fetch("/api/currentUser", {
            credentials: 'include',
        });
        const data = await res.json();

        const isLoggedIn = data.user ? true : false;
        const user = data.user ? data.user : {};
        this.setState({ isLoggedIn, user });
    }
    
    
    logUserIn = async (username, password) => {
        let title, text;
        
        const res = await fetch("/login", { // OR http://localhost:8081/login
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
            },
            credentials: 'include',
            method: 'POST',
            body: JSON.stringify({ username, password }),
        });
        
        const { user, statusCode: responseStatus } = await res.json();
        
        if (responseStatus === 422) {
            title = "Whoops!!";
            text = "Check username/password.";
        } else if (responseStatus === 204) {
            this.setState({
                isLoggedIn: true,
                user,
            });
            
            title = "Done";
            text ="You will get redirected to home page.";
        } else {
            title = "Whoops!";
            text = "There has been a hiccup. *hic* Please try again later.";
        }
        
        return { title, text };
    }

    registerUser = async (username, email, password, confirmPassword, firstname, lastname) => {
        // console.log("firing register user...");
        let title, text, registered;

        if (password.length < 4 || confirmPassword.length < 4 ) {
            title = "Whoops!!";
            text = "Password must have at least four characters.";
        } else if (password !== confirmPassword) {
            title = "Whoops!!";
            text = "Password and Confirm Password must match.";
        } else {
            const res = await fetch("/register", { // OR http://localhost:8081/register)
                headers: {
                    Accept: 'application/json',
                    'Content-Type': 'application/json',
                },
                credentials: 'include',
                method: 'POST',
                body: JSON.stringify({ username, email, password, firstname, lastname }),
            });

            const responseStatus = res.status;

            if (responseStatus === 409) {
                title = "Whoops!!";
                text = "Username already exists.";
            } else if (responseStatus === 201) {
                title = "Done";
                text = "Your account was created.";
                registered = true;
            } else {
                title = "Whoops!!";
                text = "Something went wrong. Try again later";
            }    
        }
        return { title, text, registered };
    };

    updatePhoto = async (photo) => {
        let title, text;
        console.log("updatePhoto: ", photo);
        const res = await fetch("/api/profile/update/photo", {
            credentials: 'include',
            method: 'PUT',
            body: photo,
        });
        const responseStatus = res.status;

        if (responseStatus === 200) {
            title = "Done";
            text = "Your photo was updated.";
        } else {
            title = "Whoops!!";
            text = "Something went wrong. Try again later";
        }    

        return { title, text };
    };

    updateUser = async (username, email, password, confirmPassword, firstname, lastname) => {
        let title, text;

        if ((password.length < 4 && password.length > 1 ) || (confirmPassword.length < 4 && confirmPassword.length > 1 )) {
            title = "Whoops!!";
            text = "Password must have at least four characters.";
        } else if (password !== confirmPassword) {
            title = "Whoops!!";
            text = "Password and Confirm Password must match.";
        } else {
            const res = await fetch("/api/profile/update", { // OR http://localhost:8081/register)
                headers: {
                    Accept: 'application/json',
                    'Content-Type': 'application/json',
                },
                credentials: 'include',
                method: 'PUT',
                body: JSON.stringify({ username, email, password, firstname, lastname }),
            });

            const responseStatus = res.status;

            if (responseStatus === 200) {
                title = "Done";
                text = "Your profile was updated.";
            } else {
                title = "Whoops!!";
                text = "Something went wrong. Try again later";
            }    
        }

        return { title, text };
        
    };
    
    logUserOut = async () => {
        await fetch('/logout', { // OR http://localhost:8081/register)
            credentials: 'include',
            method: 'POST',
        });

        this.setState({ isLoggedIn: false, user: {} })
    }

    render() {
        return (
            <UsersContext.Provider value={this.state}>
                {this.props.children}
            </UsersContext.Provider>
        )
    }
    
}
export { UsersContext, UsersContextProvider };

