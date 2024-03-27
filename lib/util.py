start_string = """use std::env;
fn main() -> Result<(), std::num::ParseIntError> {
    // Boilerplate
	let args: Vec<String> = env::args().collect();
    if args.len() != 2 {
        println!("Usage: parity <number>");
        std::process::exit(1);
    }
	let number = &args[1];
	let number: u64 = number.trim().parse()?;

    // Coding genius comes here
"""

end_string = """
    Ok(())
}"""

description_text = "Metaprogram to generate a Rust source code file that prints whether a number is even or odd."