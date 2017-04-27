!_TAG_FILE_FORMAT	2	/extended format; --format=1 will not append ;" to lines/
!_TAG_FILE_SORTED	1	/0=unsorted, 1=sorted, 2=foldcase/
!_TAG_PROGRAM_AUTHOR	Darren Hiebert	/dhiebert@users.sourceforge.net/
!_TAG_PROGRAM_NAME	Exuberant Ctags	//
!_TAG_PROGRAM_URL	http://ctags.sourceforge.net	/official site/
!_TAG_PROGRAM_VERSION	5.9~svn20110310	//
LANGUAGE_CHOICES	/home/hu/tutorial/snippets/models.py	/^LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])$/;"	v
LEXERS	/home/hu/tutorial/snippets/models.py	/^LEXERS = [item for item in get_all_lexers() if item[1]]$/;"	v
Meta	/home/hu/tutorial/snippets/models.py	/^    class Meta:$/;"	c	class:Snippet
STYLE_CHOICES	/home/hu/tutorial/snippets/models.py	/^STYLE_CHOICES = sorted((item, item) for item in get_all_styles())$/;"	v
Snippet	/home/hu/tutorial/snippets/models.py	/^class Snippet(models.Model):$/;"	c
code	/home/hu/tutorial/snippets/models.py	/^    code = models.TextField()$/;"	v	class:Snippet
created	/home/hu/tutorial/snippets/models.py	/^    created = models.DateTimeField(auto_now_add=True)$/;"	v	class:Snippet
language	/home/hu/tutorial/snippets/models.py	/^    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)$/;"	v	class:Snippet
linenos	/home/hu/tutorial/snippets/models.py	/^    linenos = models.BooleanField(default=False)$/;"	v	class:Snippet
ordering	/home/hu/tutorial/snippets/models.py	/^        ordering = ('created',)$/;"	v	class:Snippet.Meta
style	/home/hu/tutorial/snippets/models.py	/^    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)$/;"	v	class:Snippet
title	/home/hu/tutorial/snippets/models.py	/^    title = models.CharField(max_length=100, blank=True, default='')$/;"	v	class:Snippet
