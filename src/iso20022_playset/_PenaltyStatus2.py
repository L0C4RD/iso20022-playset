# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PenaltyStatus2Choice
from . import PenaltyStatusReason2

class PenaltyStatus2(base_types._BaseFieldType):

	__slots__ = ["_Rsn", "_Sts"]
	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', PenaltyStatusReason2, True)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', PenaltyStatusReason2, True)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', PenaltyStatus2Choice, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', PenaltyStatus2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rsn', type=PenaltyStatusReason2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=PenaltyStatus2Choice, min=1, max=1, mutex_group=None, array=False),
	))