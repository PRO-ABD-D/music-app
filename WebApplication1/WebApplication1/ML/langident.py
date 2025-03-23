from lingua import LanguageDetectorBuilder
#pip install lingua-language-detector

detector = (
    LanguageDetectorBuilder
    .from_all_languages()
    .with_preloaded_language_models()
    .build()
)

text = """Tengo miedo de estar sola
I need to get my act together, I know
I say I'm better on my own but
He's telling me I need to grow up, let go
I tell him that I've got an old soul
He said I'm there before my time
I'm asking what all of the rush is for
But I don't want to wait in line
Good things take time
I'm running out of reasons to start up a conversation with you
Usually, I'd be the first to run to your defence
But this time I can't even come up with an excuse
Tengo que vivir un día a la vez, Poco a poco
Otherwise, I lose my head and I start doubting everything that I believe in
Believe me
Tengo miedo de estar sola
I need to get my act together, I know
I say I'm better on my own but
He's telling me I need to grow up, let go
I tell him that I've got an old soul
He said I'm there before my time
I'm asking what all of the rush is for
But I don't want to wait in line
Good things take time
You push me to a side why do I wait?
For you to come around and talk again
Mess with my mind, I'll move myself out of your way
I only say I don't do feelings 'cause you're not
Ready to hear them and I'm not ready to feel them just yet
I'd just rather not confront them because then they
Bring us problems and they're always in the back of my head
Are you bored yet? Are you leaving?
Its kind of shifted, I feel the difference
Don't want attachment to you
I only say I don't do feelings 'cause you're not ready to hear them
And I'm not ready to feel them just yet, just yet"""
if text is not None:
    result = detector.detect_language_of(text)
    print(f"Detected language: {result.name}")
else:
    print("No transcription available to detect the language.")


