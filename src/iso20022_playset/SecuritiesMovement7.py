import base_types
import Max35Text
import CollateralEntryType1Code
import FinancialInstrumentQuantity33Choice
import YesNoIndicator
import SecurityIdentification19

class SecuritiesMovement7(base_types._BaseFieldType):

	__slots__ = ["_Qty", "_SctiesMvmntTp", "_TrptyAgtSvcPrvdrSctiesMvmntId", "_CollMvmnt", "_FinInstrmId", "_ClntSctiesMvmntId"]
	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	@property
	def SctiesMvmntTp(self):
		return self._SctiesMvmntTp

	@SctiesMvmntTp.setter
	def SctiesMvmntTp(self, value):
		self._SctiesMvmntTp = value if type(value) != auto else self.make_default("SctiesMvmntTp")

	@SctiesMvmntTp.deleter
	def SctiesMvmntTp(self):
		del self._SctiesMvmntTp
		self._SctiesMvmntTp = None

	@property
	def TrptyAgtSvcPrvdrSctiesMvmntId(self):
		return self._TrptyAgtSvcPrvdrSctiesMvmntId

	@TrptyAgtSvcPrvdrSctiesMvmntId.setter
	def TrptyAgtSvcPrvdrSctiesMvmntId(self, value):
		self._TrptyAgtSvcPrvdrSctiesMvmntId = value if type(value) != auto else self.make_default("TrptyAgtSvcPrvdrSctiesMvmntId")

	@TrptyAgtSvcPrvdrSctiesMvmntId.deleter
	def TrptyAgtSvcPrvdrSctiesMvmntId(self):
		del self._TrptyAgtSvcPrvdrSctiesMvmntId
		self._TrptyAgtSvcPrvdrSctiesMvmntId = None

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
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def ClntSctiesMvmntId(self):
		return self._ClntSctiesMvmntId

	@ClntSctiesMvmntId.setter
	def ClntSctiesMvmntId(self, value):
		self._ClntSctiesMvmntId = value if type(value) != auto else self.make_default("ClntSctiesMvmntId")

	@ClntSctiesMvmntId.deleter
	def ClntSctiesMvmntId(self):
		del self._ClntSctiesMvmntId
		self._ClntSctiesMvmntId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity33Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmntTp', type=CollateralEntryType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgtSvcPrvdrSctiesMvmntId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollMvmnt', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntSctiesMvmntId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

