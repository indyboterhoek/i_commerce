import { Card, CardBody, CardFooter, Image } from "@nextui-org/react";

export default function FeaturedItems() {
	const list = [
		{
			title: "Orange",
			img: "/images/fruit-1.jpeg",
			price: "$5.50",
		},
		{
			title: "Tangerine",
			img: "/images/fruit-2.jpeg",
			price: "$3.00",
		},
		{
			title: "Raspberry",
			img: "/images/fruit-3.jpeg",
			price: "$10.00",
		},
	];

	return (
		<div className="gap-2 grid grid-cols-2 sm:grid-cols-4 justify-center">
			{list.map((item, index) => (
				<Card shadow="sm" key={index} isPressable onPress={() => console.log("item pressed")}>
					<CardBody className="overflow-visible p-0">
						<Image
							shadow="sm"
							radius="lg"
							width="100%"
							alt={item.title}
							className="w-full object-cover h-[140px]"
							src={item.img}
						/>
					</CardBody>
					<CardFooter className="text-small justify-between">
						<b>{item.title}</b>
						<p className="text-default-500">{item.price}</p>
					</CardFooter>
				</Card>
			))}
		</div>
	)
}