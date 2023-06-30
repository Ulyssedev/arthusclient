// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use std::fs::File;
use std::io::BufReader;
use rodio::{Decoder, OutputStream, Sink};


// Learn more about Tauri commands at https://tauri.app/v1/guides/features/command

#[tauri::command]
fn music() {
    // Get a output stream handle to the default physical sound device
    let (_stream, stream_handle) = OutputStream::try_default().unwrap();
    let sink = Sink::try_new(&stream_handle).unwrap();
    // Load a sound from a file, using a path relative to Cargo.toml
    let file = BufReader::new(File::open("./music/trucdeouf.mp3").unwrap());
    // Decode that sound file into a source
    let source = Decoder::new(file).unwrap();
    // Play the sound directly on the device
    sink.append(source);
    sink.sleep_until_end();
    
}

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![music])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
