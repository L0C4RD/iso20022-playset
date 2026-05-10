from . import base_types
import TransactionInitiator1Code
import ISO18245MerchantCategoryCode
import TrueFalseIndicator
import AdditionalData1
import Max35Text

class Context22(base_types._BaseFieldType):

	__slots__ = ["_OthrMrchntCtgy", "_MrchntCtgySpcfcData", "_PrtlShipmnt", "_MrchntCtgyCd", "_Reauthstn", "_AddtlData", "_TxInitr", "_NoShow", "_DelydChrgs", "_ReSubmissn"]
	@property
	def OthrMrchntCtgy(self):
		return self._OthrMrchntCtgy

	@OthrMrchntCtgy.setter
	def OthrMrchntCtgy(self, value):
		self._OthrMrchntCtgy = value if type(value) != auto else self.make_default("OthrMrchntCtgy")

	@OthrMrchntCtgy.deleter
	def OthrMrchntCtgy(self):
		del self._OthrMrchntCtgy
		self._OthrMrchntCtgy = None

	@property
	def MrchntCtgySpcfcData(self):
		return self._MrchntCtgySpcfcData

	@MrchntCtgySpcfcData.setter
	def MrchntCtgySpcfcData(self, value):
		self._MrchntCtgySpcfcData = value if type(value) != auto else self.make_default("MrchntCtgySpcfcData")

	@MrchntCtgySpcfcData.deleter
	def MrchntCtgySpcfcData(self):
		del self._MrchntCtgySpcfcData
		self._MrchntCtgySpcfcData = None

	@property
	def PrtlShipmnt(self):
		return self._PrtlShipmnt

	@PrtlShipmnt.setter
	def PrtlShipmnt(self, value):
		self._PrtlShipmnt = value if type(value) != auto else self.make_default("PrtlShipmnt")

	@PrtlShipmnt.deleter
	def PrtlShipmnt(self):
		del self._PrtlShipmnt
		self._PrtlShipmnt = None

	@property
	def MrchntCtgyCd(self):
		return self._MrchntCtgyCd

	@MrchntCtgyCd.setter
	def MrchntCtgyCd(self, value):
		self._MrchntCtgyCd = value if type(value) != auto else self.make_default("MrchntCtgyCd")

	@MrchntCtgyCd.deleter
	def MrchntCtgyCd(self):
		del self._MrchntCtgyCd
		self._MrchntCtgyCd = None

	@property
	def Reauthstn(self):
		return self._Reauthstn

	@Reauthstn.setter
	def Reauthstn(self, value):
		self._Reauthstn = value if type(value) != auto else self.make_default("Reauthstn")

	@Reauthstn.deleter
	def Reauthstn(self):
		del self._Reauthstn
		self._Reauthstn = None

	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

	@property
	def TxInitr(self):
		return self._TxInitr

	@TxInitr.setter
	def TxInitr(self, value):
		self._TxInitr = value if type(value) != auto else self.make_default("TxInitr")

	@TxInitr.deleter
	def TxInitr(self):
		del self._TxInitr
		self._TxInitr = None

	@property
	def NoShow(self):
		return self._NoShow

	@NoShow.setter
	def NoShow(self, value):
		self._NoShow = value if type(value) != auto else self.make_default("NoShow")

	@NoShow.deleter
	def NoShow(self):
		del self._NoShow
		self._NoShow = None

	@property
	def DelydChrgs(self):
		return self._DelydChrgs

	@DelydChrgs.setter
	def DelydChrgs(self, value):
		self._DelydChrgs = value if type(value) != auto else self.make_default("DelydChrgs")

	@DelydChrgs.deleter
	def DelydChrgs(self):
		del self._DelydChrgs
		self._DelydChrgs = None

	@property
	def ReSubmissn(self):
		return self._ReSubmissn

	@ReSubmissn.setter
	def ReSubmissn(self, value):
		self._ReSubmissn = value if type(value) != auto else self.make_default("ReSubmissn")

	@ReSubmissn.deleter
	def ReSubmissn(self):
		del self._ReSubmissn
		self._ReSubmissn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrMrchntCtgy', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntCtgySpcfcData', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlShipmnt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntCtgyCd', type=ISO18245MerchantCategoryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Reauthstn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxInitr', type=TransactionInitiator1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NoShow', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DelydChrgs', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReSubmissn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))

