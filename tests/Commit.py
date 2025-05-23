############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Danilo Martins <mawkee@gmail.com>                             #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Kian-Meng Ang <kianmeng.ang@gmail.com>                        #
# Copyright 2024 iarspider <iarspider@gmail.com>                               #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

from __future__ import annotations

from . import Framework


class Commit(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.commit = self.g.get_user().get_repo("PyGithub").get_commit("1292bf0e22c796e91cc3d6e24b544aece8c21f2a")
        self.commit.author.login  # to force lazy completion

    def testAttributes(self):
        self.assertEqual(self.commit.author.login, "jacquev6")
        self.assertEqual(
            self.commit.comments_url,
            "https://api.github.com/repos/jacquev6/PyGithub/commits/1292bf0e22c796e91cc3d6e24b544aece8c21f2a/comments",
        )
        self.assertEqual(
            self.commit.commit.url,
            "https://api.github.com/repos/jacquev6/PyGithub/git/commits/1292bf0e22c796e91cc3d6e24b544aece8c21f2a",
        )
        self.assertEqual(self.commit.committer.login, "jacquev6")
        self.assertEqual(len(list(self.commit.files)), 1)
        self.assertEqual(self.commit.files.totalCount, 1)
        self.assertEqual(self.commit.files[0].additions, 0)
        self.assertEqual(
            self.commit.files[0].blob_url,
            "https://github.com/jacquev6/PyGithub/blob/1292bf0e22c796e91cc3d6e24b544aece8c21f2a/github%2FGithubObjects%2FGitAuthor.py",
        )
        self.assertEqual(self.commit.files[0].changes, 20)
        self.assertEqual(self.commit.files[0].deletions, 20)
        self.assertEqual(self.commit.files[0].filename, "github/GithubObjects/GitAuthor.py")
        self.assertTrue(isinstance(self.commit.files[0].patch, str))
        self.assertEqual(
            self.commit.files[0].raw_url,
            "https://github.com/jacquev6/PyGithub/raw/1292bf0e22c796e91cc3d6e24b544aece8c21f2a/github%2FGithubObjects%2FGitAuthor.py",
        )
        self.assertEqual(self.commit.files[0].sha, "ca6a3c616fc1367b6d01d04a7cf6ee27cf216f26")
        self.assertEqual(self.commit.files[0].status, "modified")
        self.assertEqual(
            self.commit.html_url, "https://github.com/jacquev6/PyGithub/commit/1292bf0e22c796e91cc3d6e24b544aece8c21f2a"
        )
        self.assertEqual(
            self.commit.node_id, "MDY6Q29tbWl0NDQ2MzY1NzM1OjEyOTJiZjBlMjJjNzk2ZTkxY2MzZDZlMjRiNTQ0YWVjZThjMjFmMmE="
        )
        self.assertEqual(len(self.commit.parents), 1)
        self.assertEqual(self.commit.parents[0].sha, "b46ed0dfde5ad02d3b91eb54a41c5ed960710eae")
        self.assertIsNone(self.commit.repository)
        self.assertEqual(self.commit.sha, "1292bf0e22c796e91cc3d6e24b544aece8c21f2a")
        self.assertEqual(self.commit.stats.deletions, 20)
        self.assertEqual(self.commit.stats.additions, 0)
        self.assertEqual(self.commit.stats.total, 20)
        self.assertIsNone(self.commit.text_matches)
        self.assertEqual(
            self.commit.url,
            "https://api.github.com/repos/jacquev6/PyGithub/commits/1292bf0e22c796e91cc3d6e24b544aece8c21f2a",
        )
        self.assertEqual(self.commit.commit.tree.sha, "4c6bd50994f0f9823f898b1c6c964ad7d4fa11ab")
        self.assertEqual(repr(self.commit), 'Commit(sha="1292bf0e22c796e91cc3d6e24b544aece8c21f2a")')

    def testGetBranchesWhereHead(self):
        repo = self.g.get_repo("PyGithub/PyGithub")
        commit = repo.get_commit("0791cc7b1a706ab5d7c607ddff35de4d486ba3e9")
        self.assertListKeyEqual(
            commit.get_branches_where_head(),
            lambda b: b.name,
            ["release-v2-0"],
        )

    def testGetComments(self):
        self.assertListKeyEqual(
            self.commit.get_comments(),
            lambda c: c.id,
            [1347033, 1347083, 1347397, 1349654],
        )

    def testCreateComment(self):
        comment = self.commit.create_comment("Comment created by PyGithub")
        self.assertEqual(comment.id, 1361949)
        self.assertEqual(comment.line, None)
        self.assertEqual(comment.path, None)
        self.assertEqual(comment.position, None)

    def testCreateCommentOnFileLine(self):
        comment = self.commit.create_comment(
            "Comment created by PyGithub",
            path="codegen/templates/GithubObject.MethodBody.UseResult.py",
            line=26,
        )
        self.assertEqual(comment.id, 1362000)
        self.assertEqual(comment.line, 26)
        self.assertEqual(comment.path, "codegen/templates/GithubObject.MethodBody.UseResult.py")
        self.assertEqual(comment.position, None)

    def testCreateCommentOnFilePosition(self):
        comment = self.commit.create_comment(
            "Comment also created by PyGithub",
            path="codegen/templates/GithubObject.MethodBody.UseResult.py",
            position=3,
        )
        self.assertEqual(comment.id, 1362001)
        self.assertEqual(comment.line, None)
        self.assertEqual(comment.path, "codegen/templates/GithubObject.MethodBody.UseResult.py")
        self.assertEqual(comment.position, 3)

    def testCreateStatusWithoutOptionalParameters(self):
        status = self.commit.create_status("pending")
        self.assertEqual(status.id, 277031)
        self.assertEqual(status.state, "pending")
        self.assertEqual(status.target_url, None)
        self.assertEqual(status.description, None)

    def testCreateStatusWithAllParameters(self):
        status = self.commit.create_status(
            "success",
            "https://github.com/jacquev6/PyGithub/issues/67",
            "Status successfully created by PyGithub",
        )
        self.assertEqual(status.id, 277040)
        self.assertEqual(status.state, "success")
        self.assertEqual(status.target_url, "https://github.com/jacquev6/PyGithub/issues/67")
        self.assertEqual(status.description, "Status successfully created by PyGithub")

    def testGetPulls(self):
        commit = self.g.get_user().get_repo("PyGithub").get_commit("e44d11d565c022496544dd6ed1f19a8d718c2b0c")
        self.assertListKeyEqual(commit.get_pulls(), lambda c: c.number, [1431])
