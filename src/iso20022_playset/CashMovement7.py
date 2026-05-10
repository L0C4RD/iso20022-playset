import base_types
import Max35Text
import ActiveCurrencyAndAmount
import YesNoIndicator
import ProprietaryStatusAndReason6
import CashAccountIdentification5Choice
import CreditDebit3Code

class CashMovement7(base_types._BaseFieldType):

	__slots__ = ["_CshAmt", "_ClntCshMvmntId", "_CshAcct", "_MvmntSts", "_CshMvmnt", "_TrptyAgtSvcPrvdrCshMvmntId", "_CshMvmntApprvd", "_CollMvmnt", "_PosTp"]
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
	def MvmntSts(self):
		return self._MvmntSts

	@MvmntSts.setter
	def MvmntSts(self, value):
		self._MvmntSts = value if type(value) != auto else self.make_default("MvmntSts")

	@MvmntSts.deleter
	def MvmntSts(self):
		del self._MvmntSts
		self._MvmntSts = None

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
	def CshMvmntApprvd(self):
		return self._CshMvmntApprvd

	@CshMvmntApprvd.setter
	def CshMvmntApprvd(self, value):
		self._CshMvmntApprvd = value if type(value) != auto else self.make_default("CshMvmntApprvd")

	@CshMvmntApprvd.deleter
	def CshMvmntApprvd(self):
		del self._CshMvmntApprvd
		self._CshMvmntApprvd = None

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
	def PosTp(self):
		return self._PosTp

	@PosTp.setter
	def PosTp(self, value):
		self._PosTp = value if type(value) != auto else self.make_default("PosTp")

	@PosTp.deleter
	def PosTp(self):
		del self._PosTp
		self._PosTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntCshMvmntId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcct', type=CashAccountIdentification5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MvmntSts', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshMvmnt', type=CreditDebit3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgtSvcPrvdrCshMvmntId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshMvmntApprvd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollMvmnt', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PosTp', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

