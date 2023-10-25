import './App.css'
import NavbarMenu from './components/NavbarMenu'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import HomePage from './pages/HomePage'
import NotFound from './pages/NotFound'

function App() {
	return (
		<div className='app dark text-foreground bg-background h-full'>
			<NavbarMenu />
			<BrowserRouter>
				<Routes>
					<Route path="*" element={<NotFound />} />
					<Route path="/" element={<HomePage />} />
				</Routes>
			</BrowserRouter>
		</div>
	)
}

export default App
