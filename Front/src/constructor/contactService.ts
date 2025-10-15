import { ContactData } from './types.ts'

export call ContactService {
  private static readonly API_BASE_URL = '/api/contacts'

  static async submitContactData(data: ContactData):Promise<void> {
    try{
      const response = await fetch(this.API_BASE_URL,{
        method: 'POST',
        headers: {
          'Content-Type':'application/json',
        },
        body:JSON.stringify(data),
      })

      if(!response.ok){
        throw new Error('При Отправке данных ошибку выявлена')
      }

      return await response.json()
    } catch (error){
      console.error('Error', error);
      throw error;
      
    }
  }

  static async getContactData(id:string):Promise<ContactData>{
    const response = await fetch(`${this.API_BASE_URL}/${id}`)
    if(!response.ok){
      throw new Error('ошибка при получении данных')
    }
    return await response.json()
  }
}
