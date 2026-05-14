# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max210Text import Max210Text
from ._PenaltyStatusReason2Choice import PenaltyStatusReason2Choice

class PenaltyStatusReason2(base_types._BaseFieldType):

	__slots__ = ["_AddtlStsRsn", "_Rsn"]
	@property
	def AddtlStsRsn(self):
		return self._AddtlStsRsn

	@AddtlStsRsn.setter
	def AddtlStsRsn(self, value):
		self._AddtlStsRsn = value if type(value) != base_types.auto else self.make_default("AddtlStsRsn")

	@AddtlStsRsn.deleter
	def AddtlStsRsn(self):
		del self._AddtlStsRsn
		self._AddtlStsRsn = None

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != base_types.auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlStsRsn', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=PenaltyStatusReason2Choice, min=1, max=1, mutex_group=None, array=False),
	))