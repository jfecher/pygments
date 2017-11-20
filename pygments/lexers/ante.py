from pygments.lexer import RegexLexer, include
from pygments.token import Text, Keyword, Comment, Name
from pygments.token import Literal, Operator, Punctuation


__all__ = ["AnteLexer"]


class AnteLexer(RegexLexer):
    name = 'Ante'
    aliases = ['ante']
    filenames = ['*.an']
    mimetypes = ['text/x-ante']

    tokens = {
        'root': [
            (r'\b(if|elif|else|import|mut|with|global|for|in|do|while|'
             r'let|export|continue|break|return|this|is|ext|new|match|'
             r'trait|module|ante|type|where|when|fun|var|and|or|not|then|'
             r'do|pub|pro|pri|const|raw|noinit)\b', Keyword),
            (r'\b(true|false)\b', Literal.Boolean),
            (r'\b(i8|i16|i32|i64|u8|u16|u32|u64|f16|f32|f64|isz|usz|'
             r'c8|c16|c32|c64|void|bool)\b', Keyword.Type),
            (r'//.*?$', Comment.Singleline),
            (r'/\*', Comment.Multiline, 'comment'),
            (r'\b[A-Z]\w*\b', Keyword.Type),
            (r'\w[A-Za-z_]*:', Name.Function),
            (r'!\[', Comment.Preproc, 'preproc'),
            (r'\![a-z_]\w*\b', Comment.Preproc),
            (r'\'[^\']\'', Literal.String.Char),  # char-lit
            (r'\'\\[^\']\'', Literal.String.Char),  # escaped char-lit
            (r'"', Literal.String, "string"),  # string
            (r'\'[a-z_]\w*', Keyword.Type),
            (r' +', Text),
            (r'[0-9_]+\.[0-9_]+(f16|f32|f64)?', Literal.Number.Float),
            (r'[0-9_]+(i8|i16|i32|i64|isz|u8|u16|u32|u64|usz|i|u)?',
                Literal.Number.Integer),
            (r'[!@#%&*\-+=|;,.<>/?]', Operator),
            (r'\->', Operator),
            (r'[:|()\[\]\{\}]', Punctuation),
            (r'\b\w+\b', Text),
        ],
        'comment': [
            (r'\*/', Comment.Multiline, '#pop'),
            (r'\n', Comment.Multiline),
            (r'.', Comment.Multiline),
            (r'/\*', Comment.Multiline, '#push'),
        ],
        'preproc': [
            (r']', Comment.Preproc, '#pop'),
            (r'\b(if|elif|else|import|mut|with|global|for|in|do|while|'
             r'let|export|continue|break|return|this|is|ext|new|match|'
             r'trait|module|ante|type|where|when|fun|var|and|or|not|then|'
             r'do|pub|pro|pri|const|raw|noinit)\b', Keyword),
            (r'\b(true|false)\b', Literal.Boolean),
            (r'\b(i8|i16|i32|i64|u8|u16|u32|u64|f16|f32|f64|isz|usz|'
             r'c8|c16|c32|c64|void|bool)\b', Keyword.Type),
            (r'\b[a-z_]\w*\b', Comment.Preproc),
            (r'[!@#%&*\-+=|;,.<>/?]', Comment.Preproc),
            (r'\->', Comment.Preproc),
            (r'[:|()\[\]\{\}]', Comment.Preproc),
            include('root'),
        ],
        'string': [
            ('${', Text, 'interpolation'),
            ('\\"', Literal.Number),
            ('[^"]*\n', Literal.String),
            ('[^"]*\\\\"', Literal.String),
            ('[^"]*"', Literal.String, '#pop'),
        ],
        'interpolation': [
            ('}', Text, '#pop'),
            include('root')
        ]
    }
