import { useEffect, useState } from 'react'
import './App.css'
import axios from 'axios'
import NavbarMenu from './components/NavbarMenu'
import { Spinner } from "@nextui-org/react";
import FeaturedItems from './components/FeaturedItems';

function App() {
	const [data, setData] = useState<any>([])

	useEffect(() => {
		async function fetchData() {
			try {
				const response = await axios.get(`${import.meta.env.VITE_API_URL}/api/products/product/home`)
				console.log(response.data)
			}
			catch (error) {
				console.error(error)
			}
		}
		fetchData()
	}, [])

	return (
		<div className='app dark text-foreground bg-background'>
			<NavbarMenu />
			<FeaturedItems />
		</div>
	)
}

export default App
