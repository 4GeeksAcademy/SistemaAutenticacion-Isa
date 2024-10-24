const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			user:{id:"",
				email:""
			}
		},
		actions: {
			// Use getActions to call a function within a fuction
			register: async (email,password)=>{
				try {
					const response = await fetch(`${process.env.BACKEND_URL}/api/register`,{
						method: "POST",
						headers: {
							"Content-Type": "application/json"
						},
						body: JSON.stringify({email:email, password:password})
					})
					const data= await response.json();
				} catch (error) {
					console.log("Error al registrar un usuario", error)
				}
			},
			login: async (email, password) => {
				try{
					const response = await fetch(`${process.env.BACKEND_URL}api/login`, {
						method: "POST",
						headers: {
							"Content-Type": "application/json"
						},
						body: JSON.stringify({ email: email, password: password })
					});
					if(response.ok){
						const data = await response.json();
						sessionStorage.setItem("token", data.access_token);
						setStore({ user: 
						{
							id: data.id,
							email: data.email
						} });
						console.log("Usuario logueado correctamente",data);
						return true;	
					}else{
						console.log("Error al loguear el usuario", errorData.message);
						return false;
					}
				}catch(error){
					console.log("Error al loguear el usuario",error);
					return false;
				}
			
			}
		}
	};
};

export default getState;
