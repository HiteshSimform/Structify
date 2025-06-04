-- ================================
-- 1. custom_user
-- ================================
CREATE TABLE custom_user (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    is_staff BOOLEAN DEFAULT FALSE,
    is_superuser BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO custom_user (email, first_name, last_name, password, is_staff, is_superuser)
VALUES 
('admin@example.com', 'Admin', 'User', 'hashedpassword123', TRUE, TRUE),
('hr@example.com', 'HR', 'Manager', 'hashedpassword123', TRUE, FALSE),
('manager@example.com', 'Manager', 'One', 'hashedpassword123', TRUE, FALSE),
('employee1@example.com', 'John', 'Doe', 'hashedpassword123', FALSE, FALSE),
('employee2@example.com', 'Jane', 'Smith', 'hashedpassword123', FALSE, FALSE);

-- ================================
-- 2. department
-- ================================
CREATE TABLE department (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_by INTEGER REFERENCES custom_user(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_by INTEGER REFERENCES custom_user(id),
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_deleted BOOLEAN DEFAULT FALSE,
    deleted_at TIMESTAMP
);

INSERT INTO department (name, description, created_by)
VALUES 
('IT', 'Handles software and hardware', 1),
('HR', 'Manages people and policy', 2),
('Finance', 'Handles accounts', 2);

-- ================================
-- 3. designation
-- ================================
CREATE TABLE designation (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_by INTEGER REFERENCES custom_user(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_by INTEGER REFERENCES custom_user(id),
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_deleted BOOLEAN DEFAULT FALSE,
    deleted_at TIMESTAMP
);

INSERT INTO designation (name, description, created_by)
VALUES 
('Software Engineer', 'Codes applications', 1),
('HR Executive', 'Manages HR tasks', 2),
('Accountant', 'Manages finances', 2),
('Manager', 'Manages teams', 3);

-- ================================
-- 4. employee
-- ================================
CREATE TABLE employee (
    id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE REFERENCES custom_user(id),
    department_id INTEGER REFERENCES department(id),
    designation_id INTEGER REFERENCES designation(id),
    phone_number VARCHAR(20),
    hire_date DATE,
    created_by INTEGER REFERENCES custom_user(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_by INTEGER REFERENCES custom_user(id),
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_deleted BOOLEAN DEFAULT FALSE,
    deleted_at TIMESTAMP
);

INSERT INTO employee (user_id, department_id, designation_id, phone_number, hire_date, created_by)
VALUES 
(3, 1, 4, '9876543210', '2024-01-10', 1), -- Manager user
(2, 2, 2, '9876543211', '2023-12-15', 1), -- HR user
(4, 1, 1, '9876543212', '2024-01-15', 2), -- Employee John Doe
(5, 3, 3, '9876543213', '2024-02-10', 2); -- Employee Jane Smith

-- ================================
-- 5. leave_types
-- ================================
CREATE TABLE leave_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    max_days INTEGER,
    created_by INTEGER REFERENCES custom_user(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_by INTEGER REFERENCES custom_user(id),
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_deleted BOOLEAN DEFAULT FALSE,
    deleted_at TIMESTAMP
);

INSERT INTO leave_types (name, description, max_days, created_by)
VALUES 
('Sick Leave', 'For medical reasons', 10, 2),
('Casual Leave', 'Personal time off', 7, 2),
('Earned Leave', 'Accrued leave', 15, 2);

-- ================================
-- 6. leave_applications
-- ================================
CREATE TABLE leave_applications (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER REFERENCES employee(id),
    leave_type_id INTEGER REFERENCES leave_types(id),
    start_date DATE,
    end_date DATE,
    reason TEXT,
    status VARCHAR(50),
    approver_id INTEGER REFERENCES custom_user(id),
    created_by INTEGER REFERENCES custom_user(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_by INTEGER REFERENCES custom_user(id),
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_deleted BOOLEAN DEFAULT FALSE,
    deleted_at TIMESTAMP
);

INSERT INTO leave_applications (employee_id, leave_type_id, start_date, end_date, reason, status, approver_id, created_by)
VALUES 
(3, 1, '2024-05-01', '2024-05-03', 'Fever and cold', 'Approved', 2, 3),
(4, 2, '2024-06-10', '2024-06-12', 'Family function', 'Pending', 2, 4);

-- ================================
-- 7. leave_balances
-- ================================
CREATE TABLE leave_balances (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER REFERENCES employee(id),
    leave_type_id INTEGER REFERENCES leave_types(id),
    balance_days DECIMAL(5,2),
    year INTEGER,
    created_by INTEGER REFERENCES custom_user(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_by INTEGER REFERENCES custom_user(id),
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_deleted BOOLEAN DEFAULT FALSE,
    deleted_at TIMESTAMP
);

INSERT INTO leave_balances (employee_id, leave_type_id, balance_days, year, created_by)
VALUES 
(3, 1, 8.0, 2024, 2),
(4, 2, 6.5, 2024, 2);

-- ================================
-- 8. salaries
-- ================================
CREATE TABLE salaries (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER REFERENCES employee(id),
    basic_salary DECIMAL(10, 2) NOT NULL,
    allowances DECIMAL(10, 2) DEFAULT 0.00,
    deductions DECIMAL(10, 2) DEFAULT 0.00,
    net_salary DECIMAL(10, 2) GENERATED ALWAYS AS (basic_salary + allowances - deductions) STORED,
    pay_period_start DATE NOT NULL,
    pay_period_end DATE NOT NULL,
    payment_date DATE NOT NULL,
    created_by INTEGER REFERENCES custom_user(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_by INTEGER REFERENCES custom_user(id),
    modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_deleted BOOLEAN DEFAULT FALSE,
    deleted_at TIMESTAMP
);

INSERT INTO salaries (
    employee_id, basic_salary, allowances, deductions,
    pay_period_start, pay_period_end, payment_date,
    created_by, modified_by
)
VALUES 
(3, 80000.00, 5000.00, 2000.00, '2024-05-01', '2024-05-31', '2024-06-01', 2, 2),
(4, 45000.00, 4000.00, 1500.00, '2024-05-01', '2024-05-31', '2024-06-01', 2, 2);

