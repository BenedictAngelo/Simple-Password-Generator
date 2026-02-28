use std::io;

pub fn password() {
    let answer: &mut String = &mut String::from("");
    println!("Type your answer: ");
    io::stdin().read_line(answer).unwrap();
    println!("What is you answer?: {}", answer);
    println!("{}", answer);
}

