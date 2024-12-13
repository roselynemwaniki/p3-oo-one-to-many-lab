class Pet:  
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]  
    all = []  # Renamed to 'all' for consistency with test  

    def __init__(self, name, pet_type, owner=None):  
        if pet_type not in self.PET_TYPES:  
            raise Exception(f"Invalid pet type: {pet_type}. Please choose from {self.PET_TYPES}.")  

        self.name = name  
        self.pet_type = pet_type  
        self.owner = owner  
        
        # Add this pet to the class-level list of all pets  
        Pet.all.append(self)  # Ensure it uses 'Pet.all'  

        if owner:  
            owner.add_pet(self)  # Register pet with the owner  

class Owner:  
    def __init__(self, name):  
        self.name = name  
        self._pets = []  # Instance variable to store pets belonging to the owner  

    def pets(self):  
        """Returns a list of the owner's pets."""  
        return self._pets  

    def add_pet(self, pet):  
        """Adds a pet to the owner after validation."""  
        if isinstance(pet, Pet):  
            pet.owner = self  # Set the owner of the pet to the current instance  
            self._pets.append(pet)  # Append the pet to the owner's list of pets  
        else:  
            raise Exception("The provided pet must be an instance of the Pet class.")  
    
    def get_sorted_pets(self):  
        """Returns a sorted list of the owner's pets by their names."""  
        return sorted(self._pets, key=lambda pet: pet.name)  # Removed the extra parentheses
    
try: 
    
    owner1 = Owner("Alice")  
    pet1 = Pet("Buddy", "dog", owner1)  # Valid instance with owner  
    owner1.add_pet(pet1)  
    
    pet2 = Pet("Mittens", "cat")  
    owner1.add_pet(pet2)  # Add pet without owner initially  
    print(f"{owner1.name}'s pets: {[pet.name for pet in owner1.pets()]}")  
    
    sorted_pets = owner1.get_sorted_pets()  
    print("Sorted pets by name:", [pet.name for pet in sorted_pets])  
    
    pet3 = Pet("Ziggy", "exotic")  
    owner1.add_pet(pet3)  
    
    print(f"Updated pets: {[pet.name for pet in owner1.pets()]}")  
    
    # Sorting again  
    sorted_pets = owner1.get_sorted_pets()  
    print("Sorted pets by name after adding Ziggy:", [pet.name for pet in sorted_pets])  
    
    # This will raise an exception as it's an invalid pet type.  
    pet_invalid = Pet("Goldie", "fish")  # Invalid pet type  
except Exception as e:  
    print(e)  