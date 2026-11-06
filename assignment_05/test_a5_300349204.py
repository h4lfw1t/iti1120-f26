"""Unit tests for assignment 05.

The example-run transcript is interactive, so the tests call the assignment
functions directly and use the transcript's reported values as expectations.
"""

import builtins
import contextlib
import importlib.util
import io
import unittest
from pathlib import Path
from unittest.mock import patch


ASSIGNMENT_DIR = Path(__file__).parent
MODULE_PATH = ASSIGNMENT_DIR / "a5_300349204" / "a5_300349204.py"


def load_assignment_module():
    """Load the submission while supplying the inputs used by its driver."""
    spec = importlib.util.spec_from_file_location("a5_submission", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    inputs = iter(
        [
            str(ASSIGNMENT_DIR / "net1.txt"),
            "4",  # recommendation user
            "2",  # first common-friend user
            "4",  # second common-friend user
        ]
    )
    with patch.object(builtins, "input", side_effect=lambda _="": next(inputs)):
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(module)
    return module


a5 = load_assignment_module()


CASES = {
    "net1.txt": {
        "users": 10,
        "maximum": 5,
        "average": 3.8,
        "most": [1, 2, 8],
        "k": (0, 10),
        "knows_everyone": False,
        "recommend": (4, 2),
        "common": ((2, 4), [6, 8]),
    },
    "net2.txt": {
        "users": 10,
        "maximum": 9,
        "average": 5.0,
        "most": [0],
        "k": (0, 10),
        "knows_everyone": True,
        "recommend": (4, 2),
        "common": ((1, 2), [0, 6, 9]),
    },
    "net3.txt": {
        "users": 13,
        "maximum": 9,
        "average": 4.153846153846154,
        "most": [0],
        "k": (2, 11),
        "knows_everyone": False,
        "recommend": (0, None),
        "common": ((0, 112), []),
    },
    "big.txt": {
        "users": 1000,
        "maximum": 347,
        "average": 19.78,
        "most": [0],
        "k": (238, 1),
        "knows_everyone": False,
        "recommend": (242, 196),
        "common": ((242, 196), [0, 53, 92, 180, 194, 204, 249, 254, 266, 330, 346]),
    },
    "huge.txt": {
        "users": 4039,
        "maximum": 1045,
        "average": 43.69101262688784,
        "most": [107],
        "k": (913, 1),
        "knows_everyone": False,
        "recommend": (1045, 1030),
        "common": ((1030, 1045), [107, 909, 955, 1043, 1111, 1197, 1368, 1788]),
    },
}


class TestNetworks(unittest.TestCase):
    def network(self, filename):
        return a5.create_network(str(ASSIGNMENT_DIR / filename))

    def test_all_recorded_network_statistics(self):
        for filename, expected in CASES.items():
            with self.subTest(filename=filename):
                network = self.network(filename)
                self.assertEqual(len(network), expected["users"])
                self.assertEqual(a5.maximum_num_friends(network), expected["maximum"])
                self.assertAlmostEqual(
                    a5.average_num_friends(network), expected["average"]
                )
                self.assertEqual(
                    a5.people_with_most_friends(network), expected["most"]
                )
                k, count = expected["k"]
                self.assertEqual(a5.k_or_more_friends(network, k), count)
                self.assertEqual(
                    a5.knows_everyone(network), expected["knows_everyone"]
                )

    def test_network_is_sorted_and_friendships_are_symmetric(self):
        for filename in CASES:
            with self.subTest(filename=filename):
                network = self.network(filename)
                ids = [user_id for user_id, _ in network]
                self.assertEqual(ids, sorted(ids))
                for user_id, friends in network:
                    self.assertEqual(friends, sorted(friends))
                    self.assertEqual(len(friends), len(set(friends)))
                    for friend in friends:
                        friend_record = dict(network)[friend]
                        self.assertIn(user_id, friend_record)

    def test_all_recorded_recommendations(self):
        for filename, expected in CASES.items():
            user, recommendation = expected["recommend"]
            with self.subTest(filename=filename):
                self.assertEqual(
                    a5.recommend(user, self.network(filename)), recommendation
                )

    def test_all_recorded_common_friend_lists(self):
        for filename, expected in CASES.items():
            (user1, user2), common = expected["common"]
            with self.subTest(filename=filename):
                self.assertEqual(
                    a5.getCommonFriends(user1, user2, self.network(filename)),
                    common,
                )

    def test_net1_exact_adjacency(self):
        self.assertEqual(
            self.network("net1.txt"),
            [
                (0, [1, 2, 3]),
                (1, [0, 4, 6, 7, 9]),
                (2, [0, 3, 6, 8, 9]),
                (3, [0, 2, 8, 9]),
                (4, [1, 6, 7, 8]),
                (5, [9]),
                (6, [1, 2, 4, 8]),
                (7, [1, 4, 8]),
                (8, [2, 3, 4, 6, 7]),
                (9, [1, 2, 3, 5]),
            ],
        )

    def test_k_boundaries(self):
        network = self.network("net1.txt")
        self.assertEqual(a5.k_or_more_friends(network, 0), len(network))
        self.assertEqual(a5.k_or_more_friends(network, 6), 0)

    def test_additional_output_example_queries(self):
        net1 = self.network("net1.txt")
        net2 = self.network("net2.txt")
        net3 = self.network("net3.txt")
        net4 = self.network("big.txt")

        self.assertEqual(a5.getCommonFriends(3, 1, net1), [0, 9])
        self.assertEqual(a5.getCommonFriends(0, 112, net3), [])
        self.assertEqual(a5.getCommonFriends(217, 163, net4), [0, 100, 119, 150])
        self.assertEqual(a5.recommend(6, net1), 7)
        self.assertEqual(a5.recommend(4, net2), 2)
        self.assertIsNone(a5.recommend(0, net2))
        self.assertEqual(a5.recommend(114, net3), 100)
        self.assertIsNone(a5.recommend(112, net3))
        self.assertEqual(a5.recommend(217, net4), 163)
        self.assertEqual(a5.k_or_more_friends(net1, 5), 3)
        self.assertEqual(a5.k_or_more_friends(net2, 8), 1)
        self.assertEqual(a5.k_or_more_friends(net3, 12), 0)
        self.assertEqual(a5.k_or_more_friends(net4, 70), 33)

    def test_additional_output_example_network_records(self):
        net2 = self.network("net2.txt")
        net3 = self.network("net3.txt")
        self.assertEqual(net2[0], (0, list(range(1, 10))))
        self.assertEqual(net2[5], (5, [0, 9]))
        self.assertEqual(net3[-3:], [
            (100, [112]),
            (112, [100, 114]),
            (114, [112]),
        ])

        net4 = self.network("big.txt")
        self.assertEqual(net4[500], (
            500,
            [348, 353, 354, 355, 361, 363, 368, 373, 374, 376, 378, 382,
             388, 391, 392, 396, 400, 402, 404, 408, 409, 410, 412, 414,
             416, 417, 421, 423, 428, 431, 438, 439, 444, 445, 450, 452,
             455, 463, 465, 474, 475, 483, 484, 487, 492, 493, 497, 503,
             506, 507, 513, 514, 517, 519, 520, 521, 524, 525, 527, 531,
             537, 538, 542, 546, 547, 548, 553, 555, 556, 557, 560, 563,
             565, 566, 580, 591, 601, 604, 614, 637, 645, 651, 683],
        ))
        self.assertEqual(net4[501], (501, [198, 348, 364, 393, 399, 441, 476, 564]))


class TestInteractiveHelpers(unittest.TestCase):
    def test_is_valid_file_name_rejects_missing_file(self):
        with patch.object(builtins, "input", return_value="missing-file.txt"):
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertIsNone(a5.is_valid_file_name())

    def test_get_file_name_retries_until_file_exists(self):
        valid = str(ASSIGNMENT_DIR / "net1.txt")
        with patch.object(
            builtins,
            "input",
            side_effect=["bla.txt", "lasjd", "33", valid],
        ):
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(a5.get_file_name(), valid)

    def test_get_uid_retries_all_invalid_inputs_in_transcript(self):
        cases = {
            "net1.txt": (["twenty", "3.4", "4"], 4),
            "net2.txt": (["zero", "-10", "52", "4.5", "4"], 4),
            "big.txt": (["20000", "242"], 242),
            "huge.txt": (["5600", "4039", "4100", "1045"], 1045),
        }
        for filename, (inputs, expected_id) in cases.items():
            with self.subTest(filename=filename):
                network = a5.create_network(str(ASSIGNMENT_DIR / filename))
                with patch.object(builtins, "input", side_effect=inputs):
                    with contextlib.redirect_stdout(io.StringIO()):
                        self.assertEqual(a5.get_uid(network), expected_id)

    def test_get_uid_additional_output_example_inputs(self):
        network = a5.create_network(str(ASSIGNMENT_DIR / "net1.txt"))
        with patch.object(
            builtins,
            "input",
            side_effect=["alsj", "twenty", "9aslj", "100000", "4.5", "-10", "-1", "7"],
        ):
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(a5.get_uid(network), 7)


if __name__ == "__main__":
    unittest.main()
