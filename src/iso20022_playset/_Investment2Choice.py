# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Deposit1
from . import OtherInvestment1
from . import RepurchaseAgreement2
from . import SecurityIdentificationAndAmount2

class Investment2Choice(base_types._BaseFieldType):

	__slots__ = ["_CntrlBkDpst", "_OthrInvstmts", "_OutrghtInvstmt", "_RpAgrmt", "_UscrdCshDpst"]
	@property
	def CntrlBkDpst(self):
		return self._CntrlBkDpst

	@CntrlBkDpst.setter
	def CntrlBkDpst(self, value):
		self._CntrlBkDpst = value if value is not None else base_types.UninitialisedField(self, 'CntrlBkDpst', Deposit1, False)

	@CntrlBkDpst.deleter
	def CntrlBkDpst(self):
		del self._CntrlBkDpst
		self._CntrlBkDpst = base_types.UninitialisedField(self, 'CntrlBkDpst', Deposit1, False)

	@property
	def OthrInvstmts(self):
		return self._OthrInvstmts

	@OthrInvstmts.setter
	def OthrInvstmts(self, value):
		self._OthrInvstmts = value if value is not None else base_types.UninitialisedField(self, 'OthrInvstmts', OtherInvestment1, False)

	@OthrInvstmts.deleter
	def OthrInvstmts(self):
		del self._OthrInvstmts
		self._OthrInvstmts = base_types.UninitialisedField(self, 'OthrInvstmts', OtherInvestment1, False)

	@property
	def OutrghtInvstmt(self):
		return self._OutrghtInvstmt

	@OutrghtInvstmt.setter
	def OutrghtInvstmt(self, value):
		self._OutrghtInvstmt = value if value is not None else base_types.UninitialisedField(self, 'OutrghtInvstmt', SecurityIdentificationAndAmount2, False)

	@OutrghtInvstmt.deleter
	def OutrghtInvstmt(self):
		del self._OutrghtInvstmt
		self._OutrghtInvstmt = base_types.UninitialisedField(self, 'OutrghtInvstmt', SecurityIdentificationAndAmount2, False)

	@property
	def RpAgrmt(self):
		return self._RpAgrmt

	@RpAgrmt.setter
	def RpAgrmt(self, value):
		self._RpAgrmt = value if value is not None else base_types.UninitialisedField(self, 'RpAgrmt', RepurchaseAgreement2, False)

	@RpAgrmt.deleter
	def RpAgrmt(self):
		del self._RpAgrmt
		self._RpAgrmt = base_types.UninitialisedField(self, 'RpAgrmt', RepurchaseAgreement2, False)

	@property
	def UscrdCshDpst(self):
		return self._UscrdCshDpst

	@UscrdCshDpst.setter
	def UscrdCshDpst(self, value):
		self._UscrdCshDpst = value if value is not None else base_types.UninitialisedField(self, 'UscrdCshDpst', Deposit1, False)

	@UscrdCshDpst.deleter
	def UscrdCshDpst(self):
		del self._UscrdCshDpst
		self._UscrdCshDpst = base_types.UninitialisedField(self, 'UscrdCshDpst', Deposit1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CntrlBkDpst', type=Deposit1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OthrInvstmts', type=OtherInvestment1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OutrghtInvstmt', type=SecurityIdentificationAndAmount2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RpAgrmt', type=RepurchaseAgreement2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UscrdCshDpst', type=Deposit1, min=0, max=1, mutex_group=1, array=False),
	))