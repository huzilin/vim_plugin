!_TAG_FILE_FORMAT	2	/extended format; --format=1 will not append ;" to lines/
!_TAG_FILE_SORTED	1	/0=unsorted, 1=sorted, 2=foldcase/
!_TAG_PROGRAM_AUTHOR	Darren Hiebert	/dhiebert@users.sourceforge.net/
!_TAG_PROGRAM_NAME	Exuberant Ctags	//
!_TAG_PROGRAM_URL	http://ctags.sourceforge.net	/official site/
!_TAG_PROGRAM_VERSION	5.9~svn20110310	//
SnippetSerializer	/home/hu/tutorial/snippets/serializers.py	/^class SnippetSerializer(serializers.Serializer):$/;"	c
code	/home/hu/tutorial/snippets/serializers.py	/^    code = serializers.CharField(style={'base_template': 'textarea.html'})$/;"	v	class:SnippetSerializer
create	/home/hu/tutorial/snippets/serializers.py	/^    def create(self, validated_data):$/;"	m	class:SnippetSerializer
id	/home/hu/tutorial/snippets/serializers.py	/^    id = serializers.IntegerField(read_only=True)$/;"	v	class:SnippetSerializer
language	/home/hu/tutorial/snippets/serializers.py	/^    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')$/;"	v	class:SnippetSerializer
linenos	/home/hu/tutorial/snippets/serializers.py	/^    linenos = serializers.BooleanField(required=False)$/;"	v	class:SnippetSerializer
style	/home/hu/tutorial/snippets/serializers.py	/^    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')$/;"	v	class:SnippetSerializer
title	/home/hu/tutorial/snippets/serializers.py	/^    title = serializers.CharField(required=False, allow_blank=True, max_length=100)$/;"	v	class:SnippetSerializer
update	/home/hu/tutorial/snippets/serializers.py	/^    def update(self, instance, validated_data):$/;"	m	class:SnippetSerializer
