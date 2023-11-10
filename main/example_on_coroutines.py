import asyncio
import time

from rich import print


def custom_print(message: str) -> None:
    """Custom function for printing."""
    print(f"[bold green]>>>> {message} <<<<<")


async def get_inputs() -> str:
    """Simulate getting user inputs."""
    await asyncio.sleep(1)
    return "Inputs received!"


async def make_prediction() -> str:
    """Simulate making predictions."""
    await asyncio.sleep(3)
    return "Predictions made!"


async def method_1() -> None:
    """This gathers all the coroutines and runs as a batch. It waits for all
    of the given tasks to complete before returning."""
    start_time = time.perf_counter()
    print("\n\nRunning method_1 ...\n")
    result_get_inputs, result_make_prediction = await asyncio.gather(
        get_inputs(), make_prediction()
    )

    custom_print(result_get_inputs)
    custom_print(result_make_prediction)
    end_time = time.perf_counter()
    print(f"\n[yellow]It took {(end_time - start_time):.3f} seconds to run.")


async def method_2() -> None:
    """This creates an individual task for each coroutine. It schedules the task
    to run and returns immediately."""
    start_time = time.perf_counter()
    print("\n\nRunning method_2 ...\n")
    result_get_inputs = await asyncio.create_task(get_inputs())
    result_make_prediction = await asyncio.create_task(make_prediction())

    custom_print(result_get_inputs)
    custom_print(result_make_prediction)
    end_time = time.perf_counter()
    print(f"\n[yellow]It took {(end_time - start_time):.3f} seconds to run.")


asyncio.run(method_1())  # It took 3.112 seconds to run.
asyncio.run(method_2())  # It took 4.003 seconds to run.
