# SingT

## Description

SingT is a Telegram bot that generates a concise summary of any song, based on
its lyrics. The bot can process audio either from a **YouTube link** or by
accepting an **audio file** directly via Telegram. After extracting the audio,
the bot converts speech to text, detects the language of the lyrics, translates
them into the user's preferred language, and provides a brief summary of the
song’s content.

The goal is to help users quickly understand the theme and meaning of songs,
regardless of language. This makes the bot ideal for music enthusiasts, language
learners, and anyone exploring music from different cultures.

### How It Works

1. **Audio Input**: The user can either:
   - Provide a **YouTube link** to the song, from which the bot extracts the
     audio track.
   - Upload an **audio file** directly through Telegram.

2. **Speech-to-Text**: The bot uses **Whisper**, a speech-to-text model, to
   convert the audio into text.

3. **Language Detection**: The bot detects the language of the song lyrics using
   a language detection library like `langdetect`.

4. **Translation**: The lyrics are then translated into the language selected by
   the user, using an advanced translation model (such as GPT).

5. **Summary Generation**: Finally, the bot generates a concise summary of the
   song’s content using a large language model.

### Key Features

- **Audio Processing**: Handles audio input either via YouTube or direct file
  upload.
- **Speech-to-Text Conversion**: Utilizes OpenAI’s **Whisper** model for
  accurate transcription of lyrics.
- **Language Detection**: Automatically detects the language of the song.
- **Translation**: Supports multiple languages, allowing translations into the
  user's selected language.
- **Summarization**: Provides a brief and insightful summary of the song's
  lyrics, capturing the core themes and emotions.

### Use Cases

- **Music Enthusiasts**: Get a quick understanding of a song’s meaning without
  needing to listen to the entire track.
- **Language Learners**: Learn the meaning of foreign-language songs with
  translated summaries.
- **Cross-Cultural Exploration**: Explore music from various cultures with an
  easy-to-understand summary in your native language.

## Team

| Name                   | Innomail                          | Role                        |
|------------------------| --------------------------------- | --------------------------- |
| Apollinaria Chernikova | a.chernikova@innopolis.university | Data Scientist, ML Engineer |
| Egor Machnev           | e.machnev@innopolis.university    | Data Engineer, MLOps        |

## Technology Stack

- **YouTube API**: For extracting audio from YouTube videos.
- **Whisper (OpenAI)**: For speech-to-text conversion of audio files.
- **langdetect**: For detecting the language of the lyrics.
- **GPT-based models**: For translation and summarization tasks.
- **Aiogram**: For Telegram bot integration and handling user interactions.

## Current Progress

We are currently in the development stage, where:

- The **functional schema** of the bot has been designed.
- Initial testing of **Whisper**, **langdetect**, and translation models has
  been conducted.
- Basic **Telegram bot integration** using **Aiogram** has been established.
