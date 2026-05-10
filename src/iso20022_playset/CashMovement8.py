import base_types
import YesNoIndicator
import CollateralEntryType1Code
import Max35Text
import CashAccountIdentification5Choice
import ActiveCurrencyAndAmount

class CashMovement8(base_types._BaseFieldType):

	__slots__ = ["_CshAcct", "_TrptyAgtSvcPrvdrCshMvmntId", "_CshMvmnt", "_CollMvmnt", "_ClntCshMvmntId", "_CshAmt"]
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
	def TrptyAgtSvcPrvdrCshMvmntId(self):
		return self._TrptyAgtSvcPrvdrCshMvmntId

	@TrptyAgtSvcPrvdrCshMvmntId.setter
	def TrptyAgtSvcPrvdrCshMvmntId(self, value):
		self._TrptyAgtSvcPrvdrCshMvmntId = value if type(value) != auto else self.make_default("TrptyAgtSvcPrvdrCshMvmntId")

	@TrptyAgtSvcPrvdrCshMvmntId.deleter
	def TrptyAgtSvcPrvdrCshMvmntId(self):
		del self._TrptyAgtSvcPrvdrCshMvmntId
		self._TrptyAgtSvcPrvdrCshMvmntId = None

	@property
	def CshMvmnt(self):
		return self._CshMvmnt

	@CshMvmnt.setter
	def CshMvmnt(self, value):
		self._CshMvmnt = value if type(value) != auto else self.make_default("CshMvmnt")

	@CshMvmnt.deleter
	def CshMvmnt(self):
		del self._CshMvmnt
		self._CshMvmnt = None

	@property
	def CollMvmnt(self):
		return self._CollMvmnt

	@CollMvmnt.setter
	def CollMvmnt(self, value):
		self._CollMvmnt = value if type(value) != auto else self.make_default("CollMvmnt")

	@CollMvmnt.deleter
	def CollMvmnt(self):
		del self._CollMvmnt
		self._CollMvmnt = None

	@property
	def ClntCshMvmntId(self):
		return self._ClntCshMvmntId

	@ClntCshMvmntId.setter
	def ClntCshMvmntId(self, value):
		self._ClntCshMvmntId = value if type(value) != auto else self.make_default("ClntCshMvmntId")

	@ClntCshMvmntId.deleter
	def ClntCshMvmntId(self):
		del self._ClntCshMvmntId
		self._ClntCshMvmntId = None

	@property
	def CshAmt(self):
		return self._CshAmt

	@CshAmt.setter
	def CshAmt(self, value):
		self._CshAmt = value if type(value) != auto else self.make_default("CshAmt")

	@CshAmt.deleter
	def CshAmt(self):
		del self._CshAmt
		self._CshAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshAcct', type=CashAccountIdentification5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgtSvcPrvdrCshMvmntId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshMvmnt', type=CollateralEntryType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollMvmnt', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntCshMvmntId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

