import unittest
from django.test import TestCase
from djblets.util.misc import cache_memoize
                          ("equal",  0, 6, 2, 8)])
                         [("equal",   0, 4, 0, 4),
                          ("insert",  5, 5, 5, 9),
                          ("equal",   5, 8, 9, 12)])
        f = open(os.path.join(self.PREFIX, "orig_src", filename), "r")
        a = f.readlines()
        f.close()
        f = open(os.path.join(self.PREFIX, "new_src", filename), "r")
        b = f.readlines()
        f.close()
        print result

class DiffParserTest(unittest.TestCase):
            self.failUnless(file.origFile.startswith("%s/orig_src/" %
            self.failUnless(file.newFile.startswith("%s/new_src/" %
    def testMoveDetection(self):
        """Testing move detection"""
        differ = MyersDiffer(old.splitlines(), new.splitlines())
        opcode_generator = get_diff_opcode_generator(differ)

            tag = opcodes[0]
            if tag == 'delete':
                if 'moved' in meta:
                    r_moves.append(meta['moved'])
            elif tag == 'insert':
                if 'moved' in meta:
                    i_moves.append(meta['moved'])

        self.assertEqual(len(r_moves), 1)
        self.assertEqual(len(i_moves), 1)

        moves = [
            (15, 28),
            (16, 29),
            (17, 30),
            (18, 31),
            (19, 32)
        ]
        for i, j in moves:
            self.assertTrue(j in i_moves[0])
            self.assertTrue(i in r_moves[0])
            self.assertEqual(i_moves[0][j], i)
            self.assertEqual(r_moves[0][i], j)
    def _get_file(self, *relative):
        f = open(os.path.join(*tuple([self.PREFIX] + list(relative))))
        data = f.read()
        f.close()
        return data
                                          '<span class="hl">abc</span>')
                                          '<span class="hl">a</span>bc')
        repository = Repository.objects.get(pk=1)
        repository = Repository.objects.get(pk=1)
        f = open(os.path.join(self.PREFIX, "diffs", "context", "foo.c.diff"),
                 "r")
        data = f.read()
        f.close()
            'Index: README\n'
            '==========================================================='
            '========\n'
            '--- README  (revision 123)\n'
            '+++ README  (new)\n'
            '@ -1,1 +1,1 @@\n'
            '-blah..\n'
            '+blah blah\n'
        repository = Repository.objects.create(
            name='Subversion SVN',
            path='file://%s' % (os.path.join(os.path.dirname(__file__),
                                             '..', 'scmtools', 'testdata',
                                             'svn_repo')),
            tool=Tool.objects.get(name='Subversion'))
            'Index: README\n'
            '==========================================================='
            '========\n'
            '--- README  (revision 123)\n'
            '+++ README  (new)\n'
            '@ -1,1 +1,1 @@\n'
            '-blah..\n'
            '+blah blah\n'
        repository = Repository.objects.create(
            name='Subversion SVN',
            path='file://%s' % (os.path.join(os.path.dirname(__file__),
                                             '..', 'scmtools', 'testdata',
                                             'svn_repo')),
            tool=Tool.objects.get(name='Subversion'))
            'Index: README\n'
            '==========================================================='
            '========\n'
            '--- README  (revision 124)\n'
            '+++ README  (new)\n'
            '@ -1,1 +1,1 @@\n'
            '-blah blah\n'
            '+blah!\n'
            'Index: README\n'
            '==========================================================='
            '========\n'
            '--- README  (revision 123)\n'
            '+++ README  (new)\n'
            '@ -1,1 +1,1 @@\n'
            '-blah..\n'
            '+blah blah\n'
            'Index: UNUSED\n'
            '==========================================================='
            '========\n'
            '--- UNUSED  (revision 123)\n'
            '+++ UNUSED  (new)\n'
            '@ -1,1 +1,1 @@\n'
            '-foo\n'
            '+bar\n'
        # Note that we're using SVN here for the test just because it's
        # a bit easier to test with than Git (easier diff parsing logic
        # and revision numbers).
        repository = Repository.objects.create(
            name='Subversion SVN',
            path='file://%s' % (os.path.join(os.path.dirname(__file__),
                                             '..', 'scmtools', 'testdata',
                                             'svn_repo')),
            tool=Tool.objects.get(name='Subversion'))
        self.assertTrue(('/README', '123') in saw_file_exists)
        self.assertFalse(('/UNUSED', '123') in saw_file_exists)
            '# Node ID a6fc203fee9091ff9739c9c00cd4a6694e023f48\n'
            '# Parent  7c4735ef51a7c665b5654f1a111ae430ce84ebbd\n'
            'diff --git a/doc/readme b/doc/readme\n'
            '--- a/doc/readme\n'
            '+++ b/doc/readme\n'
            '@@ -1,3 +1,3 @@\n'
            ' Hello\n'
            '-\n'
            '+...\n'
            ' goodbye\n'
            '# Node ID 7c4735ef51a7c665b5654f1a111ae430ce84ebbd\n'
            '# Parent  661e5dd3c4938ecbe8f77e2fdfa905d70485f94c\n'
            'diff --git a/doc/newfile b/doc/newfile\n'
            'new file mode 100644\n'
            '--- /dev/null\n'
            '+++ b/doc/newfile\n'
            '@@ -0,0 +1,1 @@\n'
            '+Lorem ipsum\n'
                for a, b in map(None, A, B):
        filediff = FileDiff(source_file='foo', diffset=DiffSet())
        generator = DiffChunkGenerator(None, filediff)

        deep_equal(generator._get_line_changed_regions(None, None),
        regions = generator._get_line_changed_regions(old, new)
        regions = generator._get_line_changed_regions(old, new)
        regions = generator._get_line_changed_regions(old, new)