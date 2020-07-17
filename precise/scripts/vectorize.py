#!/usr/bin/env python3
# Copyright 2019 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Package a dataset into a numpy file

:output_file str
    Numpy npz file to write dataset to

:-p --params-file str -
    Params file to read from

...
"""
from prettyparse import Usage

from precise.params import inject_params
from precise.scripts.base_script import BaseScript
from precise.train_data import TrainData


class VectorizeScript(BaseScript):
    usage = Usage(__doc__) | TrainData.usage

    def run(self):
        if self.args.params_file:
            inject_params(self.args.params_file.replace('.params', ''))
        data = TrainData.from_both(self.args.tags_file, self.args.tags_folder, self.args.folder)
        (train_in, train_out), (test_in, test_out) = data.load()
        import numpy as np
        np.savez(train_in=train_in, train_out=train_out, test_in=test_in, test_out=test_out)


if __name__ == '__main__':
    VectorizeScript.run_main()
