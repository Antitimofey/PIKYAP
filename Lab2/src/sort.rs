use std::io;

fn main() {
    println!("Please enter array size:");
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let size: usize = input.trim().parse().expect("Please enter a valid integer");
    
    let mut numbers = Vec::new();

    // Input 10 integers from the user
    println!("Please enter 10 integers:");

    for _ in 0..size { 
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Failed to read line");
        let num: i32 = input.trim().parse().expect("Please enter a valid integer");
        numbers.push(num);
    }

    for i in 0..size {
        let mut min_index = i;
        for j in (i + 1)..size {
            if numbers[j] < numbers[min_index] {
                min_index = j;
            }
        }
        numbers.swap(i, min_index);
    }

    println!("Sorted array: {:?}", numbers);
}
