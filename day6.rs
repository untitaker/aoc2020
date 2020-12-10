use std::collections::BTreeSet;
use std::fs;
use std::io::{self, BufRead, BufReader};

fn main() -> io::Result<()> {
    println!(
        "part 1: {}",
        run(BTreeSet::new(), |a, b| a.union(b).cloned().collect())?
    );
    println!(
        "part 1: {}",
        run(('a'..='z').into_iter().collect(), |a, b| a
            .intersection(b)
            .cloned()
            .collect())?
    );
    Ok(())
}

fn run(
    set_init: BTreeSet<char>,
    func: impl Fn(&BTreeSet<char>, &BTreeSet<char>) -> BTreeSet<char>,
) -> io::Result<u64> {
    let f = BufReader::new(fs::File::open("day6.input.txt")?);
    let mut answers = set_init.clone();
    let mut answers_count = 0u64;

    for line in f.lines().into_iter().chain(Some(Ok("".to_owned()))) {
        let line = line?;
        let line = line.trim();

        if line.is_empty() {
            answers_count += answers.len() as u64;
            answers = set_init.clone();
        } else {
            answers = func(&answers, &line.chars().collect());
        }
    }

    Ok(answers_count)
}
