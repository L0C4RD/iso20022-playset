from . import base_types
from .Deposit1 import Deposit1
from .SecurityIdentificationAndAmount2 import SecurityIdentificationAndAmount2
from .RepurchaseAgreement2 import RepurchaseAgreement2
from .OtherInvestment1 import OtherInvestment1

class Investment2Choice(base_types._BaseFieldType):

	__slots__ = ["_UscrdCshDpst", "_CntrlBkDpst", "_OutrghtInvstmt", "_RpAgrmt", "_OthrInvstmts"]
	@property
	def UscrdCshDpst(self):
		return self._UscrdCshDpst

	@UscrdCshDpst.setter
	def UscrdCshDpst(self, value):
		self._UscrdCshDpst = value if type(value) != auto else self.make_default("UscrdCshDpst")

	@UscrdCshDpst.deleter
	def UscrdCshDpst(self):
		del self._UscrdCshDpst
		self._UscrdCshDpst = None

	@property
	def CntrlBkDpst(self):
		return self._CntrlBkDpst

	@CntrlBkDpst.setter
	def CntrlBkDpst(self, value):
		self._CntrlBkDpst = value if type(value) != auto else self.make_default("CntrlBkDpst")

	@CntrlBkDpst.deleter
	def CntrlBkDpst(self):
		del self._CntrlBkDpst
		self._CntrlBkDpst = None

	@property
	def OutrghtInvstmt(self):
		return self._OutrghtInvstmt

	@OutrghtInvstmt.setter
	def OutrghtInvstmt(self, value):
		self._OutrghtInvstmt = value if type(value) != auto else self.make_default("OutrghtInvstmt")

	@OutrghtInvstmt.deleter
	def OutrghtInvstmt(self):
		del self._OutrghtInvstmt
		self._OutrghtInvstmt = None

	@property
	def RpAgrmt(self):
		return self._RpAgrmt

	@RpAgrmt.setter
	def RpAgrmt(self, value):
		self._RpAgrmt = value if type(value) != auto else self.make_default("RpAgrmt")

	@RpAgrmt.deleter
	def RpAgrmt(self):
		del self._RpAgrmt
		self._RpAgrmt = None

	@property
	def OthrInvstmts(self):
		return self._OthrInvstmts

	@OthrInvstmts.setter
	def OthrInvstmts(self, value):
		self._OthrInvstmts = value if type(value) != auto else self.make_default("OthrInvstmts")

	@OthrInvstmts.deleter
	def OthrInvstmts(self):
		del self._OthrInvstmts
		self._OthrInvstmts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UscrdCshDpst', type=Deposit1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CntrlBkDpst', type=Deposit1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OutrghtInvstmt', type=SecurityIdentificationAndAmount2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RpAgrmt', type=RepurchaseAgreement2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OthrInvstmts', type=OtherInvestment1, min=0, max=1, mutex_group=1, array=False),
	))

