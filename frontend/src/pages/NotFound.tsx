import { Link, Button } from "@nextui-org/react";

export default function NotFound() {
	return (
		<div className="flex justify-center h-screen overflow-hidden">
			<div className="flex flex-col justify-center gap-10 text-center w-max">
				<h1 className="text-9xl font-bold">404</h1>
				<h2 className="text-5xl">Page Not Found</h2>
				<Button
					href={"/"}
					as={Link}
					color="primary"
					showAnchorIcon
					variant="solid"
				>
					Return to Home
				</Button>
			</div>
		</div>
	);
}