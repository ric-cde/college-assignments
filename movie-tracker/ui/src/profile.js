import Card from 'react-bootstrap/card';
import { UsersContext } from './contexts/Users';
import { Component } from 'react';
import { Redirect } from 'react-router-dom';
import SweetAlert from 'sweetalert-react';
import 'sweetalert/dist/sweetalert.css';

// Uploading photo adapted form https://flaviocopes.com/how-to-upload-files-fetch/ and https://dev.to/yosraskhiri/how-to-upload-an-image-using-mern-stack-1j95

class Profile extends Component {
    static contextType = UsersContext;

    constructor(props) {
        super(props);
        this.state = {
            username: '',
            email: '',
            password: '',
            confirmPassword: '',
            firstname: '',
            lastname: '',
            photo: '',
            currentphoto: '',
            alert: {
              showAlert: false,
              title: '',
              text: '',
            }
      }
    }

    // state & form handling methods adapted from https://icodemag.com/how-to-build-a-login-register-app-with-the-mern-stack-part-4-setting-up-frontend-routes/
    
    componentDidMount() {
    if (this.context.isLoggedIn) {
        const url = "/api/profile";
        try {
            fetch(url)
                .then((res) => res.json())
                .then((res) => {
                    // console.log(res);
                    const { username, email, firstname, lastname, photo } = res.user;
                    const currentphoto = photo;
                    this.setState({ username, email, firstname, lastname, currentphoto });
                });
        } catch (error) {
            console.log(error);
        }
    }
    }

    handleFormSubmit = async (event) => {
        event.preventDefault();
        const { username, email, password, confirmPassword, firstname, lastname } = this.state;
        const { title, text } = await this.context.updateUser(
          username,
          email,
          password,
          confirmPassword,
          firstname,
          lastname,
        );

        console.log(text);
        
        this.setState({
          alert: {
            showAlert: true,
            title,
            text,
          },
        });
    };

    handlePhoto = (event) => {
        this.setState({
            photo: event.target.files[0],
        //   [event.target.name]: event.target.value,
        });
      };

    handlePhotoSubmit = async (event) => {
        event.preventDefault();
        const { photo } = this.state;
        // console.log(photo);
        const formData = new FormData();
        formData.append('photo', photo);
        // console.log(formData); 

        const { title, text } = await this.context.updatePhoto(formData);

        this.setState({
            alert: {
              showAlert: true,
              title,
              text,
            },
          });
    }

    handleInputChange = (event) => {
        this.setState({
          [event.target.name]: event.target.value,
        });
      };

    render() {
        // console.log("showAlert", this.state.alert.showAlert);
        if (this.context.isLoggedIn) {
            return (
                <div className="w-100 h-100">
                <h1 className="page-title bg-success">Profile</h1>
                    <SweetAlert
                        show={this.state.alert.showAlert}
                        title={this.state.alert.title}
                        text={this.state.alert.text}
                        onConfirm={() => this.setState({ alert: { showAlert: false } })}
                    />
                    <br /><p className="lead text-center">How would you like to update your profile?</p>
                    <div className="d-flex row mb-3">
                        <Card className="my-auto mx-auto shadow-lg p-3 bg-white rounded">
                        <img className="img-thumbnail rounded mx-auto" width="300px" alt="" src={ 
                                this.state.currentphoto && "data:" + this.state.currentphoto.mimetype + ";base64, " + this.state.currentphoto.data
                                } />
                            <form onSubmit={this.handlePhotoSubmit} encType="multipart/form-data" >
                                <input className="form-control mb-2" type="file" accept=".png, .jpg, .jpeg, .gif" name="photo" onChange={this.handlePhoto} required />
                                <button type="submit" className="btn btn-primary w-100">Upload photo</button>
                            </form>
                        </Card>
                    </div>
                    <div className="d-flex h-50 row">
                        <Card className="my-auto mx-auto shadow-lg p-3 mb-5 bg-white rounded">
                            <Card.Body>
                            <form  onSubmit={this.handleFormSubmit} >
                                <div className="form-group row">
                                    <label htmlFor="InputUsername" className="col-sm-4 col-form-label">Username:</label>
                                    <div className="col-sm-8">
                                        <input type="text" className="form-control" id="InputUsername" pattern="^\S{1,30}"
                                        aria-describedby="inputHelp" name="username" placeholder="Enter username" 
                                        value={this.state.username} onChange={this.handleInputChange} disabled />
                                    </div>    
                                </div>
                                <div className="form-group row">
                                    <label htmlFor="InputEmail" className="col-sm-4 col-form-label">Email:</label>
                                    <div className="col-sm-8">
                                        <input type="email" name="email" className="form-control" id="InputEmail" pattern="^\S{1,30}"
                                        value={this.state.email} onChange={this.handleInputChange} placeholder="Enter your email" disabled />
                                    </div>
                                </div>
                                <div className="form-group row">
                                    <label htmlFor="InputPassword" className="col-sm-4 col-form-label">Password:</label>
                                    <div className="col-sm-8">
                                        <input type="password" name="password" className="form-control" id="InputPassword" pattern="^\S{1,30}"
                                        value={this.state.password} onChange={this.handleInputChange} placeholder="Enter a new password" />
                                    </div>
                                </div>
                                <div className="form-group row">
                                    <label htmlFor="InputConfirmPassword" className="col-sm-4 col-form-label">Password:</label>
                                    <div className="col-sm-8">
                                        <input type="password" name="confirmPassword" className="form-control" id="InputConfirmPassword" pattern="^\S{1,30}"
                                        value={this.state.confirmPassword} onChange={this.handleInputChange} placeholder="Confirm new password" />
                                    </div>
                                </div>
                                <div className="form-group row">
                                    <label htmlFor="InputFname" className="col-sm-4 col-form-label">First name:</label>
                                    <div className="col-sm-8">
                                        <input type="text" name="firstname" className="form-control" id="InputFname" 
                                        value={this.state.firstname} onChange={this.handleInputChange} placeholder="Change your first name" required />
                                    </div>
                                </div>
                                <div className="form-group row">
                                    <label htmlFor="InputLname" className="col-sm-4 col-form-label">Last name:</label>
                                    <div className="col-sm-8">
                                        <input type="text" name="lastname" className="form-control" id="InputLname" 
                                        value={this.state.lastname} onChange={this.handleInputChange} placeholder="Change your last name" required />
                                </div>
                                </div>
                                <button type="submit" className="btn btn-primary w-100">Save changes</button>
                            </form>
                            </Card.Body>
                        </Card>
                        </div>
                    </div>
            )}
        return <Redirect to="/" />;
        }
}

export default Profile;