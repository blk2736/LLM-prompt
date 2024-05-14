prompt = f"""You are a document reading specialist. I will provide you with a text excerpt below. After reading it, please formulate three questions regarding the document. I will also give you two examples for your reference. 
    ---------------------------
    example 1:
    [ducument]
    Matthieu Chedid was born in Boulogne-Billancourt, Hauts-de-Seine, France, the son of French \
    singer Louis Chedid, and the grandson of the Egyptian-born French writer and poet of Lebanese descent Andrée Chedid who has written lyrics for him. His sister is the music \
    video and concert director Émilie Chedid.
    [question]
    <Who is the father of the performer of Qui de noux deux?>
    <Where was Matthieu Chedid born?>
    <What is Matthieu Chedid's sister's occupation>
    ---------------------------
    example 2:
    [ducument]
    Green Ice is the soundtrack to the 1981 United Kingdom science fiction film "Green Ice" starring \
    Ryan O\'Neal. The soundtrack was recorded by Bill Wyman and contains 18 original songs.
    [question]
    <From which country does the movie Green Ice originate?>
    <Who is the child of the cast member of Green Ice?>
    <How many songs are included in Green Ice?>
    ---------------------------
    Now the ducument is:
    {document}
    Please enter the questions you would like to ask into the < >."""
