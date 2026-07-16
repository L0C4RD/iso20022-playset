# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IntraPositionMovement10
from . import IntraPositionStatusAndReason4
from . import SecuritiesAccount19
from . import SystemPartyIdentification8

class IntraPositionMovements6(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_Mvmnt", "_SfkpgAcct", "_StsAndRsn"]
	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnr', SystemPartyIdentification8, False)

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = base_types.UninitialisedField(self, 'AcctOwnr', SystemPartyIdentification8, False)

	@property
	def Mvmnt(self):
		return self._Mvmnt

	@Mvmnt.setter
	def Mvmnt(self, value):
		self._Mvmnt = value if value is not None else base_types.UninitialisedField(self, 'Mvmnt', IntraPositionMovement10, True)

	@Mvmnt.deleter
	def Mvmnt(self):
		del self._Mvmnt
		self._Mvmnt = base_types.UninitialisedField(self, 'Mvmnt', IntraPositionMovement10, True)

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if value is not None else base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount19, False)

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount19, False)

	@property
	def StsAndRsn(self):
		return self._StsAndRsn

	@StsAndRsn.setter
	def StsAndRsn(self, value):
		self._StsAndRsn = value if value is not None else base_types.UninitialisedField(self, 'StsAndRsn', IntraPositionStatusAndReason4, False)

	@StsAndRsn.deleter
	def StsAndRsn(self):
		del self._StsAndRsn
		self._StsAndRsn = base_types.UninitialisedField(self, 'StsAndRsn', IntraPositionStatusAndReason4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=SystemPartyIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mvmnt', type=IntraPositionMovement10, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsAndRsn', type=IntraPositionStatusAndReason4, min=0, max=1, mutex_group=None, array=False),
	))