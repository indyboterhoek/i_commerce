import { Card, CardBody, CardFooter } from "@nextui-org/react";
import { useState, useEffect } from "react";
import axios from "axios";

type FeaturedItem = {
	name: string,
	image: string,
	price: number,
	sale?: number,
}

export default function FeaturedItems() {
	const [featuredList, setFeaturedList] = useState<FeaturedItem[]>([]);
	const [selected, setSelected] = useState(0);
	const [isLoaded, setIsLoaded] = useState(false);

	useEffect(() => {
		async function fetchData() {
			try {
				const response = await axios.get(`${import.meta.env.VITE_API_URL}/api/products/product/home`)
				console.log(response.data)
				const data = response.data.slice(0, 3)
				setFeaturedList(data)
				setIsLoaded(true)
			}
			catch (error) {
				console.error(error)
			}
		}
		fetchData()
	}, [])

	return (
		<div className="flex gap-2 h-full">
			{!isLoaded ? <Card shadow="sm" className={"row-span-2"} key={0} isPressable onMouseEnter={() => {
				setSelected(0);
			}} onPress={() => console.log("item pressed")}>
				<CardBody className={`featured-card p-1 h-[510px] w-[510px]`} style={{
					"backgroundImage": ``,
					"backgroundSize": "cover",
				}}>
				</CardBody>
				<CardFooter className="text-small justify-between">
					<b>Loading...</b>
					<p className={`text-default-500`}>$0</p>
				</CardFooter>
			</Card> : null}
			{featuredList.map((item, index) => (
				<Card shadow="sm" className={index == selected ? "row-span-2" : ""} key={index} isPressable onMouseEnter={() => {
					setSelected(index);
				}} onPress={() => console.log("item pressed")}>
					<CardBody className={`featured-card p-1 bg-white h-[510px] ${index == selected ? "w-[510px]" : "w-[200px]"}`} style={{
						"backgroundImage": `url(${import.meta.env.VITE_API_URL}${item.image})`,
						"backgroundSize": "cover",
					}}>
					</CardBody>
					<CardFooter className="text-small justify-between">
						<b>{item.name}</b>
						<p className={`text-default-500 ${item.sale ? "line-through" : ""}`}>${item.price}</p>
						{item.sale ? <p className="text-default-500">${item.sale}</p> : null}
					</CardFooter>
				</Card>
			))}
		</div>
	)
}