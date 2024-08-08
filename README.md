# Three-Tier Web Application Deployment with Ansible

## Overview

This repository provides Ansible roles and playbooks to deploy a three-tier web application consisting of a frontend (Nginx web server), a backend (Node.js application), and a database (MySQL server). The deployment is automated using Ansible, ensuring that all components are correctly configured and can communicate with each other.

## Project Directory Structure

The directory structure of the project is organized as follows:


## Role Definitions and Dependencies

### Frontend Role

- **Tasks**: Install and configure Nginx.
- **Templates**: `nginx.conf.j2`
- **Dependencies**: None

**[See `frontend/meta/main.yml` in the repository for role dependencies.]**

### Backend Role

- **Tasks**: Install Node.js, configure the application, and start the service.
- **Templates**: `app.js.j2`, `package.json.j2`
- **Dependencies**: None

**[See `backend/meta/main.yml` in the repository for role dependencies.]**

### Database Role

- **Tasks**: Install MySQL server and configure the database.
- **Dependencies**: None

**[See `database/meta/main.yml` in the repository for role dependencies.]**

## Inventory File

The inventory file is used to define groups and hosts for frontend, backend, and database tiers.

- **Static Inventory**: `inventory/hosts.ini`
- **Dynamic Inventory**: `inventory/ec2_inventory.py`

**[Update the inventory files with appropriate host information and configurations.]**

## Playbooks

### Deploy Playbook

**File**: `playbooks/deploy.yml`

This playbook orchestrates the deployment of the three-tier application by calling the roles for frontend, backend, and database.

**[See `deploy.yml` in the repository for detailed playbook configuration.]**

### Test Playbook

**File**: `playbooks/test.yml`

This playbook verifies the deployment and functionality of each tier.

**[See `test.yml` in the repository for detailed playbook configuration.]**

## Instructions for Use

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Update Inventory**:
    - Configure `inventory/hosts.ini` or `inventory/ec2_inventory.py` with your hosts and parameters.

3. **Configure `ansible.cfg`**:
    - Ensure the inventory path is set correctly in `ansible.cfg`.

4. **Run Deployment**:
    ```bash
    ansible-playbook -i inventory/hosts.ini playbooks/deploy.yml
    ```

5. **Run Testing**:
    ```bash
    ansible-playbook -i inventory/hosts.ini playbooks/test.yml
    ```

## Output:
- ![image](https://github.com/user-attachments/assets/114c7626-9bfd-44a9-a8f2-910ab9cbe16e)
- ![image](https://github.com/user-attachments/assets/c3344d6c-e8d1-4d3b-9e9d-e453461c9325)
- ![image](https://github.com/user-attachments/assets/6f2f72d2-ca82-4a85-9b70-d12b4d073ae3)
- ![image](https://github.com/user-attachments/assets/40887b1d-cba6-4a03-899b-99668b6b7e76)
- ![image](https://github.com/user-attachments/assets/6f59ce51-df8d-4a7b-bfca-c46d20bb9a79)
- ![image](https://github.com/user-attachments/assets/54c468e1-86d3-4d4f-bfc5-8f95de69a90f)






## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

