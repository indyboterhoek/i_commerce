import FeaturedItems from '../components/FeaturedItems';
import SliderItems from '../components/SliderItems';

export default function HomePage() {
	return (
		<div className='w-full h-auto'>
			<div className="flex justify-center p-20 h-full">
				<div className="featured w-min h-min">
					<FeaturedItems />
				</div>
			</div>
			<div className="flex justify-center p-10">
				<SliderItems />
			</div>
		</div>
	)
}