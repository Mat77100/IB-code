#15/01/2026


class ParentCompany:
    def __init__ (self, CompanyName, CompanySize, CompanyID):
        self.CompanyName = CompanyName
        self.CompanySize = CompanySize
        self.CompanyID = CompanyID
    def GetCompName(self):
        print(f"Parent company name: \033[0;36m{self.CompanyName}\033[0m")
    def GetCompSize(self):
        print(f"Size of parent company: \033[0;36m{self.CompanySize}\033[0m")
    def GetCompID(self):
        print(f"Parent company ID: \033[0;36m{self.CompanyID}\033[0m")

class Contracts(ParentCompany):
    def __init__(self, CompanyName, CompanySize, CompanyID, is_active, contractID, contractName, pay, client):
        super().__init__(CompanyName, CompanySize, CompanyID)
        self.is_active = is_active
        self.contractID = contractID
        self.contractName = contractName
        self.pay = pay
        self.client = client
    def ContractStatus(self):
        print(f"Current contract active: \033[0;36m{self.is_active}\033[0m")
    def SwitchStatus(self):
        if self.is_active == True:
            self.is_active = False
            print("Contract is now inactive")
        else:
            self.is_active = True
            print("Contract is now active")
    def GetContractID(self):
        print(f"Contract ID: \033[0;36m{self.contractID}\033[0m")
    def GetContractName(self):
        print(f"Contract name: \033[0;36m{self.contractName}\033[0m")
    def GetContractPay(self):
        print(f"Contract pay: \033[0;36m{self.pay}\033[0m")
    def GetContractClient(self):
        print(f"Contract client: \033[0;36m{self.client}\033[0m")

class Vehicles(ParentCompany):
    def __init__(self, CompanyName, CompanySize, CompanyID, FuelConsumption, Registration, LicensePlate):
        super().__init__(CompanyName, CompanySize, CompanyID)
        self.FuelConsumption = FuelConsumption
        self.Registration = Registration
        self.LicensePlate = LicensePlate
    def GetLicensePlate(self):
        print(f"Vehicle license plate: {self.LicensePlate}")
    def GetRegistration(self):
        print(f"Vehicle registration: {self.Registration}")
    def GetFuelConsumption(self):
        print(f"Vehicle fuel consumption: {self.FuelConsumption}")
