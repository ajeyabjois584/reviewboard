import imp
        super(FileDiffMigrationTests, self).setUp()

        super(HighlightRegionTest, self).setUp()

            imp.find_module('mercurial')
    def setUp(self):
        filediff = FileDiff(source_file='foo', diffset=DiffSet())
        self.generator = DiffChunkGenerator(None, filediff)

        deep_equal(self.generator._get_line_changed_regions(None, None),
        regions = self.generator._get_line_changed_regions(old, new)
        regions = self.generator._get_line_changed_regions(old, new)
        regions = self.generator._get_line_changed_regions(old, new)
    def test_indent_spaces(self):
        """Testing DiffChunkGenerator._serialize_indentation with spaces"""
        self.assertEqual(self.generator._serialize_indentation('    '),
                         '&gt;&gt;&gt;&gt;')

    def test_indent_tabs(self):
        """Testing DiffChunkGenerator._serialize_indentation with tabs"""
        self.assertEqual(self.generator._serialize_indentation('\t'),
                         '&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&gt;|')

    def test_indent_spaces_and_tabs(self):
        """Testing DiffChunkGenerator._serialize_indentation
        with spaces and tabs
        """
        self.assertEqual(self.generator._serialize_indentation('   \t'),
                         '&gt;&gt;&gt;&mdash;&mdash;&mdash;&gt;|')

    def test_indent_tabs_and_spaces(self):
        """Testing DiffChunkGenerator._serialize_indentation
        with tabs and spaces
        """
        self.assertEqual(
            self.generator._serialize_indentation('\t   '),
            '&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&gt;|&gt;&gt;&gt;')

    def test_indent_9_spaces_and_tab(self):
        """Testing DiffChunkGenerator._serialize_indentation
        with 9 spaces and tab
        """
        self.assertEqual(
            self.generator._serialize_indentation('       \t'),
            '&gt;&gt;&gt;&gt;&gt;&gt;&gt;|')

    def test_indent_8_spaces_and_tab(self):
        """Testing DiffChunkGenerator._serialize_indentation
        with 8 spaces and tab
        """
        self.assertEqual(
            self.generator._serialize_indentation('      \t'),
            '&gt;&gt;&gt;&gt;&gt;&gt;&gt;|')

    def test_indent_7_spaces_and_tab(self):
        """Testing DiffChunkGenerator._serialize_indentation
        with 7 spaces and tab
        """
        self.assertEqual(
            self.generator._serialize_indentation('     \t'),
            '&gt;&gt;&gt;&gt;&gt;&mdash;&gt;|')

    def test_unindent_spaces(self):
        """Testing DiffChunkGenerator._serialize_unindentation with spaces"""
        self.assertEqual(self.generator._serialize_unindentation('    '),
                         '&lt;&lt;&lt;&lt;')

    def test_unindent_tabs(self):
        """Testing DiffChunkGenerator._serialize_unindentation with tabs"""
        self.assertEqual(self.generator._serialize_unindentation('\t'),
                         '|&lt;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;')

    def test_unindent_spaces_and_tabs(self):
        """Testing DiffChunkGenerator._serialize_unindentation
        with spaces and tabs
        """
        self.assertEqual(self.generator._serialize_unindentation('   \t'),
                         '&lt;&lt;&lt;|&lt;&mdash;&mdash;&mdash;')

    def test_unindent_tabs_and_spaces(self):
        """Testing DiffChunkGenerator._serialize_unindentation
        with tabs and spaces
        """
        self.assertEqual(
            self.generator._serialize_unindentation('\t   '),
            '|&lt;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash;&lt;&lt;&lt;')

    def test_unindent_9_spaces_and_tab(self):
        """Testing DiffChunkGenerator._serialize_unindentation
        with 9 spaces and tab
        """
        self.assertEqual(
            self.generator._serialize_unindentation('       \t'),
            '&lt;&lt;&lt;&lt;&lt;&lt;&lt;|')

    def test_unindent_8_spaces_and_tab(self):
        """Testing DiffChunkGenerator._serialize_unindentation
        with 8 spaces and tab
        """
        self.assertEqual(
            self.generator._serialize_unindentation('      \t'),
            '&lt;&lt;&lt;&lt;&lt;&lt;|&lt;')

    def test_unindent_7_spaces_and_tab(self):
        """Testing DiffChunkGenerator._serialize_unindentation
        with 7 spaces and tab
        """
        self.assertEqual(
            self.generator._serialize_unindentation('     \t'),
            '&lt;&lt;&lt;&lt;&lt;|&lt;&mdash;')

    def test_highlight_indent(self):
        """Testing DiffChunkGenerator._highlight_indentation
        with indentation
        """
        self.assertEqual(
            self.generator._highlight_indentation('', '        foo', True, 4),
            ('', '<span class="indent">&gt;&gt;&gt;&gt;</span>    foo'))

    def test_highlight_unindent(self):
        """Testing DiffChunkGenerator._highlight_indentation
        with unindentation
        """
        self.assertEqual(
            self.generator._highlight_indentation('        foo', '', False, 4),
            ('<span class="unindent">&lt;&lt;&lt;&lt;</span>    foo', ''))


class DiffOpcodeGeneratorTests(TestCase):
    """Unit tests for DiffOpcodeGenerator."""
    def setUp(self):
        self.generator = get_diff_opcode_generator(MyersDiffer('', ''))

    def test_indentation_with_spaces(self):
        """Testing DiffOpcodeGenerator._calculate_indentation
        with indenting spaces
        """
        self.assertEqual(
            self.generator._compute_line_indentation(
                '    foo',
                '        foo'),
            (True, 4))

    def test_indentation_with_tabs(self):
        """Testing DiffOpcodeGenerator._calculate_indentation
        with indenting tabs
        """
        self.assertEqual(
            self.generator._compute_line_indentation(
                '    foo',
                '\t    foo'),
            (True, 1))

    def test_indentation_with_spaces_and_tabs(self):
        """Testing DiffOpcodeGenerator._calculate_indentation
        with indenting spaces and tabs
        """
        self.assertEqual(
            self.generator._compute_line_indentation(
                '    foo',
                '  \t    foo'),
            (True, 3))

    def test_indentation_with_tabs_and_spaces(self):
        """Testing DiffOpcodeGenerator._calculate_indentation
        with indenting tabs and spaces
        """
        self.assertEqual(
            self.generator._compute_line_indentation(
                '    foo',
                '\t      foo'),
            (True, 3))

    def test_indentation_with_replacing_tabs_with_spaces(self):
        """Testing DiffOpcodeGenerator._calculate_indentation
        with replacing tabs with spaces
        """
        self.assertEqual(
            self.generator._compute_line_indentation(
                '\tfoo',
                '        foo'),
            (True, 1))

    def test_indentation_with_replacing_tabs_with_spaces(self):
        """Testing DiffOpcodeGenerator._calculate_indentation
        with spaces with tabs
        """
        self.assertEqual(
            self.generator._compute_line_indentation(
                '        foo',
                '\tfoo'),
            None)

    def test_indentation_with_no_changes(self):
        """Testing DiffOpcodeGenerator._calculate_indentation
        without changes
        """
        self.assertEqual(
            self.generator._compute_line_indentation(
                '    foo',
                '    foo'),
            None)

    def test_unindentation_with_spaces(self):
        """Testing DiffOpcodeGenerator._calculate_indentation
        with unindenting spaces
        """
        self.assertEqual(
            self.generator._compute_line_indentation(
                '        foo',
                '    foo'),
            (False, 4))

    def test_unindentation_with_tabs(self):
        """Testing DiffOpcodeGenerator._calculate_indentation
        with unindenting tabs
        """
        self.assertEqual(
            self.generator._compute_line_indentation(
                '\t    foo',
                '    foo'),
            (False, 1))

    def test_unindentation_with_spaces_and_tabs(self):
        """Testing DiffOpcodeGenerator._calculate_indentation
        with unindenting spaces and tabs
        """
        self.assertEqual(
            self.generator._compute_line_indentation(
                '  \t    foo',
                '    foo'),
            (False, 3))

    def test_unindentation_with_tabs_and_spaces(self):
        """Testing DiffOpcodeGenerator._calculate_indentation
        with unindenting tabs and spaces
        """
        self.assertEqual(
            self.generator._compute_line_indentation(
                '\t      foo',
                '    foo'),
            (False, 3))

    def test_unindentation_with_replacing_tabs_with_spaces(self):
        """Testing DiffOpcodeGenerator._calculate_indentation
        with replacing tabs with spaces
        """
        self.assertEqual(
            self.generator._compute_line_indentation(
                '\tfoo',
                '    foo'),
            (False, 1))
