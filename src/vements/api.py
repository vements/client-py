#!/usr/bin/env python

# Copyright 2023 Monster Street Systems LLC
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# NB: This is a generated file; any changes will be lost.

from datetime import datetime
from enum import Enum
from sys import stderr
from typing import Optional, Set

from ulid import ULID

from vements import types
from vements.client import Client, ClientConfig


class Output(Enum):
    TEXT = 0
    OBJECT = 1


class Resource:
    _client: Client
    _output: Output
    _verbose: bool

    def __init__(self, client: Client, output: Output = Output.OBJECT, verbose: bool = False):
        self._client = client
        self._output = output
        self._verbose = verbose


class Achievement(Resource):
    def leaderboard(
        self,
        achievement_id: str,
    ):
        """Achievement leaderboard

        Reads and returns achievement leaderboard

        This is a GET operation.  It returns the response text
        or an instance of AchievementLeaderboardResponse.
        """
        path = f"/achievement/{achievement_id}/leaderboard"
        params = {}

        try:
            response = self._client.get(path, params=params)
        except Exception as ex:
            print("client get exception:", ex, file=stderr)
            return
        if response.status_code < 200 or response.status_code >= 300:
            print(
                "client get client exception:", response.status_code, response.content, file=stderr
            )
            return
        return (
            response.text
            if self._output == Output.TEXT
            else types.AchievementLeaderboardResponse(**response.json())
        )

    def record(
        self,
        achievement_id: str,
        participant_id: ULID | str,
        value: int,
        recorded: Optional[datetime],
    ):
        """Record achievement progress

        Records and returns achievement progress

        This is a PUT operation.  It returns the response text
        or an instance of AchievementProgressResponse.
        """
        path = f"/achievement/{achievement_id}/progress"
        params = {}
        params["participant_id"] = participant_id
        params["value"] = value
        params["recorded"] = recorded

        try:
            response = self._client.put(path, params)
        except Exception as ex:
            print("client put exception:", ex, file=stderr)
            return
        if response.status_code < 200 or response.status_code >= 300:
            print(
                "client put client exception:", response.status_code, response.content, file=stderr
            )
            return
        return (
            response.text
            if self._output == Output.TEXT
            else types.AchievementProgressResponse(**response.json())
        )

    def list(
        self,
        project_id: ULID | str,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ):
        """List achievements

        Reads and returns list of achievements in the given project

        This is a GET operation.  It returns the response text
        or an instance of AchievementListResponse.
        """
        path = f"/achievement"
        params = {}
        if project_id is not None:
            params["project_id"] = project_id
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset

        try:
            response = self._client.get(path, params=params)
        except Exception as ex:
            print("client get exception:", ex, file=stderr)
            return
        if response.status_code < 200 or response.status_code >= 300:
            print(
                "client get client exception:", response.status_code, response.content, file=stderr
            )
            return
        return (
            response.text
            if self._output == Output.TEXT
            else types.AchievementListResponse(**response.json())
        )

    def create(
        self,
        project_id: ULID | str,
        display: str,
        goal: int,
        repeats: int,
        locked_image: Optional[str],
        unlocked_image: Optional[str],
        position: int,
        public: bool,
        extra: Optional[object],
    ):
        """Create achievement

        Creates and returns achievement in the given project

        This is a PUT operation.  It returns the response text
        or an instance of AchievementCreateResponse.
        """
        path = f"/achievement"
        params = {}
        params["project_id"] = project_id
        params["display"] = display
        params["goal"] = goal
        params["repeats"] = repeats
        params["locked_image"] = locked_image
        params["unlocked_image"] = unlocked_image
        params["position"] = position
        params["public"] = public
        params["extra"] = extra

        try:
            response = self._client.put(path, params)
        except Exception as ex:
            print("client put exception:", ex, file=stderr)
            return
        if response.status_code < 200 or response.status_code >= 300:
            print(
                "client put client exception:", response.status_code, response.content, file=stderr
            )
            return
        return (
            response.text
            if self._output == Output.TEXT
            else types.AchievementCreateResponse(**response.json())
        )

    def read(
        self,
        achievement_id: ULID | str,
    ):
        """Read achievement

        Reads and returns achievement by achievement id

        This is a GET operation.  It returns the response text
        or an instance of AchievementReadResponse.
        """
        path = f"/achievement/{achievement_id}"
        params = {}

        try:
            response = self._client.get(path, params=params)
        except Exception as ex:
            print("client get exception:", ex, file=stderr)
            return
        if response.status_code < 200 or response.status_code >= 300:
            print(
                "client get client exception:", response.status_code, response.content, file=stderr
            )
            return
        return (
            response.text
            if self._output == Output.TEXT
            else types.AchievementReadResponse(**response.json())
        )

    def update(
        self,
        achievement_id: ULID | str,
        display: str,
        goal: int,
        repeats: int,
        locked_image: Optional[str],
        unlocked_image: Optional[str],
        position: int,
        public: bool,
        extra: Optional[object],
    ):
        """Update achievement

        Updates and returns achievement by achievement id

        This is a POST operation.  It returns the response text
        or an instance of AchievementUpdateResponse.
        """
        path = f"/achievement/{achievement_id}"
        params = {}
        params["display"] = display
        params["goal"] = goal
        params["repeats"] = repeats
        params["locked_image"] = locked_image
        params["unlocked_image"] = unlocked_image
        params["position"] = position
        params["public"] = public
        params["extra"] = extra

        try:
            response = self._client.post(path, params)
        except Exception as ex:
            print("client post exception:", ex, file=stderr)
            return
        if response.status_code < 200 or response.status_code >= 300:
            print(
                "client post client exception:",
                response.status_code,
                response.content,
                file=stderr,
            )
            return
        return (
            response.text
            if self._output == Output.TEXT
            else types.AchievementUpdateResponse(**response.json())
        )

    def delete(
        self,
        achievement_id: ULID | str,
    ):
        """Delete achievement by id.

        Delete achievement by achievement id

        This is a DELETE operation.  It returns the response text
        or an instance of AchievementDeleteResponse.
        """
        path = f"/achievement/{achievement_id}"

        try:
            response = self._client.delete(path)
        except Exception as ex:
            print("client delete exception:", ex, file=stderr)
            return
        if response.status_code < 200 or response.status_code >= 300:
            print(
                "client delete client exception:",
                response.status_code,
                response.content,
                file=stderr,
            )
            return
        return (
            response.text
            if self._output == Output.TEXT
            else types.AchievementDeleteResponse(**response.json())
        )


class Participant(Resource):
    def progress(
        self,
        participant_id: str,
    ):
        """Participant progress

        Reads and returns participant progress.

        This is a GET operation.  It returns the response text
        or an instance of ParticipantProgressResponse.
        """
        path = f"/participant/{participant_id}/progress"
        params = {}

        try:
            response = self._client.get(path, params=params)
        except Exception as ex:
            print("client get exception:", ex, file=stderr)
            return
        if response.status_code < 200 or response.status_code >= 300:
            print(
                "client get client exception:", response.status_code, response.content, file=stderr
            )
            return
        return (
            response.text
            if self._output == Output.TEXT
            else types.ParticipantProgressResponse(**response.json())
        )

    def scores(
        self,
        participant_id: str,
    ):
        """Participant scores

        Reads and returns participant scores.

        This is a GET operation.  It returns the response text
        or an instance of ParticipantScoresResponse.
        """
        path = f"/participant/{participant_id}/scores"
        params = {}

        try:
            response = self._client.get(path, params=params)
        except Exception as ex:
            print("client get exception:", ex, file=stderr)
            return
        if response.status_code < 200 or response.status_code >= 300:
            print(
                "client get client exception:", response.status_code, response.content, file=stderr
            )
            return
        return (
            response.text
            if self._output == Output.TEXT
            else types.ParticipantScoresResponse(**response.json())
        )

    def list(
        self,
        project_id: ULID | str,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ):
        """List participants

        Reads and returns list of participants in the given project

        This is a GET operation.  It returns the response text
        or an instance of ParticipantListResponse.
        """
        path = f"/participant"
        params = {}
        if project_id is not None:
            params["project_id"] = project_id
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset

        try:
            response = self._client.get(path, params=params)
        except Exception as ex:
            print("client get exception:", ex, file=stderr)
            return
        if response.status_code < 200 or response.status_code >= 300:
            print(
                "client get client exception:", response.status_code, response.content, file=stderr
            )
            return
        return (
            response.text
            if self._output == Output.TEXT
            else types.ParticipantListResponse(**response.json())
        )

    def create(
        self,
        project_id: ULID | str,
        display: str,
        external_id: str,
        image: Optional[str],
        extra: Optional[object],
    ):
        """Create participant

        Creates and returns participant in the given project

        This is a PUT operation.  It returns the response text
        or an instance of ParticipantCreateResponse.
        """
        path = f"/participant"
        params = {}
        params["project_id"] = project_id
        params["display"] = display
        params["external_id"] = external_id
        params["image"] = image
        params["extra"] = extra

        try:
            response = self._client.put(path, params)
        except Exception as ex:
            print("client put exception:", ex, file=stderr)
            return
        if response.status_code < 200 or response.status_code >= 300:
            print(
                "client put client exception:", response.status_code, response.content, file=stderr
            )
            return
        return (
            response.text
            if self._output == Output.TEXT
            else types.ParticipantCreateResponse(**response.json())
        )

    def read(
        self,
        participant_id: ULID | str,
    ):
        """Read participant

        Reads and returns participant by participant id

        This is a GET operation.  It returns the response text
        or an instance of ParticipantReadResponse.
        """
        path = f"/participant/{participant_id}"
        params = {}

        try:
            response = self._client.get(path, params=params)
        except Exception as ex:
            print("client get exception:", ex, file=stderr)
            return
        if response.status_code < 200 or response.status_code >= 300:
            print(
                "client get client exception:", response.status_code, response.content, file=stderr
            )
            return
        return (
            response.text
            if self._output == Output.TEXT
            else types.ParticipantReadResponse(**response.json())
        )

    def update(
        self,
        participant_id: ULID | str,
        display: str,
        external_id: str,
        image: Optional[str],
        extra: Optional[object],
    ):
        """Update participant

        Updates and returns participant by participant id

        This is a POST operation.  It returns the response text
        or an instance of ParticipantUpdateResponse.
        """
        path = f"/participant/{participant_id}"
        params = {}
        params["display"] = display
        params["external_id"] = external_id
        params["image"] = image
        params["extra"] = extra

        try:
            response = self._client.post(path, params)
        except Exception as ex:
            print("client post exception:", ex, file=stderr)
            return
        if response.status_code < 200 or response.status_code >= 300:
            print(
                "client post client exception:",
                response.status_code,
                response.content,
                file=stderr,
            )
            return
        return (
            response.text
            if self._output == Output.TEXT
            else types.ParticipantUpdateResponse(**response.json())
        )

    def delete(
        self,
        participant_id: ULID | str,
    ):
        """Delete participant by id.

        Delete participant by participant id

        This is a DELETE operation.  It returns the response text
        or an instance of ParticipantDeleteResponse.
        """
        path = f"/participant/{participant_id}"

        try:
            response = self._client.delete(path)
        except Exception as ex:
            print("client delete exception:", ex, file=stderr)
            return
        if response.status_code < 200 or response.status_code >= 300:
            print(
                "client delete client exception:",
                response.status_code,
                response.content,
                file=stderr,
            )
            return
        return (
            response.text
            if self._output == Output.TEXT
            else types.ParticipantDeleteResponse(**response.json())
        )


class Scoreboard(Resource):
    def record(
        self,
        scoreboard_id: str,
        participant_id: ULID | str,
        value: int,
        recorded: Optional[datetime],
    ):
        """Record a scoreboard score

        Records and returns a scoreboard score.

        This is a PUT operation.  It returns the response text
        or an instance of ScoreboardScoreResponse.
        """
        path = f"/scoreboard/{scoreboard_id}/score"
        params = {}
        params["participant_id"] = participant_id
        params["value"] = value
        params["recorded"] = recorded

        try:
            response = self._client.put(path, params)
        except Exception as ex:
            print("client put exception:", ex, file=stderr)
            return
        if response.status_code < 200 or response.status_code >= 300:
            print(
                "client put client exception:", response.status_code, response.content, file=stderr
            )
            return
        return (
            response.text
            if self._output == Output.TEXT
            else types.ScoreboardScoreResponse(**response.json())
        )

    def scores(
        self,
        scoreboard_id: str,
        from_: Optional[datetime] = None,
        to: Optional[datetime] = None,
    ):
        """Scoreboard scores

        Reads and returns scoreboard scores

        This is a GET operation.  It returns the response text
        or an instance of ScoreboardScoresResponse.
        """
        path = f"/scoreboard/{scoreboard_id}/scores"
        params = {}
        if from_ is not None:
            params["from"] = from_
        if to is not None:
            params["to"] = to

        try:
            response = self._client.get(path, params=params)
        except Exception as ex:
            print("client get exception:", ex, file=stderr)
            return
        if response.status_code < 200 or response.status_code >= 300:
            print(
                "client get client exception:", response.status_code, response.content, file=stderr
            )
            return
        return (
            response.text
            if self._output == Output.TEXT
            else types.ScoreboardScoresResponse(**response.json())
        )

    def list(
        self,
        project_id: ULID | str,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ):
        """List scoreboards

        Reads and returns list of scoreboards in the given project

        This is a GET operation.  It returns the response text
        or an instance of ScoreboardListResponse.
        """
        path = f"/scoreboard"
        params = {}
        if project_id is not None:
            params["project_id"] = project_id
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset

        try:
            response = self._client.get(path, params=params)
        except Exception as ex:
            print("client get exception:", ex, file=stderr)
            return
        if response.status_code < 200 or response.status_code >= 300:
            print(
                "client get client exception:", response.status_code, response.content, file=stderr
            )
            return
        return (
            response.text
            if self._output == Output.TEXT
            else types.ScoreboardListResponse(**response.json())
        )

    def create(
        self,
        project_id: ULID | str,
        display: str,
        rank_dir: str,
        public: bool,
        extra: Optional[object],
    ):
        """Create scoreboard

        Creates and returns scoreboard in the given project

        This is a PUT operation.  It returns the response text
        or an instance of ScoreboardCreateResponse.
        """
        path = f"/scoreboard"
        params = {}
        params["project_id"] = project_id
        params["display"] = display
        params["rank_dir"] = rank_dir
        params["public"] = public
        params["extra"] = extra

        try:
            response = self._client.put(path, params)
        except Exception as ex:
            print("client put exception:", ex, file=stderr)
            return
        if response.status_code < 200 or response.status_code >= 300:
            print(
                "client put client exception:", response.status_code, response.content, file=stderr
            )
            return
        return (
            response.text
            if self._output == Output.TEXT
            else types.ScoreboardCreateResponse(**response.json())
        )

    def read(
        self,
        scoreboard_id: ULID | str,
    ):
        """Read scoreboard

        Reads and returns scoreboard by scoreboard id

        This is a GET operation.  It returns the response text
        or an instance of ScoreboardReadResponse.
        """
        path = f"/scoreboard/{scoreboard_id}"
        params = {}

        try:
            response = self._client.get(path, params=params)
        except Exception as ex:
            print("client get exception:", ex, file=stderr)
            return
        if response.status_code < 200 or response.status_code >= 300:
            print(
                "client get client exception:", response.status_code, response.content, file=stderr
            )
            return
        return (
            response.text
            if self._output == Output.TEXT
            else types.ScoreboardReadResponse(**response.json())
        )

    def update(
        self,
        scoreboard_id: ULID | str,
        display: str,
        rank_dir: str,
        public: bool,
        extra: Optional[object],
    ):
        """Update scoreboard

        Updates and returns scoreboard by scoreboard id

        This is a POST operation.  It returns the response text
        or an instance of ScoreboardUpdateResponse.
        """
        path = f"/scoreboard/{scoreboard_id}"
        params = {}
        params["display"] = display
        params["rank_dir"] = rank_dir
        params["public"] = public
        params["extra"] = extra

        try:
            response = self._client.post(path, params)
        except Exception as ex:
            print("client post exception:", ex, file=stderr)
            return
        if response.status_code < 200 or response.status_code >= 300:
            print(
                "client post client exception:",
                response.status_code,
                response.content,
                file=stderr,
            )
            return
        return (
            response.text
            if self._output == Output.TEXT
            else types.ScoreboardUpdateResponse(**response.json())
        )

    def delete(
        self,
        scoreboard_id: ULID | str,
    ):
        """Delete scoreboard by id.

        Delete scoreboard by scoreboard id

        This is a DELETE operation.  It returns the response text
        or an instance of ScoreboardDeleteResponse.
        """
        path = f"/scoreboard/{scoreboard_id}"

        try:
            response = self._client.delete(path)
        except Exception as ex:
            print("client delete exception:", ex, file=stderr)
            return
        if response.status_code < 200 or response.status_code >= 300:
            print(
                "client delete client exception:",
                response.status_code,
                response.content,
                file=stderr,
            )
            return
        return (
            response.text
            if self._output == Output.TEXT
            else types.ScoreboardDeleteResponse(**response.json())
        )


class API:
    achievement: Achievement
    participant: Participant
    scoreboard: Scoreboard
    verbose: bool

    def __init__(
        self,
        api_key: Optional[str] = None,
        tags: Set[str] = set(),
        client: Optional[Client] = None,
        output: Output = Output.OBJECT,
        verbose: bool = False,
    ):
        client = client or Client(client_config=ClientConfig(api_key=api_key, tags=tags))
        self.achievement = Achievement(client=client, output=output, verbose=verbose)
        self.participant = Participant(client=client, output=output, verbose=verbose)
        self.scoreboard = Scoreboard(client=client, output=output, verbose=verbose)
        self.verbose = verbose

    def api_version(self) -> str:
        """Returns the API version."""
        return "1.0.3"

    def client_version(self) -> str:
        """Returns the client version."""
        return "0.0.2"

