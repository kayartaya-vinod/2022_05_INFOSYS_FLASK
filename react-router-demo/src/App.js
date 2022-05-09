import Header from './components/Header';
import Home from './components/Home';
import AddCustomer from './components/AddCustomer';
import ViewAllCustomers from './components/ViewAllCustomers';

import { BrowserRouter as Router, Link, Route, Routes } from 'react-router-dom';
function App() {
    return (
        <Router>
            <Header />
            <div className='container'>
                <div className='row'>
                    <div className='col-md-4 list-group'>
                        <Link className='list-group-item' to='/'>
                            Home
                        </Link>
                        <Link className='list-group-item' to='/add-customer'>
                            Add customer
                        </Link>
                        <Link
                            className='list-group-item'
                            to='/view-all-customers'
                        >
                            View all customers
                        </Link>
                    </div>
                    <div
                        className='col-md-8 alert alert-secondary'
                        style={{ minHeight: '600px' }}
                    >
                        <Routes>
                            <Route path='/' exact={true} element={<Home />} />
                            <Route
                                path='/add-customer'
                                element={<AddCustomer />}
                            />
                            <Route
                                path='/view-all-customers'
                                element={<ViewAllCustomers />}
                            />
                            <Route path='*' element={<h1>Page not found</h1>} />
                        </Routes>
                    </div>
                </div>
            </div>
        </Router>
    );
}

export default App;
