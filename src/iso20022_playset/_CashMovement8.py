from . import base_types
from ._YesNoIndicator import YesNoIndicator
from ._Max35Text import Max35Text
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._CollateralEntryType1Code import CollateralEntryType1Code
from ._CashAccountIdentification5Choice import CashAccountIdentification5Choice

class CashMovement8(base_types._BaseFieldType):

	__slots__ = ["_ClntCshMvmntId", "_CshMvmnt", "_CollMvmnt", "_CshAcct", "_CshAmt", "_TrptyAgtSvcPrvdrCshMvmntId"]
	@property
	def ClntCshMvmntId(self):
		return self._ClntCshMvmntId

	@ClntCshMvmntId.setter
	def ClntCshMvmntId(self, value):
		self._ClntCshMvmntId = value if type(value) != base_types.auto else self.make_default("ClntCshMvmntId")

	@ClntCshMvmntId.deleter
	def ClntCshMvmntId(self):
		del self._ClntCshMvmntId
		self._ClntCshMvmntId = None

	@property
	def CollMvmnt(self):
		return self._CollMvmnt

	@CollMvmnt.setter
	def CollMvmnt(self, value):
		self._CollMvmnt = value if type(value) != base_types.auto else self.make_default("CollMvmnt")

	@CollMvmnt.deleter
	def CollMvmnt(self):
		del self._CollMvmnt
		self._CollMvmnt = None

	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if type(value) != base_types.auto else self.make_default("CshAcct")

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = None

	@property
	def CshAmt(self):
		return self._CshAmt

	@CshAmt.setter
	def CshAmt(self, value):
		self._CshAmt = value if type(value) != base_types.auto else self.make_default("CshAmt")

	@CshAmt.deleter
	def CshAmt(self):
		del self._CshAmt
		self._CshAmt = None

	@property
	def CshMvmnt(self):
		return self._CshMvmnt

	@CshMvmnt.setter
	def CshMvmnt(self, value):
		self._CshMvmnt = value if type(value) != base_types.auto else self.make_default("CshMvmnt")

	@CshMvmnt.deleter
	def CshMvmnt(self):
		del self._CshMvmnt
		self._CshMvmnt = None

	@property
	def TrptyAgtSvcPrvdrCshMvmntId(self):
		return self._TrptyAgtSvcPrvdrCshMvmntId

	@TrptyAgtSvcPrvdrCshMvmntId.setter
	def TrptyAgtSvcPrvdrCshMvmntId(self, value):
		self._TrptyAgtSvcPrvdrCshMvmntId = value if type(value) != base_types.auto else self.make_default("TrptyAgtSvcPrvdrCshMvmntId")

	@TrptyAgtSvcPrvdrCshMvmntId.deleter
	def TrptyAgtSvcPrvdrCshMvmntId(self):
		del self._TrptyAgtSvcPrvdrCshMvmntId
		self._TrptyAgtSvcPrvdrCshMvmntId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClntCshMvmntId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollMvmnt', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcct', type=CashAccountIdentification5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshMvmnt', type=CollateralEntryType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgtSvcPrvdrCshMvmntId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

