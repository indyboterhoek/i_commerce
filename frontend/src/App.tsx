import { useEffect, useState } from 'react'
import './App.css'

function App() {
	const [data, setData] = useState<any>([])

	useEffect(() => {
		async function fetchData() {
			console.log(import.meta.env.VITE_API_URL)
			try {
				const response = await fetch(import.meta.env.VITE_API_URL)
				const json = await response.json()
				setData(json)
			}
			catch (error) {
				console.error(error)
			}
		}
		fetchData()
	}, [])

	return (
		<>
			Hello world
		</>
	)
}

export default App
