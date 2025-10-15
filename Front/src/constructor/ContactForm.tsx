import { useState } from "react"
import { ContactData } from "./types"

const ContactForm : React.FC = () => {
  const [formData, setFormData] = useState<ContactData>({
    roomNumber: '',
    group: '',
    numberGroup: ''
  })


  const hanleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const {name, value} = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }))
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    console.log('отправленные данные:', formData)
  }

  return(
<form onSubmit={handleSubmit} className="contact-form">
      <div className="form-group">
          <label htmlFor="roomNumber">Номер комнаты</label>
          <input
            type="text"
            id="roomNumber"
            name="roomNumber"
            value={formData.roomNumber}
            onChange={handleInputChange}
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="group">Группа</label>
          <input
            type="text"
            id="group"
          name="group"
          value={formData.group}
          onChange={handleInputChange}
        />
      </div>

      <div className="form-group">
        <label htmlFor="numberGroup">Номер группы</label>
        <input
          type="number"
          id="numberGroup"
          name="numberGroup"
          value={formData.numberGroup}
          onChange={handleInputChange}
        />
      </div>

      <button type="submit">Отправить</button>
      </form>
  )
};

export default ContactForm;

