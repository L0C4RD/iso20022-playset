import base_types
import ProcessingStatus71Choice
import SystemPartyIdentification8
import RequestDetails22
import Max35Text
import ISODateTime
import CashAccount40
import IntraBalance5
import BranchAndFinancialInstitutionIdentification8

class IntraBalanceModification8(base_types._BaseFieldType):

	__slots__ = ["_CshAcct", "_PrcgSts", "_CshAcctSvcr", "_ReqRef", "_ReqDtls", "_UndrlygIntraBal", "_StsDt", "_CshAcctOwnr"]
	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if type(value) != auto else self.make_default("CshAcct")

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = None

	@property
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if type(value) != auto else self.make_default("PrcgSts")

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = None

	@property
	def CshAcctSvcr(self):
		return self._CshAcctSvcr

	@CshAcctSvcr.setter
	def CshAcctSvcr(self, value):
		self._CshAcctSvcr = value if type(value) != auto else self.make_default("CshAcctSvcr")

	@CshAcctSvcr.deleter
	def CshAcctSvcr(self):
		del self._CshAcctSvcr
		self._CshAcctSvcr = None

	@property
	def ReqRef(self):
		return self._ReqRef

	@ReqRef.setter
	def ReqRef(self, value):
		self._ReqRef = value if type(value) != auto else self.make_default("ReqRef")

	@ReqRef.deleter
	def ReqRef(self):
		del self._ReqRef
		self._ReqRef = None

	@property
	def ReqDtls(self):
		return self._ReqDtls

	@ReqDtls.setter
	def ReqDtls(self, value):
		self._ReqDtls = value if type(value) != auto else self.make_default("ReqDtls")

	@ReqDtls.deleter
	def ReqDtls(self):
		del self._ReqDtls
		self._ReqDtls = None

	@property
	def UndrlygIntraBal(self):
		return self._UndrlygIntraBal

	@UndrlygIntraBal.setter
	def UndrlygIntraBal(self, value):
		self._UndrlygIntraBal = value if type(value) != auto else self.make_default("UndrlygIntraBal")

	@UndrlygIntraBal.deleter
	def UndrlygIntraBal(self):
		del self._UndrlygIntraBal
		self._UndrlygIntraBal = None

	@property
	def StsDt(self):
		return self._StsDt

	@StsDt.setter
	def StsDt(self, value):
		self._StsDt = value if type(value) != auto else self.make_default("StsDt")

	@StsDt.deleter
	def StsDt(self):
		del self._StsDt
		self._StsDt = None

	@property
	def CshAcctOwnr(self):
		return self._CshAcctOwnr

	@CshAcctOwnr.setter
	def CshAcctOwnr(self, value):
		self._CshAcctOwnr = value if type(value) != auto else self.make_default("CshAcctOwnr")

	@CshAcctOwnr.deleter
	def CshAcctOwnr(self):
		del self._CshAcctOwnr
		self._CshAcctOwnr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgSts', type=ProcessingStatus71Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctSvcr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqDtls', type=RequestDetails22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygIntraBal', type=IntraBalance5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctOwnr', type=SystemPartyIdentification8, min=0, max=1, mutex_group=None, array=False),
	))

