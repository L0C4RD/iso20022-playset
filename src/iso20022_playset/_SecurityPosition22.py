# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import EligiblePosition20
from . import SecurityIdentification19

class SecurityPosition22(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmId", "_Pos"]
	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@property
	def Pos(self):
		return self._Pos

	@Pos.setter
	def Pos(self, value):
		self._Pos = value if value is not None else base_types.UninitialisedField(self, 'Pos', EligiblePosition20, True)

	@Pos.deleter
	def Pos(self):
		del self._Pos
		self._Pos = base_types.UninitialisedField(self, 'Pos', EligiblePosition20, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pos', type=EligiblePosition20, min=0, max=1000, mutex_group=None, array=True),
	))