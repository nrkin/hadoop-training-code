The question is regarding improvement of the search functionality:

1. We have an index of words by which we can directly get the post_id which contains that word.
The index lookup can be made cleaner by leaving common words like a, the, an etc.
Also, words filtered from the tags like "a", "p" can be excluded from the index.
The input will have to be filtered accordingly to make the search more relevant.

2. We can keep an index of tags and the post-id so that tag-search is faster

3. An index of author_id against post_id can give us the activity of a particular use. Search by user-i/username could be efficient using this.
