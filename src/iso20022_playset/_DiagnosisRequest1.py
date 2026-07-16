# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import TrueFalseIndicator

class DiagnosisRequest1(base_types._BaseFieldType):

	__slots__ = ["_AcqrrId", "_HstDgnssFlg"]
	@property
	def AcqrrId(self):
		return self._AcqrrId

	@AcqrrId.setter
	def AcqrrId(self, value):
		self._AcqrrId = value if value is not None else base_types.UninitialisedField(self, 'AcqrrId', Max35Text, True)

	@AcqrrId.deleter
	def AcqrrId(self):
		del self._AcqrrId
		self._AcqrrId = base_types.UninitialisedField(self, 'AcqrrId', Max35Text, True)

	@property
	def HstDgnssFlg(self):
		return self._HstDgnssFlg

	@HstDgnssFlg.setter
	def HstDgnssFlg(self, value):
		self._HstDgnssFlg = value if value is not None else base_types.UninitialisedField(self, 'HstDgnssFlg', TrueFalseIndicator, False)

	@HstDgnssFlg.deleter
	def HstDgnssFlg(self):
		del self._HstDgnssFlg
		self._HstDgnssFlg = base_types.UninitialisedField(self, 'HstDgnssFlg', TrueFalseIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcqrrId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='HstDgnssFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))