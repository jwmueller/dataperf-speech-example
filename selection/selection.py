from typing import Dict, List
import dataclasses


@dataclasses.dataclass
#dict {"targets": {"dog":[list of IDs], ...}, "nontargets": [list of IDs]}
class TrainingSet:
    targets: Dict[str, List[str]]
    nontargets: List[str]


# include additional dependencies as needed
from random import sample


class TrainingSetSelection:
    def __init__(
        self,
        train_embeddings,
        train_set_size,
        audio_flag=False
    ) -> None:
        """
        Args:
            train_embeddings: dict {"targets": {"dog":[{'ID':string,'feature_vector':np.array,'audio':np.array}, ...], ...}, "nontargets": [list]}

            train_set_size: int (total number of samples to select)

            audio_flag: bool (if audio is included in the training_embeddings)

        """

        self.target_vectors = train_embeddings
        # {"targets": {"dog":[{'ID':string,'feature_vector':np.array,'audio':np.array}, ...], ...},
        #  "nontargets": [{'ID':string,'feature_vector':np.array,'audio':np.array}, ...]}
        self.train_set_size = train_set_size
        self.audio_flag = audio_flag

    def select(self):
        """"
        Replace this with your custom training set selection algorithm

        Returns: 
            TrainingSet
        """

        if self.audio_flag:
            print(self.target_vectors['non_targets'][0]['audio'])

        per_class_size = self.train_set_size // 6 #5 targets + nontarget

        selected_targets = {}
        for target, sample_list in self.target_vectors['targets'].items():
            selected_samples = sample(sample_list, per_class_size)
            selected_targets[target] = [sample['ID'] for sample in selected_samples]

        selected_nontarget_samples = sample(self.target_vectors['non_targets'], per_class_size)
        selected_nontargets = [sample['ID'] for sample in selected_nontarget_samples]


        training_set = TrainingSet(
            targets= selected_targets,
            nontargets= selected_nontargets,
        )

        return training_set
