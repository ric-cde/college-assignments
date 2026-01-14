import Card from 'react-bootstrap/card';
import { UsersContext } from './contexts/Users';
import { Component } from 'react';
import { Redirect } from 'react-router-dom';
import SweetAlert from 'sweetalert-react';
import 'sweetalert/dist/sweetalert.css';

// adapted from https://getbootstrap.com/docs/4.0/components/forms/

class Register extends Component {
    static contextType = UsersContext;

    // state & form handling methods adapted from https://icodemag.com/how-to-build-a-login-register-app-with-the-mern-stack-part-4-setting-up-frontend-routes/
    
    state = {
        username: '',
        email: '',
        password: '',
        confirmPassword: '',
        firstname: '',
        lastname: '',
        registered: false,
        alert: {
          showAlert: false,
          title: '',
          text: '',
        },
      };

    handleFormSubmit = async (event) => {
        event.preventDefault();
        const { username, email, password, confirmPassword, firstname, lastname } = this.state;
    
        const { title, text, registered } = await this.context.registerUser(
          username,
          email,
          password,
          confirmPassword,
          firstname,
          lastname,
        );

        if (registered) alert('Account created!');
    
        this.setState({
          registered,
          alert: {
            showAlert: true,
            title,
            text,
          },
        });
    };

    handleInputChange = (event) => {
        this.setState({
          [event.target.name]: event.target.value,
        });
      };


    render() {
        console.log("registered", this.state.registered);
        if (this.state.registered) {
            this.setState({ registered: false });           
            return <Redirect to="/login" />;
        } else if (!this.context.isLoggedIn) {
            const { showAlert, title, text } = this.state.alert;

            return (
                <div className="w-100 h-100">
                    <SweetAlert
                        show={showAlert}
                        title={title}
                        text={text}
                        onConfirm={() => this.setState({ alert: { showAlert: false } })}
                    />
                    <h1 className="page-title bg-success">Register</h1>
                    <div className="d-flex h-75">
                        <Card className="my-auto mx-auto shadow-lg p-3 mb-5 bg-white rounded">
                            <Card.Body>
                            <form  onSubmit={this.handleFormSubmit} > {/*  className="" action="/register" method="post" */}
                                <div className="form-group row">
                                    <label htmlFor="InputUsername" className="col-sm-4 col-form-label">Username:</label>
                                    <div className="col-sm-8">
                                        <input type="text" className="form-control" id="InputUsername" pattern="^\S{1,30}"
                                        aria-describedby="inputHelp" name="username" placeholder="Enter username" 
                                        value={this.state.username} onChange={this.handleInputChange} required />
                                        <small id="inputHelp" className="form-text text-muted">Choose a handle with no spaces</small>
                                    </div>    
                                </div>
                                <div className="form-group row">
                                    <label htmlFor="InputEmail" className="col-sm-4 col-form-label">Email:</label>
                                    <div className="col-sm-8">
                                        <input type="email" name="email" className="form-control" id="InputEmail" pattern="^\S{1,30}"
                                        value={this.state.email} onChange={this.handleInputChange} placeholder="Enter your email" required />
                                    </div>
                                </div>
                                <div className="form-group row">
                                    <label htmlFor="InputPassword" className="col-sm-4 col-form-label">Password:</label>
                                    <div className="col-sm-8">
                                        <input type="password" name="password" className="form-control" id="InputPassword" pattern="^\S{1,30}"
                                        value={this.state.password} onChange={this.handleInputChange} placeholder="Enter a password" required />
                                    </div>
                                </div>
                                <div className="form-group row">
                                    <label htmlFor="InputConfirmPassword" className="col-sm-4 col-form-label">Password:</label>
                                    <div className="col-sm-8">
                                        <input type="password" name="confirmPassword" className="form-control" id="InputConfirmPassword" pattern="^\S{1,30}"
                                        value={this.state.confirmPassword} onChange={this.handleInputChange} placeholder="Confirm your password" required />
                                    </div>
                                </div>
                                <div className="form-group row">
                                    <label htmlFor="InputFname" className="col-sm-4 col-form-label">First name:</label>
                                    <div className="col-sm-8">
                                        <input type="text" name="firstname" className="form-control" id="InputFname" 
                                        value={this.state.firstname} onChange={this.handleInputChange} placeholder="Enter your first name" required />
                                    </div>
                                </div>
                                <div className="form-group row">
                                    <label htmlFor="InputLname" className="col-sm-4 col-form-label">Last name:</label>
                                    <div className="col-sm-8">
                                        <input type="text" name="lastname" className="form-control" id="InputLname" 
                                        value={this.state.lastname} onChange={this.handleInputChange} placeholder="Enter your last name" required />
                                </div>
                                </div>
                                <button type="submit" className="btn btn-primary w-100">Sign up</button>
                            </form>
                            </Card.Body>
                        </Card>
                        </div>
                </div>
                )
            }

        return <Redirect to="/" />;
    }
}

export default Register;