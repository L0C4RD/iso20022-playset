# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max210Text
from . import PenaltyStatusReason2Choice

class PenaltyStatusReason2(base_types._BaseFieldType):

	__slots__ = ["_AddtlStsRsn", "_Rsn"]
	@property
	def AddtlStsRsn(self):
		return self._AddtlStsRsn

	@AddtlStsRsn.setter
	def AddtlStsRsn(self, value):
		self._AddtlStsRsn = value if value is not None else base_types.UninitialisedField(self, 'AddtlStsRsn', Max210Text, False)

	@AddtlStsRsn.deleter
	def AddtlStsRsn(self):
		del self._AddtlStsRsn
		self._AddtlStsRsn = base_types.UninitialisedField(self, 'AddtlStsRsn', Max210Text, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', PenaltyStatusReason2Choice, False)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', PenaltyStatusReason2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlStsRsn', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=PenaltyStatusReason2Choice, min=1, max=1, mutex_group=None, array=False),
	))