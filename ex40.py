class Song(object):					# class Song has a _init_ that takes this and lyrics params

	def __init__(this, lyrics):
		this.lyrics = lyrics		# this is a var for instance being accessed
									# this.lyrics defines form for printing

	def sing_me_a_song(this):		# this is a function. Method in Java. 
		for line in this.lyrics:	# for all X in this.lyrics
			print line				# prints each line of happy_bday

happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])

									# happy_bday is set as an instance of Song
print
bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


"""
Tesing vim to see how it compares to other text editors...
	Supports syntax highlighting and indentation!

In Java:

<Songs.java>

public class Songs{

	public static void main(String[] args){

		Lyrics happy_bday = new Lyrics ("Happy birthday to you\nI don't want to get sued\nSo I'll stop right there");
		Lyrics bulls_on_parade = new Lyrics ("They rally around the family\nWith pockets full of shells");
		

		System.out.println(happy_bday.sing_me_a_song());

		System.out.println(bulls_on_parade.sing_me_a_song());

	}

}

<Lyrics.java>

public class Lyrics {

	private String lyrics;

	public Lyrics (String lyrics){

		this.lyrics = lyrics;
	}

	public String sing_me_a_song(){
		return lyrics;
	}

}

"""
