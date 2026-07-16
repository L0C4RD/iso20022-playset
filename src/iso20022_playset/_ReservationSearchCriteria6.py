# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification4Choice
from . import BranchAndFinancialInstitutionIdentification8
from . import DateTimeSearch2Choice
from . import ReservationType2Choice
from . import SystemIdentification2Choice

class ReservationSearchCriteria6(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_AcctOwnr", "_CurRsvatnTp", "_DfltRsvatnTp", "_DtTm", "_SysId"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', AccountIdentification4Choice, False)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', AccountIdentification4Choice, False)

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnr', BranchAndFinancialInstitutionIdentification8, False)

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = base_types.UninitialisedField(self, 'AcctOwnr', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def CurRsvatnTp(self):
		return self._CurRsvatnTp

	@CurRsvatnTp.setter
	def CurRsvatnTp(self, value):
		self._CurRsvatnTp = value if value is not None else base_types.UninitialisedField(self, 'CurRsvatnTp', ReservationType2Choice, True)

	@CurRsvatnTp.deleter
	def CurRsvatnTp(self):
		del self._CurRsvatnTp
		self._CurRsvatnTp = base_types.UninitialisedField(self, 'CurRsvatnTp', ReservationType2Choice, True)

	@property
	def DfltRsvatnTp(self):
		return self._DfltRsvatnTp

	@DfltRsvatnTp.setter
	def DfltRsvatnTp(self, value):
		self._DfltRsvatnTp = value if value is not None else base_types.UninitialisedField(self, 'DfltRsvatnTp', ReservationType2Choice, True)

	@DfltRsvatnTp.deleter
	def DfltRsvatnTp(self):
		del self._DfltRsvatnTp
		self._DfltRsvatnTp = base_types.UninitialisedField(self, 'DfltRsvatnTp', ReservationType2Choice, True)

	@property
	def DtTm(self):
		return self._DtTm

	@DtTm.setter
	def DtTm(self, value):
		self._DtTm = value if value is not None else base_types.UninitialisedField(self, 'DtTm', DateTimeSearch2Choice, False)

	@DtTm.deleter
	def DtTm(self):
		del self._DtTm
		self._DtTm = base_types.UninitialisedField(self, 'DtTm', DateTimeSearch2Choice, False)

	@property
	def SysId(self):
		return self._SysId

	@SysId.setter
	def SysId(self, value):
		self._SysId = value if value is not None else base_types.UninitialisedField(self, 'SysId', SystemIdentification2Choice, False)

	@SysId.deleter
	def SysId(self):
		del self._SysId
		self._SysId = base_types.UninitialisedField(self, 'SysId', SystemIdentification2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=AccountIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurRsvatnTp', type=ReservationType2Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DfltRsvatnTp', type=ReservationType2Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DtTm', type=DateTimeSearch2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysId', type=SystemIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
	))