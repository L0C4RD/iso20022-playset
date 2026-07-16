# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import TrueFalseIndicator

class HostStatus1(base_types._BaseFieldType):

	__slots__ = ["_AcqrrId", "_Rchbl"]
	@property
	def AcqrrId(self):
		return self._AcqrrId

	@AcqrrId.setter
	def AcqrrId(self, value):
		self._AcqrrId = value if value is not None else base_types.UninitialisedField(self, 'AcqrrId', Max35Text, False)

	@AcqrrId.deleter
	def AcqrrId(self):
		del self._AcqrrId
		self._AcqrrId = base_types.UninitialisedField(self, 'AcqrrId', Max35Text, False)

	@property
	def Rchbl(self):
		return self._Rchbl

	@Rchbl.setter
	def Rchbl(self, value):
		self._Rchbl = value if value is not None else base_types.UninitialisedField(self, 'Rchbl', TrueFalseIndicator, False)

	@Rchbl.deleter
	def Rchbl(self):
		del self._Rchbl
		self._Rchbl = base_types.UninitialisedField(self, 'Rchbl', TrueFalseIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcqrrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rchbl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))