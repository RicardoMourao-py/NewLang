class PrePro:
    @staticmethod
    def filter(source: str) -> str:
        """
        Remove comentários do código.
        """
        lines = source.split('\n')
        result = []
        in_comment_block = False

        for line in lines:
            if not in_comment_block:
                line = line.split('//')[0]
                if '/*' in line:
                    in_comment_block = True
                    line = line.split('/*')[0]
                if line.strip():
                    result.append(line)
            else:
                if '*/' in line:
                    in_comment_block = False
                    line = line.split('*/', 1)[1]
                else:
                    line = ''

        return '\n'.join(result)
