# # formal grammar

# # - ply (lex/yacc)
# # + parsimonious
# # + parsley

# # parser combinators

# # - funcparserlib
# # - codetalker

# # markdownblog.py
# # Post ::= Title Slug Posted Tags Body
# # Title ::= "Title: " Anychar+ "\n"
# # Slug ::= "Slug: " URLchar+ "\n"


# grammar = makeGrammar("""
#     post = title:title slug:slug posted:posted tags:tags body:body ->Post(title, slug, tags, body)
#     title = 'Title: ' <anychar+>:title '\\n' -> title
#     slug = 'Slug: ' <urlchar+>:slug '\\n' -> slug
#     posted = 'Posted: ' iso8601date:date '\\n' -> date
#     body = 'Body: ' <anychar+
    
# """)

