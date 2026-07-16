# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import PartialSettlement2Code
from . import PreConfirmation1Code

class AdditionalParameters24(base_types._BaseFieldType):

	__slots__ = ["_PreConf", "_PrtlSttlm", "_PrvsPrtlConfId"]
	@property
	def PreConf(self):
		return self._PreConf

	@PreConf.setter
	def PreConf(self, value):
		self._PreConf = value if value is not None else base_types.UninitialisedField(self, 'PreConf', PreConfirmation1Code, False)

	@PreConf.deleter
	def PreConf(self):
		del self._PreConf
		self._PreConf = base_types.UninitialisedField(self, 'PreConf', PreConfirmation1Code, False)

	@property
	def PrtlSttlm(self):
		return self._PrtlSttlm

	@PrtlSttlm.setter
	def PrtlSttlm(self, value):
		self._PrtlSttlm = value if value is not None else base_types.UninitialisedField(self, 'PrtlSttlm', PartialSettlement2Code, False)

	@PrtlSttlm.deleter
	def PrtlSttlm(self):
		del self._PrtlSttlm
		self._PrtlSttlm = base_types.UninitialisedField(self, 'PrtlSttlm', PartialSettlement2Code, False)

	@property
	def PrvsPrtlConfId(self):
		return self._PrvsPrtlConfId

	@PrvsPrtlConfId.setter
	def PrvsPrtlConfId(self, value):
		self._PrvsPrtlConfId = value if value is not None else base_types.UninitialisedField(self, 'PrvsPrtlConfId', Max35Text, False)

	@PrvsPrtlConfId.deleter
	def PrvsPrtlConfId(self):
		del self._PrvsPrtlConfId
		self._PrvsPrtlConfId = base_types.UninitialisedField(self, 'PrvsPrtlConfId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PreConf', type=PreConfirmation1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlSttlm', type=PartialSettlement2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsPrtlConfId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))