import asyncio

# An asynchronous function that simulates a delay
async def fetch_data(data_id):
    print(f"Fetching data for ID: {data_id}...")
    await asyncio.sleep(2)  # Simulate a network or I/O delay
    print(f"Data fetched for ID: {data_id}")
    return f"Data-{data_id}"

# Another asynchronous function to process the data
async def process_data(data):
    print(f"Processing {data}...")
    await asyncio.sleep(1)  # Simulate processing delay
    print(f"Processing complete for {data}")
    return f"Processed-{data}"

# A main function to coordinate the tasks
async def main():
    print("Starting async tasks...")
    # Fetch data and process it concurrently
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    task3 = asyncio.create_task(fetch_data(3))

    # Wait for all fetch tasks to complete
    fetched_data = await asyncio.gather(task1, task2, task3)

    # Process the fetched data one by one
    for data in fetched_data:
        await process_data(data)

    print("All tasks complete!")

# Run the asynchronous main function
asyncio.run(main())
