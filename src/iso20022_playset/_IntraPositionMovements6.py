# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IntraPositionMovement10 import IntraPositionMovement10
from ._IntraPositionStatusAndReason4 import IntraPositionStatusAndReason4
from ._SecuritiesAccount19 import SecuritiesAccount19
from ._SystemPartyIdentification8 import SystemPartyIdentification8

class IntraPositionMovements6(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_Mvmnt", "_SfkpgAcct", "_StsAndRsn"]
	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != base_types.auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	@property
	def Mvmnt(self):
		return self._Mvmnt

	@Mvmnt.setter
	def Mvmnt(self, value):
		self._Mvmnt = value if type(value) != base_types.auto else self.make_default("Mvmnt")

	@Mvmnt.deleter
	def Mvmnt(self):
		del self._Mvmnt
		self._Mvmnt = None

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if type(value) != base_types.auto else self.make_default("SfkpgAcct")

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = None

	@property
	def StsAndRsn(self):
		return self._StsAndRsn

	@StsAndRsn.setter
	def StsAndRsn(self, value):
		self._StsAndRsn = value if type(value) != base_types.auto else self.make_default("StsAndRsn")

	@StsAndRsn.deleter
	def StsAndRsn(self):
		del self._StsAndRsn
		self._StsAndRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=SystemPartyIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mvmnt', type=IntraPositionMovement10, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsAndRsn', type=IntraPositionStatusAndReason4, min=0, max=1, mutex_group=None, array=False),
	))